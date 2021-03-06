# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi. Copyright Camptocamp SA
#    Contributor: Pedro Manuel Baeza <pedro.baeza@serviciosbaeza.com>
#                 Ignacio Ibeas <ignacio@acysos.com>
#                 Alejandro Santana <alejandrosantana@anubia.es>
#                 Valentin GRIMAUD <ljf+odoo-base-location@reflexlibre.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Location management for lead (aka Better ZIP)',
    'version': '9.0.1.1.0',
    'depends': ['base'],
    'author': "ReflexLibre,"
              "Camptocamp,"
              "ACYSOS S.L.,"
              "Alejandro Santana,"
              "Tecnativa,"
              "Odoo Community Association (OCA)",
    'license': "AGPL-3",
    'contributors': [
        'Nicolas Bessi <nicolas.bessi@camptocamp.com>',
        'Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>',
        'Ignacio Ibeas (Acysos S.L.)',
        'Alejandro Santana <alejandrosantana@anubia.es>',
        'Sandy Carter <sandy.carter@savoirfairelinux.com>',
        'Yannick Vaucher <yannick.vaucher@camptocamp.com>',
        'Valentin GRIMAUD <ljf+odoo-base-location@reflexlibre.net>',
    ],
    'summary': '''Enhanced zip/npa management system for lead''',
    'website': 'https://reflexlibre.net',
    'data': ['views/better_zip_view.xml',
             'views/state_view.xml',
             'views/res_country_view.xml',
             'views/company_view.xml',
             'views/partner_view.xml',
             'views/lead_view.xml',
             'security/ir.model.access.csv'],
    'demo': [
        'demo/better_zip.xml',
    ],
    'installable': True,
    'auto_install': False,
}
