# -*- coding: utf-8 -*-

from odoo import api, fields, models
import logging

import zeep

class Partner(models.Model):
    _inherit = "res.partner"

    def buscar_datos_sat(self):
        wsdl = 'https://www.ingface.net/ServiciosIngface/ingfaceWsServices?wsdl'
        client = zeep.Client(wsdl=wsdl)

        resultado = client.service.nitContribuyentes(usuario='CONSUMO_NIT', clave='58B45D8740C791420C53A49FFC924A1B58B45D8740C791420C53A49FFC924A1B', nit=self.vat.replace('-',''))
        self.nombre_facturacion_fel = resultado.nombre

        return True
