# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import random

class HREmployee(models.AbstractModel):
	_inherit = 'hr.employee'
	_description = "Provider"

	# Override
	# name = fields.Char(string="Provider Name")

	# New Fields


	@api.model
	def _defaultReqList(self):
		all_doc_list =[]
		document_obj = self.env['enrsimply.document_type'].search([])
		for document in document_obj:
			doc_dict = {'requirement_type_id': document.id, 'submitted':False, 'submit_dt':False}
			doc_list =(0 , 0, doc_dict)
			all_doc_list.append(doc_list)
		return all_doc_list

	@api.model
	def _defaultAddress(self):
		all_doc_list =[]
		adtype_obj = self.env['enrsimply.addresstype'].search([])
		for adtype in adtype_obj:
			adtype_dict = {
						  	'address_type_id':adtype.id, 
						  	'address_1':False,
						  	'address_2':False,
						  	'address_3':False,
						  	'city':False,
						  	'zip':False,
						  	'state_id':False,
						  	'country_id':False,
						  	'default_address':False,}
			adtype_list =(0 , 0, adtype_dict)
			all_doc_list.append(adtype_list)

		return all_doc_list



	type = fields.Selection([
		('regular', 'Regular'),
		('provider', 'Healthcare Provider'),
	], string='Employee Type', default='regular')
	first_name = fields.Char(required=True)
	middle_name = fields.Char()
	last_name = fields.Char(required=True)
	employee_id = fields.Char(string='Employee ID')
	ss_number = fields.Char(string='SSN', required=True, groups="hr.group_hr_user")
	driver_license_number = fields.Char(string="Driver's License", required=True, groups="hr.group_hr_user")
	driver_license_state_id = fields.Many2one('res.country.state',string="Driver's License State", required=True, groups="hr.group_hr_user")
	birth_state_id = fields.Many2one('res.country.state', string='State of Birth', groups="hr.group_hr_user")
	medical_license_number = fields.Char(string='License Number', groups="hr.group_hr_user")
	medical_npi_number = fields.Char(string='NPI Number', groups="hr.group_hr_user")
	aca_key = fields.Char(string='ACA Key', groups="hr.group_hr_user")
	aca_site_email = fields.Char(groups="hr.group_hr_user")
	grp_npi_number = fields.Char(string='Group NPI#', groups="hr.group_hr_user")
	grp_medicare_number = fields.Char(string='Group Medicare#', groups="hr.group_hr_user")
	grp_medical_number = fields.Char(string='Group Medical#', groups="hr.group_hr_user")
	notes = fields.Text()

	# Related Fields
	specialization_id = fields.Many2one('enrsimply.specialization', string='Specialization')
	atp_area_ids = fields.One2many('enrsimply.prov.atp', 'provider_id', string='Provider ATP Area')

	pin_ids = fields.One2many('enrsimply.prov.pin', 'provider_id', string='Pending Provider PIN', domain=[('pin_status', '=', 'pending')])
	pin_inactive_ids = fields.One2many('enrsimply.prov.pin', 'provider_id', domain=[('pin_status', '=', 'inactive')])
	pin_active_ids = fields.One2many('enrsimply.prov.pin', 'provider_id', domain=[('pin_status', '=', 'active')])

	ccs_pin_ids = fields.One2many('enrsimply.prov.ccs', 'provider_id', string='Provider CCS Paneling PIN')
	requirement_list_ids = fields.One2many('enrsimply.prov.requirements', 'provider_id', string='Requirements submitted by Provider', default=_defaultReqList)

	aca_attestation_stat_ids = fields.One2many('enrsimply.prov.aca_att', 'provider_id', string='Provider ACA Attestation Status')

	
	license_ids = fields.One2many('enrsimply.prov.licenses', 'provider_id', string='Provider Licenses')
	address_ids = fields.One2many('enrsimply.prov.address', 'provider_id', string='Provider Address', default=_defaultAddress)
	education_ids = fields.One2many('enrsimply.prov.educ', 'provider_id', string='Provider Education')
	board_certif_ids = fields.One2many('enrsimply.prov.cert', 'provider_id', string='Provider Certification')

	@api.onchange('first_name','middle_name','last_name')
	def _compute_name(self):
		self.name = "%s %s %s" % (self.first_name or '', self.middle_name or '', self.last_name or '')