odoo.define('enrollsimply.MailBotService', function (require) {
    'use strict';

    var mailBotService = require('mail_bot.MailBotService');

    var core = require('web.core');
    var _t = core._t;

    mailBotService.include({

    	getPreviews: function (filter) {
	        if (!this.isRequestingForNativeNotifications()) {
	            return [];
	        }
	        if (filter && filter !== 'mailbox_inbox') {
	            return [];
	        }
	        var previews = [{
	            title: _t("EnrollSimplyBot has a request"),
	            imageSRC: "/mail/static/src/img/odoobot.png",
	            status: 'bot',
	            body:  _t("Enable desktop notifications to chat"),
	            id: 'request_notification',
	            unreadCounter: 1,
	        }];
	        return previews;
	    },

    });

});