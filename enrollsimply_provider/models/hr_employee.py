# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import random

class HREmployee(models.AbstractModel):
	_inherit = 'hr.employee'

	# New Fields
	first_name = fields.Char(required=True)
	middle_name = fields.Char()
	last_name = fields.Char(required=True)
	employee_id = fields.Char(string='Employee ID')
	ss_number = fields.Char(string='SSN', required=True)
	driver_license_number = fields.Char(string="Driver's License")