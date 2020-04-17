from odoo import models, fields, api, _
from datetime import datetime


class ATPArea(models.Model):
	_name = 'enrsimply.prov.atp'
	_description = 'Provider ATP Area'
	provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
	area_id = fields.Many2one('enrsimply.area.id',string='Area ID', required=True)
	location_id = fields.Many2one('enrsimply.location.id',string='Location ID', required=True)
    primary_area_id = fields.Many2one('enrsimply.area.id',string='Primary Area ID', required = True)
    expire_dt = fields.Date('Expiry Date')

	
class PIN(models.Model):
	_name = 'enrsimply.prov.pin'
	_description = 'Provider PIN'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    pin_type_id = fields.Many2one('enrsimply.pin_type.id',string='PIN Type ID', required='True')
    pin_number = fields.Char('PIN',10, required=True)
    pin_eff_dt = fields.Date('PIN Effective Date', required=True)
    pin_end_dt = fields.Date('PIN End Date', required=False)
    pin_status = fields.Char('PIN Status',1, required=True) #value=A for Active status
    area_id = fields.Many2one('enrsimply.area.id',string='Area ID', required=False)
	location_id = fields.Many2one('enrsimply.location.id',string='Location ID', required=False)

class CCS(models.Model):
	_name = 'enrsimply.prov.ccs'
	_description = 'Provider CCS Paneling PIN'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    pin_type_id = fields.Many2one('enrsimply.pin_type.id',string='PIN Type ID', required='True')
    pin_number = fields.Char('PIN',10, required=True)
    pin_eff_dt = fields.Date('PIN Effective Date', required=True)
    pin_end_dt = fields.Date('PIN End Date', required=False)
    pin_status = fields.Char('PIN Status',1, required=True) #value=A for Active status
    panel_taxonomy = fields.Many2one('enrsimply.specialization.code','Panel Taxonomy Code', required=False)

class Requirement_List(models.Model):
	_name = 'enrsimply.prov.requirements'
	_description = 'Requirements submitted by Provider'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    requirement_type_id = fields.Many2one('enrsimply.document_type.id',string='Document Type ID', required='True')
    submitted = fields.Boolean('Submit Status',required=True)
    submit_dt = fields.Date('Document Submit Date', required=False)

class ACA_Attestation(model.Models):
    _name = 'enrsimply.prov.aca_att'
    _description = 'Provider ACA Attestation Status'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    aca_status = fields.Char('ACA Status',1, required=True) #value=A for Active status

class License(model.Models):
    _name = 'enrsimply.prov.aca'
    _description = 'Provider Licenses'

class BoardCertification(model.Models):
    _name = 'enrsimply.prov.cert'
    _description = 'Provider Board Certification'

class Education(model.Models):
    _name = 'enrsimply.prov.educ'
    _description = 'Provider Education'
c