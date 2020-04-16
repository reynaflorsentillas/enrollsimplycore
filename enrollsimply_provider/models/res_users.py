# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResUsers(models.Model):
	_inherit = 'res.users'
	
	odoobot_state = fields.Selection(
		[
			('not_initialized', 'Not initialized'),
			('onboarding_emoji', 'Onboarding emoji'),
			('onboarding_attachement', 'Onboarding attachement'),
			('onboarding_command', 'Onboarding command'),
			('onboarding_ping', 'Onboarding ping'),
			('idle', 'Idle'),
			('disabled', 'Disabled'),
		], string="EnrollSimplyBot Status")  # keep track of the state: correspond to the code of the last message sent
