# -*- coding: utf-8 -*-
#############################################################################
#
#   
#
#    Copyright (C) 2024-TODAY 
#    Author: Nikhil Nakrani
#
#############################################################################
{
    'name': 'Enable Tracking All Fields',
    'summary': 'Enable Tracking for all the Fields of model',
    'version': '15.0',
    'author': 'Nikhil Nakrani',
    'category': 'Base',
    'license': 'LGPL-3',
    'depends': [
        'mail',
    ],
    'data': [
        'views/ir_model_inherit_view.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
