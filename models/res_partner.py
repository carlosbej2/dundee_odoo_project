from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def write(self, vals):
        if self.env.user.has_group('dundee.group_user_normal_rights'):
            raise UserError(_('Disculpa %s, no tiene permisos para modificar CONTACTOS.' % self.env.user.name))
        return super(ResPartner, self).write(vals)

    @api.model
    def create(self, vals):
        if self.env.user.has_group('dundee.group_user_normal_rights'):
            raise UserError(_('Disculpa %s, no tiene permisos para crear CONTACTOS.' % self.env.user.name))
        return super(ResPartner, self).create(vals)
