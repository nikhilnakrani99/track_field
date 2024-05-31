# -*- coding: utf-8 -*-
#############################################################################
#
#   
#
#    Copyright (C) 2024-TODAY 
#    Author: Nikhil Nakrani
#
#############################################################################

from odoo import _, api, fields, models


class IrModel(models.Model):
    _inherit = 'ir.model'

    is_tracking_field = fields.Boolean(string="Tracking all Fields", default=False)


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.model
    def _track_get_fields(self):
        super(MailThread, self)._track_get_fields()
        tracked_fields = []
        Model = self.env['ir.model'].sudo()
        if Model.search([('model', '=', str(self._name))]).is_tracking_field:
            for name, field in self._fields.items():
                if name not in ['write_date', '__last_update']:
                    tracked_fields.append(name)
        if tracked_fields:
            return set(self.fields_get(tracked_fields))
        else:
            model_fields = {
                name
                for name, field in self._fields.items()
                if getattr(field, 'tracking', None) or getattr(field, 'track_visibility', None)
            }
            return model_fields and set(self.fields_get(model_fields))