# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Accounting Dashboard Odoo18',
    'version': '18.0.1.0.0',
    'category': 'Accounting ',
    'summary': """The Odoo Accounting Dashboard shows key financial metrics, 
     tracks payments, and visualizes income and expenses in one place.""",
    'description': """Accounting, Odoo Accounting Dashboard, 
     Accounting Dashboard V18, Account Dashboard, Dashboard, Invoice Dashboard, 
     Invoice Graph View, Odoo18""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://cybrosys.com',
    'depends': ['account', 'base_accounting_kit'],
    'data': [
        'views/account_move_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_accounting_dashboard/static/src/js/lib/chart/chart.min.js',
            'odoo_accounting_dashboard/static/src/xml/accounting_dashboard.xml',
            'odoo_accounting_dashboard/static/src/js/accounting_dashboard.js',
        ]
    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': False,
    'application': False,
}
