# -*- coding: utf-8 -*-

{
    'name': 'Vipdoo - Account Date Full Payment',
    'version': '16.0',
    'summary': 'Vipdoo - Account Date Full Payment',
    'description': """Provides The Date Of The Full Payment Abd Store It Without Change""",
    "sequence": 100,
    'category': 'Accounting',
    'author': 'Vipdoo',
    'maintainer': 'Vipdoo',
    'website': 'https://vipdoo.com/',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move.xml',
    ],
    'demo': [],
    'qweb': [],

    'images': ['static/description/icon.jpeg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
