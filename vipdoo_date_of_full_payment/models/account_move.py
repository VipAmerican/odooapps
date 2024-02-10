# -*- coding: utf-8 -*-
import datetime

from odoo import api, fields, models, Command, _


class AccountMove(models.Model):
    _inherit = "account.move"

    date_of_full_payment = fields.Datetime(string='Date of Full Payment', store=True, compute='get_date_of_full_payment')

    @api.onchange("payment_state")
    @api.depends("payment_state")
    def get_date_of_full_payment(self):
        for rec in self:
            if rec.payment_state == 'paid':
                if not rec.date_of_full_payment:
                    rec.date_of_full_payment = datetime.datetime.now()
