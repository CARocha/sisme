# -*- coding: UTF-8 -*-
from django import forms
from django.forms import ModelForm
from sisme.fed.models import *
from sisme.fed.forms import ANIOS
import datetime


MONTH_CHOICES = (('', 'Mes'),
                 (1, 'Enero'), (2, 'Febrero'),
                 (3, 'Marzo'), (4, 'Abril'),
                 (5, 'Mayo'), (6, 'Junio'),
                 (7, 'Julio'), (8, 'Agosto'),
                 (9, 'Septiembre'), (10, 'Octubre'),
                 (11, 'Noviembre'), (12, 'Diciembre'))

ANIOS_CHOICE = (('', u'Año'), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013),)

class InfluenciaForm(forms.Form):
    modalidad = forms.MultipleChoiceField(choices=MODALIDAD_CHOICE, label='Modalidad de apoyo', required=False)
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizacion.objects.all(), label='Organizaciones', required=False)
    temas = forms.ModelMultipleChoiceField(queryset=Tema.objects.all(), label='Temas', required=False)
    resultado = forms.ModelMultipleChoiceField(queryset=Resultado.objects.all().exclude(id=7), label='Resultados', required=False)
    meses = forms.MultipleChoiceField(choices=MONTH_CHOICES, error_messages={'required': 'Seleccione al menos un mes'})    
    anio = forms.ChoiceField(choices=ANIOS_CHOICE, error_messages={'required': u'Seleccione un año'})