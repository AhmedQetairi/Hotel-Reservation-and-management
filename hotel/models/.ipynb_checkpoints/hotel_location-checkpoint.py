# See LICENSE file for full copyright and licensing details.
import logging
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as dt

_logger = logging.getLogger(__name__)
try:
    import pytz
except (ImportError, IOError) as err:
    _logger.debug(err)


class HotelLocation(models.Model):

    _name = "hotel.location"
    _description = "Hotel Location"
     
    

    name = fields.Char("Location")
    
      
    
class HotelCity(models.Model):

    _name = "hotel.city"
    _description = "Hotel City"

    name = fields.Char("City")

    

class HotelDistrict(models.Model):

    _name = "hotel.district"
    _description = "Hotel District"

    name = fields.Char("District")