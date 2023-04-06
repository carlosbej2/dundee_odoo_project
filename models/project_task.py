from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProjectTask(models.Model):
    _inherit = 'project.task'

    informe_tarea = fields.Html(
        string='Informe de la tarea',
    )
    worker_id = fields.Many2one(
        string='Trabajador',
        comodel_name='res.partner',
        ondelete='restrict',
    )
    requisitos_tarea = fields.Html(
        string='Requisitos de la tarea',
    )
    tarea_realizada = fields.Boolean(
        string='¿Tarea realizada?',
        store="True",
    )
    image_to_attach = fields.Binary(
        string='Adjunto',
        attachment=True,
    )

    @api.onchange('tarea_realizada')
    def _onchange_tarea_realizada(self):
        for record in self:
            if record.tarea_realizada:
                if not record.informe_tarea:
                    raise models.UserError(
                        _('Debe escribir un informe de la tarea antes de '
                          'marcarla como realizada!')
                    )
                else:
                    record.sudo().activity_schedule(
                       'mail.mail_activity_data_todo',
                        summary='Tarea realizada',
                        user_id=self.env.user.id,
                        note='Tarea realizada por el trabajador {}.'.format(
                            record.worker_id.name
                            ),
                    )
                    
    def action_task_2_done(self):
        if self.env.user.has_group('dundee.group_user_normal_rights'):
            raise UserError(_(
                'Disculpa %s, solo el ADMINISTRADOR puede pasar a finalizada la tarea' % self.env.user.name
                ))
        self.stage_id = self.env['project.task.type'].search(
            [('name', '=', 'Finalizado')], limit=1
        )
    
    def action_task_2_review(self):
        if not self.tarea_realizada:
            raise models.UserError(
                _('Debe marcar la tarea como realizada antes de '
                  'pasarla a revisión!')
            )
        else:
            admin = self.env['res.users'].search(
                [('name', '=', 'Carlos Bayón')],
            )
            self.stage_id = self.env['project.task.type'].search(
                [('name', '=', 'Para revisar')], limit=1
            )
            self.worker_id = admin
            self.user_id = admin

    @api.model
    def create(self, vals):
        if self.env.user.has_group('dundee.group_user_normal_rights'):
            raise UserError(_('Disculpa %s, no tiene permisos para crear TAREAS.' % self.env.user.name))
        return super(ProjectTask, self).create(vals)


