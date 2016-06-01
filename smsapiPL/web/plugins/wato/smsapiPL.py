#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# smsapiPL
__author__ = 'awiamo'

register_notification_parameters("smsapiPL", Dictionary(
    optional_keys = ["url_prefix", "priority"],
    elements = [
        ("SMSAPIPL_KEY", TextAscii(
            title = _("API Key"),
            help = _("You need to provide a valid API key to be able to send sms notifications "
                     "using SMSAPI.PL."),
            size = 40,
            allow_empty = False,
            regex = "[a-zA-Z0-9]{10}",
        )),
	("SMSAPIPL_SMSTYPE", Alternative( title = _('<a target="_blank" href="https://www.smsapi.pl/faq#Wysyłka wiadomości-4">SMS Type</a>'), 
		elements = [
			FixedValue(value ='ECO', totext = "", title = _("(ECO)")),
			FixedValue(value ='2WAY', totext = "", title = _("(2WAY)")),
			TextAscii(
				title = _("(PRO) - set sender name:"), default_value = "$HOSTADDRESS$",
					    ),
			]
		)),
    ]
))


