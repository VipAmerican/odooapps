# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, SUPERUSER_ID, _, Command
from odoo.exceptions import UserError


class Partner(models.Model):
    _inherit = "res.partner"

    x_customer_id = fields.Char(string='Customer ID')
    x_vendor_id = fields.Char(string='Vendor ID')
    customer_rank = fields.Integer(default=1, copy=False)

    _sql_constraints = [
        ('customer_company_uniq', 'Check(1=1)', 'The customer id must be unique per company !'),
        ('vendor_company_uniq', 'Check(1=1)', 'The vendor id must be unique per company !'),
    ]

    @api.model
    def create(self, vals):
        result = super(Partner, self).create(vals)
        if not result.parent_id and result.customer_rank:
            result.x_customer_id = self.env['ir.sequence'].next_by_code('res.customer')
        elif not result.parent_id and result.supplier_rank:
            result.x_vendor_id = self.env['ir.sequence'].next_by_code('res.vendor')
        return result
