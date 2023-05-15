from odoo import models, fields
class todo_tasca(models.Model):
 _name = 'todo.tasca'
 titol = fields.Char('Títol', required=True)
 data_final = fields.Date('Data final')