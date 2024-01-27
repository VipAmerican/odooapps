# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_id = fields.Char(string='Customer ID', compute='get_client_id_value', store=True)

    @api.onchange('partner_id')
    def get_client_id_value(self):
        for rec in self:
            if rec.partner_id:
                if rec.partner_id.customer_rank > 0:
                    if rec.partner_id.x_customer_id:
                        rec.customer_id = rec.partner_id.x_customer_id
                    else:
                        rec.customer_id = False
                elif rec.partner_id.supplier_rank > 0:
                    if rec.partner_id.x_vendor_id:
                        rec.customer_id = rec.partner_id.x_vendor_id
                    else:
                        rec.customer_id = False
                else:
                    rec.customer_id = False
            else:
                rec.customer_id = False
