# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
class check_vaucher_do(models.Model):
     _name = 'check.vaucher_do'

     date_con = fields.Date(string="Fecha", required=False, )

     description = fields.Char(string="Descripcion", required=True, )
     amount_check = fields.Float(string="Monto",  required=True, )
     concept_id = fields.Many2one(comodel_name="account.voucher", string="", required=False, )


class check_vaucher(models.Model):
     _inherit = 'account.voucher'
     concepts_ids = fields.One2many(comodel_name="check.vaucher_do", inverse_name="concept_id", string="Conceptos", required=False, )



