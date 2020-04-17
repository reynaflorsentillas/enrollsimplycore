# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class BasicTransientModels(models.AbstractModel):
	_name = 'basic.model'
	name = fields.Char(string='Name', required=True)
	code = fields.Char(string='Code', required=False)



class Specialization(models.Model):
	_name = 'enrsimply.specialization'
	_description = 'Specialization'
	_inherit = 'basic.model'

	taxonomy_code = fields.Char(string='Taxonony Code', required=False)

	#For Medicare
	# For Reference https://data.cms.gov/Medicare-Enrollment/CROSSWALK-MEDICARE-PROVIDER-SUPPLIER-to-HEALTHCARE/j75i-rw8y
	medicare_specialty_code = fields.Char(string='MEDICARE SPECIALTY CODE ', required=False)
	medicare_provider_code = fields.Char(string='MEDICARE PROVIDER/SUPPLIER TYPE DESCRIPTION', required=False)

class SchoolType(models.Model):
	_name = 'hr.schooltype'
	_description = 'School Type'
	_inherit = 'basic.model'

class ActionReason(models.Model): 
	_name = 'enrsimply.pin.type'
	_description = 'Pin Type'
	_inherit = 'basic.model'


class Licenses(models.Model): 
	_name = 'enrsimply.licenses'
	_description = 'Licenses Type'
	_inherit = 'basic.model'

class PinType(models.Model): 
	_name = 'enrsimply.pin.type'
	_description = 'Pin Type'
	_inherit = 'basic.model'


class Areas(models.Model): 
	_name = 'enrsimply.areas'
	_description = 'Areas'
	_inherit = 'basic.model'

class Locations(models.Model): 
	_name = 'enrsimply.locations'
	_description = 'Locations'
	_inherit = 'basic.model'

	area_ids = fields.Many2many('enrsimply.areas', 'area_location_rel', 'area_id', 'location_id')


class PinTransactionSatus(models.Model): 
	_name = 'enrsimply.pin.trans_status'
	_description = 'Pin Transaction Type'
	_inherit = 'basic.model'


class Action(models.Model): 
	_name = 'enrsimply.pin.action'
	_description = 'Action'
	_inherit = 'basic.model'

class ActionReason(models.Model): 
	_name = 'enrsimply.pin.action_reason'
	_description = 'Action Reason'
	_inherit = 'basic.model'

class DocumentType(models.Model): 
	_name = 'enrsimply.document_type'
	_description = 'Action Reason'
	_inherit = 'basic.model'
