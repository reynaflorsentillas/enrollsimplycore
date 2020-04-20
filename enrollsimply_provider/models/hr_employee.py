# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import random

class HREmployee(models.AbstractModel):
	_inherit = 'hr.employee'
	_description = "Provider"

	# Override
	name = fields.Char(string="Provider Name")

	# New Fields
	first_name = fields.Char(required=True)
	middle_name = fields.Char()
	last_name = fields.Char(required=True)
	employee_id = fields.Char(string='Employee ID')
	ss_number = fields.Char(string='SSN', required=True, groups="hr.group_hr_user")
	driver_license_number = fields.Char(string="Driver's License", required=True, groups="hr.group_hr_user")
	driver_license_state_id = fields.Many2one('res.country.state',string="Driver's License State", required=True, groups="hr.group_hr_user")
	birth_state_id = fields.Many2one('res.country.state', string='State of Birth', groups="hr.group_hr_user")
	medical_license_number = fields.Char(string='License Number', required=True, groups="hr.group_hr_user")
	medical_npi_number = fields.Char(string='NPI Number', groups="hr.group_hr_user")
	aca_key = fields.Char(string='ACA Key', groups="hr.group_hr_user")
	aca_site_email = fields.Char(groups="hr.group_hr_user")
	grp_npi_number = fields.Char(string='Group NPI#', required=True, groups="hr.group_hr_user")
	grp_medicare_number = fields.Char(string='Group Medicare#', required=True, groups="hr.group_hr_user")
	grp_medical_number = fields.Char(string='Group Medical#', required=True, groups="hr.group_hr_user")
	notes = fields.Text()

	@api.onchange('first_name','middle_name','last_name')
	def _compute_name(self):
		self.name = "%s %s %s" % (self.first_name or '', self.middle_name or '', self.last_name or '')