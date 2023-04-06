from odoo import _, api, fields, models


class ProjectTaskCreation(models.TransientModel):
    _name = 'project.task.creation'
    _description = 'Wizard para la creación de tareas'

    name = fields.Char(
        string='Título de la tarea',
    )
    description = fields.Html(
        string='Descripción de la tarea',
    )  
    worker_id = fields.Many2one(
        string='Trabajador',
        comodel_name='res.partner',
        ondelete='restrict',
    )
    project_id = fields.Many2one(
        string='Proyecto',
        comodel_name='project.project',
        ondelete='restrict',
    )
    stage_ids_from_project = fields.Many2one(
        string='Fase',
        comodel_name='project.task.type',
        ondelete='restrict',
    )

    def create_task(self):
        self.ensure_one()
        task = self.env['project.task'].create({
            'name': self.name,
            'project_id': self.project_id.id,
            'worker_id': self.worker_id.id,
            'requisitos_tarea': self.description,
            'user_id': self.worker_id.user_id.id,
            'kanban_state': 'done',
        })
        return {
            'name': _('Tarea creada!'),
            'type': 'ir.actions.act_window',
            'res_model': 'project.task',
            'res_id': task.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
        }
