from odoo import _, api, models
from odoo.exceptions import ValidationError


class PosConfig(models.Model):
    _inherit = "pos.config"

    @api.constrains(
        "pricelist_id",
        "use_pricelist",
        "available_pricelist_ids",
        "journal_id",
        "invoice_journal_id",
        "payment_method_ids",
    )
    def _check_currencies(self):
        try:
            super()._check_currencies()
        except ValidationError as err:
            msg_to_catch = _(
                "All available pricelists must be in the same currency as the company or"
                " as the Sales Journal set on this point of sale if you use"
                " the Accounting application."
            )
            if err.args[0] != msg_to_catch:
                raise
