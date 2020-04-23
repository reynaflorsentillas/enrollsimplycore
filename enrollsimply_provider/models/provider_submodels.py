from odoo import models, fields, api, _
from datetime import datetime

STATUS = [('active', 'Active'), ('inactive', 'Inactive')]
STATUS_PIN = [('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending')]

class ATPArea(models.Model):
    _name = 'enrsimply.prov.atp'
    _description = 'Provider ATP Area'
    provider_id = fields.Many2one('hr.employee',string='Provider ID')
    area_id = fields.Many2one('enrsimply.areas',string='Area') #, required=True)
    location_id = fields.Many2one('enrsimply.locations',string='Location') #, required=True)
    primary_area_id = fields.Many2one('enrsimply.areas',string='Primary Area', required = True)
    expire_dt = fields.Date(string='Expiry Date')

	
class PIN(models.Model):
    _name = 'enrsimply.prov.pin'
    _description = 'Provider PIN'
    provider_id = fields.Many2one('hr.employee',string='Provider ID')
    pin_type_id = fields.Many2one('enrsimply.pin.type',string='PIN Type') #, required=True)
    pin_number = fields.Char(string='PIN', required=False)
    pin_eff_dt = fields.Date(string='Effective Date', required=False)
    pin_end_dt = fields.Date(string='End Date', required=False)
    pin_status = fields.Selection(STATUS_PIN, string='PIN Status', required=False, default="pending")
    area_id = fields.Many2one('enrsimply.areas',string='Area', required=False)
    location_id = fields.Many2one('enrsimply.locations',string='Location', required=False)

    trans_date = fields.Date(string='Transaction Date', required=False)#, default=fields.Date)


class CCS(models.Model):
    _name = 'enrsimply.prov.ccs'
    _description = 'Provider CCS Paneling PIN'
    provider_id = fields.Many2one('hr.employee',string='Provider ID')
    pin_type_id = fields.Many2one('enrsimply.pin.type',string='PIN Type') #, required=True)
    pin_number = fields.Char(string='PIN') #, required=True)
    pin_eff_dt = fields.Date(string='PIN Effective Date') #, required=True)
    pin_end_dt = fields.Date(string='PIN End Date', required=False)
    pin_status = fields.Selection(STATUS,string='PIN Status') #, required=True)
    panel_taxonomy = fields.Many2one('enrsimply.specialization',string='Panel Taxonomy Code', required=False)

class Requirement_List(models.Model):
    _name = 'enrsimply.prov.requirements'
    _description = 'Requirements submitted by Provider'
    provider_id = fields.Many2one('hr.employee',string='Provider ID') #, required=True)
    requirement_type_id = fields.Many2one('enrsimply.document_type',string='Document Type ID') #, required=True)
    submitted = fields.Boolean(string='Submit Status') #, required=True)
    submit_dt = fields.Date(string='Document Submit Date', required=False)

class ACA_Attestation(models.Model):
    _name = 'enrsimply.prov.aca_att'
    _description = 'Provider ACA Attestation Status'
    provider_id = fields.Many2one('hr.employee',string='Provider ID') #, required=True)
    aca_status = fields.Selection(STATUS, string='ACA Status') #, required=True) #value=A for Active status
    pin_type_id = fields.Many2one('enrsimply.pin.type',string='PIN Type') #, required=True)
    eff_dt = fields.Date(string='Effective Date') #, required=True)
    end_dt = fields.Date(string='End Date', required=False)
    taxonomy_cd = fields.Many2one('enrsimply.specialization',string='Taxonomy Code', required=False)


# class License(models.Model):
#     _name = 'enrsimply.prov.aca'
#     _description = 'Provider Licenses'
#     provider_id = fields.Many2one('hr.employee',string='Provider ID') #, required=True)
#     license_type_id = fields.Many2one('enrsimply.license',string='License Type') #, required=True)
#     license_number = fields.Char(string='License Number')
#     eff_dt = fields.Date(string='Effective Date') #, required=True)
#     exp_dt = fields.Date(string='Expiration Date', required=False)


class Licenses(models.Model):
    _name = 'enrsimply.prov.licenses'
    _description = 'Provider Licenses'
    provider_id = fields.Many2one('hr.employee', string='Provider ID')
    license_type_id = fields.Many2one('enrsimply.licenses', string='License Type') #, required=True)
    license_number = fields.Char(string='License Number') #, required=True)
    effctive_date  = fields.Date(string='Effective Date') #, required=True)
    expry_date = fields.Date(string='Expiration Date')
    active = fields.Boolean('Active', default=True)


class BoardCertification(models.Model):
    _name = 'enrsimply.prov.cert'
    _description = 'Provider Board Certification'
    provider_id = fields.Many2one('hr.employee',string='Provider ID') #, required=True)
    certified_yr = fields.Integer(string='Certified Year')
    certified = fields.Char(string='License') #, required=True)
    specialty_id = fields.Many2one('enrsimply.specialization',string='Specialty') #, required=True)
    primary = fields.Boolean(required=False)
    recertified_year = fields.Integer(string='Recertified Year')
    pin_status = fields.Selection(STATUS,string='Certification Status') #, required=True)
    
class Education(models.Model):
    _name = 'enrsimply.prov.educ'
    _description = 'Provider Education'
    provider_id = fields.Many2one('hr.employee',string='Provider ID') #, required=True)
    grad_year = fields.Integer(string='Graduation Year') #, required=True)
    school_type_id = fields.Many2one('hr.schooltype',string='School Type ID') #, required=True)
    university = fields.Char(string='University') #, required=True)
    state_id = fields.Many2one('res.country.state',string='School State',required=False)
    country_id = fields.Many2one('res.country',string='School Country') #, required=True)
    thru_dt = fields.Date(string='Thru Date')
    degree_earned = fields.Boolean(string='Degree Earned') #, required=True)