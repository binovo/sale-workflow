from odoo import api, SUPERUSER_ID


def assign_default_sale_type(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["sale.order"].search([])._compute_sale_type_id()
