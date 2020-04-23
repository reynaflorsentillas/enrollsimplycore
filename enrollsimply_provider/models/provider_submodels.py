from odoo import models, fields, api, _
from datetime import datetime

STATUS = [('active', 'Active'), ('inactive', 'Inactive')]
STATUS_PIN = [('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending')]


class ProviderAdress(models.Model):
    _name = 'enrsimply.prov.address'
    _description = 'Provider Address'

    provider_id = fields.Many2one('hr.employee',string='Provider ID')
    res_partner_id = fields.Many2one('res.partner', string='Partner')
    address_type_id = fields.Many2one('enrsimply.addresstype', string='Type')

    address_1 = fields.Char(string='Address 1')
    address_2 = fields.Char(string='Address 2')
    address_3 = fields.Char(string='Address 3')
    city = fields.Char(string='City')
    zip = fields.Char(string='Zip')
    state_id = fields.Many2one('res.country.state',string='State')
    country_id = fields.Many2one('res.country', string='Country')    
    default_address = fields.Boolean('Default Address')


    def getValues(self, dict_key=False, dict=False):
        if dict_key in dict:
            return dict[dict_key]
        return False

    @api.model
    def create(self, vals):
        address_2 = self.getValues('address_2', vals) or ""
        address_3 = self.getValues('address_3', vals) or ""
        street2 = address_2 + ' '  + address_3

        partner_model = self.env['res.partner']
        provider_obj = self.env['hr.employee'].search([('id', '=', vals['provider_id'])])

        #Create Partner
        result_partner = partner_model.create({
                'type': 'contact',
                'name': provider_obj.name,
                'street': self.getValues('address_1', vals),
                'street2': street2,
                'city': self.getValues('city', vals),
                'zip': self.getValues('zip', vals),
                'state_id': self.getValues('state_id', vals),
                'country_id': self.getValues('country_id', vals),})

        vals['res_partner_id'] = result_partner and result_partner.id or False
        res = super(ProviderAdress, self).create(vals)
        return res

    def write(self,vals):
        for rec in self:
            address_2 = ""
            address_3 = ""

            partner_list = {}
            if 'address_1' in vals:
                partner_list['street'] = vals['address_1']

            if 'address_2' in vals:
                address_2 = vals['address_2']
            else:
                address_2 = rec.address_2

            if 'address_3' in vals:
                address_2 = vals['address_3']
            else:
                address_2 = rec.address_3

            if address_2 or address_3:
                partner_list['street2'] = address_2 + ' ' + address_3

            if 'city' in vals:
                partner_list['city'] = vals['city']
            if 'zip' in vals:
                partner_list['zip'] = vals['zip']
            if 'state_id' in vals:
                partner_list['state_id'] = vals['state_id']
            if 'country_id' in vals:
                partner_list['country_id'] = vals['country_id']
            partner_id = rec.res_partner_id.write(partner_list)

        res = super(ProviderAdress, self).write(vals)
        return res


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