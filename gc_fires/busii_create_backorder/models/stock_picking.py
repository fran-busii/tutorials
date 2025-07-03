from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError
_logger = logging.getLogger(__name__)

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    def action_make_backorder(self):
        """Handles Create Backorder button action."""
        if self.state in ['draft', 'cancel']:
                raise UserError(_("The delivery order must not be in draft or cancel state."))
        if 'WH/OUT/' in self.name and self.state not in ['draft', 'cancel']:
            _logger.info(f"Delivery order  we are looking at: {self.name} with backorder_id: {self.backorder_id.name}")
            if len(self.move_ids_without_package) != 1:
                raise UserError(_("The delivery order must have exactly one line."))
                
            if self.backorder_id.name == False:
                _logger.info(f"Delivery order {self.name} does not have a backorder_id")
                self.write({
                'backorder_id': self.id,
                })