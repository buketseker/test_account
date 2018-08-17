# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MechSoft - Turkish COA Plan',
    'version': '1.0',
    'category': 'Localization',
    'description': """
MechSoft tarafından geliştirilen Türkiye Tek Düzen Hesap Planı
    """,
    'author': 'MechSoft',
    'maintainer':'MechSoft',
    'website':'https://www.mechsoft.com.tr',
    'depends': [
        'account', 'account_accountant'
    ],
    'data': [
        'data/l10n_tr_chart_data.xml',
        'data/account_data.xml',
        'data/account_tax_template_data.xml',
        'data/account_chart_template_data.yml',
    ],
}
