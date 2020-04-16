from odoo import models, fields, api, _


class Specialization(models.Model):
	_name = 'enrsimply.specialization'
	_description = 'Specialization'

	name = fields.Char(string='Name', required=True)
	code = fields.Char(string='Code', required=False)
	taxonomy_code = fields.Char(string='Taxonony Code', required=False)

	#For Medicare
	# For Reference https://data.cms.gov/Medicare-Enrollment/CROSSWALK-MEDICARE-PROVIDER-SUPPLIER-to-HEALTHCARE/j75i-rw8y
	medicare_specialty_code = fields.Char(string='MEDICARE SPECIALTY CODE ', required=False)
	medicare_provider_code = fields.Char(string='MEDICARE PROVIDER/SUPPLIER TYPE DESCRIPTION', required=False)

class School(models.Model):
	_name = 'enrsimply.specialization'
	_description = 'Specialization'