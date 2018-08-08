# -*- coding: utf-8 -*-
#
#
#    Author: Valentin GRIMAUD <ljf+odoo-base-location@reflexlibre.net> 
#    Contributor: Pedro Manuel Baeza <pedro.baeza@serviciosbaeza.com>
#                 Ignacio Ibeas <ignacio@acysos.com>
#                 Alejandro Santana <alejandrosantana@anubia.es>
#                 Nicolas Bessi. Copyright Camptocamp SA   
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
#
from openerp import models, fields, api


class ResLead(models.Model):
    _inherit = 'crm.lead'
    zip_id = fields.Many2one('res.better.zip', 'City/Location')
    zip2_id = fields.Many2one('res.better.zip', 'City/Location')

    @api.one
    @api.onchange('zip_id')
    def onchange_zip_id(self):
        if self.zip_id:
            self.zip = self.zip_id.name
            self.city = self.zip_id.city
            self.state_id = self.zip_id.state_id
            self.country_id = self.zip_id.country_id
    
    @api.one
    @api.onchange('zip2_id')
    def onchange_zip2_id(self):
        if self.zip2_id:
            self.x_zip = self.zip2_id.name
            self.x_city = self.zip2_id.city
