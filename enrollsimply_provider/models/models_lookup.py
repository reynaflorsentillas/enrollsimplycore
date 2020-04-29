# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class BasicTransientModels(models.AbstractModel):
	_name = 'basic.model'
	_rec_name = 'complete_name'
	_order = 'complete_name'

	name = fields.Char(string='Name', required=True)
	code = fields.Char(string='Code', required=False)
	complete_name = fields.Char('Complete Name', compute='_compute_complete_name',store=True)

	@api.depends('name', 'code')
	def _compute_complete_name(self):			
		for rec in self:
			code =""
			name =""
			if rec.code:
				code = "[" + rec.code + "]"
			name = rec.name
			rec.complete_name = code +" "+ name


class AddressType(models.Model):
	_name = 'enrsimply.addresstype'
	_description = 'Address Type'
	_inherit = 'basic.model'
	_order = 'code'

class Specialization(models.Model):
	_name = 'enrsimply.specialization'
	_description = 'Specialization'
	_inherit = 'basic.model'

	taxonomy_code = fields.Char(string='Taxonomy Code', required=False)
	taxonomy_id = fields.Many2one('enrsimply.taxonomy', string='Taxonomy')


class Taxonomy(models.Model):
	_name = 'enrsimply.taxonomy'
	_description = 'Taxonomy'
	_inherit = 'basic.model'



class SpecializationMedicare(models.Model):
	_name = 'enrsimply.spec.medcare'
	_description = 'Medicare Code'
	_inherit = 'basic.model'

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

	partner_id = fields.Many2one('res.partner', 'Address')

class Locations(models.Model): 
	_name = 'enrsimply.locations'
	_description = 'Locations'
	_inherit = 'basic.model'

	area_ids = fields.Many2many('enrsimply.areas', 'area_location_rel', 'area_id', 'location_id')
	partner_id = fields.Many2one('res.partner', 'Address')


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
	_description = 'Document Type'
	_inherit = 'basic.model'

class DocumentTemplateList(models.Model):
	_name = 'enrsimply.doc.temp.list'
	_description = 'Document Template List'
	_inherit = 'basic.model'

	document_id = fields.Many2one('enrsimply.document_type', string="Position")
	job_id = fields.Many2one('hr.job', string="Position")
