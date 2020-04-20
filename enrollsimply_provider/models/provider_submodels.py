from odoo import models, fields, api, _
from datetime import datetime


class ATPArea(models.Model):
	_name = 'enrsimply.prov.atp'
	_description = 'Provider ATP Area'
	provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
	area_id = fields.Many2one('enrsimply.area.id',string='Area ID', required=True)
	location_id = fields.Many2one('enrsimply.location.id',string='Location ID', required=True)
    primary_area_id = fields.Many2one('enrsimply.area.id',string='Primary Area ID', required = True)
    expire_dt = fields.Date(string='Expiry Date')

	
class PIN(models.Model):
	_name = 'enrsimply.prov.pin'
	_description = 'Provider PIN'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    pin_type_id = fields.Many2one('enrsimply.pin_type.id',string='PIN Type ID', required='True')
    pin_number = fields.Char(string='PIN',10, required=True)
    pin_eff_dt = fields.Date(string='PIN Effective Date', required=True)
    pin_end_dt = fields.Date(string='PIN End Date', required=False)
    pin_status = fields.Selection(['Active','Inactive'],string='PIN Status',1, required=True)
    area_id = fields.Many2one('enrsimply.area.id',string='Area ID', required=False)
	location_id = fields.Many2one('enrsimply.location.id',string='Location ID', required=False)

class CCS(models.Model):
	_name = 'enrsimply.prov.ccs'
	_description = 'Provider CCS Paneling PIN'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    pin_type_id = fields.Many2one('enrsimply.pin_type.id',string='PIN Type ID', required='True')
    pin_number = fields.Char(string='PIN',10, required=True)
    pin_eff_dt = fields.Date(string='PIN Effective Date', required=True)
    pin_end_dt = fields.Date(string='PIN End Date', required=False)
    pin_status = fields.Selection(['Active','Inactive'],string='PIN Status',1, required=True)
    panel_taxonomy = fields.Many2one('enrsimply.specialization.code',string='Panel Taxonomy Code', required=False)

class Requirement_List(models.Model):
	_name = 'enrsimply.prov.requirements'
	_description = 'Requirements submitted by Provider'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    requirement_type_id = fields.Many2one('enrsimply.document_type.id',string='Document Type ID', required='True')
    submitted = fields.Boolean(string='Submit Status',required=True)
    submit_dt = fields.Date(string='Document Submit Date', required=False)

class ACA_Attestation(model.Models):
    _name = 'enrsimply.prov.aca_att'
    _description = 'Provider ACA Attestation Status'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    aca_status = fields.Char(string='ACA Status',1, required=True) #value=A for Active status
    pin_type_id = fields.Many2one('enrsimply.pin_type.id',string='PIN Type ID', required='True')
    eff_dt = fields.Date(string='Effective Date', required=True)
    end_dt = fields.Date(string='End Date', required=False)
    taxonomy_cd = fields.Many2one('enrsimply.specialization.code',string='Taxonomy Code', required=False)


class License(model.Models):
    _name = 'enrsimply.prov.aca'
    _description = 'Provider Licenses'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    license_type_id = fields.Many2one('enrsimply.license.id',string'License Type',required=True)
    license_number = fields.Char(string='License Number',10)
    eff_dt = fields.Date(string='Effective Date', required=True)
    exp_dt = fields.Date(string='Expiration Date', required=False)


class BoardCertification(model.Models):
    _name = 'enrsimply.prov.cert'
    _description = 'Provider Board Certification'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    certified_yr = fields.Integer(string='Certified Year')
    certified = fields.Char(10,string='License',required=True)
    specialty_id = fields.Many2one('enrsimply.specialization.code',string='Specialty', required=true)
    primary = fields.Boolean(required=False)
    recertified_year = fields.Integer(string='Recertified Year')
    pin_status = fields.Selection(['Active','Inactive'],string='Certification Status',1, required=True)
    
class Education(model.Models):
    _name = 'enrsimply.prov.educ'
    _description = 'Provider Education'
    provider_id = fields.Many2one('hr.employee.id',string='Provider ID', required=True)
    grad_year = fields.Integer(string='Graduation Year', required=True)
    school_type_id = fields.Many2one('hr.schooltype.id',string='School Type ID', required=True)
    university = fields.Char(string='University',100,required=True)
    state_id = fields.Many2one('res.country.state.id',string='School State',required=False)
    country_id = fields.Many2one('res.country.id',string='School Country',required=True)
    thru_dt = fields.Date(string='Thru Date')
    degree_earned = fields.Boolean(string='Degree Earned',required=True)