from odoo import fields, models


class Item(models.Model):
    _name = "fridge_rangers.item"
    _description = "Food items left on the fridge"

    name = fields.Char(required=True)
    description = fields.Text()
    owner_id = fields.Many2one(
        "res.users", required=True, default=lambda self: self.env.user
    )
    added_date = fields.Date(default=fields.Date.today())
    expiry_date = fields.Date()
    state = fields.Selection(
        [("in_fridge", "In fridge"), ("eaten", "Eaten"), ("expired", "Expired")],
        required=True,
        default="in_fridge",
    )
