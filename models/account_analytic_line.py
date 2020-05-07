from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket_id',
    )
    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
        related='ticket_id.project_id',
    )
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
        related='ticket_id.task_id',
    )
    account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analityc Account',
        related='ticket_id.account_id',
        store="True",
    )