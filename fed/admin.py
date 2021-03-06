from django.contrib import admin
from models import *
from sisme.contraparte.models import Informe

class BaseAdmin(admin.ModelAdmin):
    save_on_top = True    

class OrganizacionAdmin(BaseAdmin):
    list_display = ['nombre_corto', 'telefono_1', 'email', 'contacto']
    list_filter = ['user']
    search_fields = ['nombre', 'nombre_corto', 'email', 'telefono1', 'contacto', 'telefono_contacto']
    
    class Media:
        js = ('/files/js/tiny_mce/tiny_mce.js',
              '/files/js/tiny_mce/tconfig.js')
    
class TemaTrabajoInline(admin.TabularInline):
    filter_horizontal = ['municipio']    
    model = TemaTrabajo
    extra = 1
    
class PoblacionMetaDirectaInline(admin.TabularInline):        
    model = PoblacionMetaDirecta
    fields = ['grupo_etareo', 'hombres', 'alcanzada_hombre', 'mujeres', 'alcanzada_mujer']
    extra = 1
    
class PoblacionMetaIndirectaInline(admin.TabularInline):        
    model = PoblacionMetaIndirecta
    fields = ['grupo_etareo', 'hombres', 'alcanzada_hombre', 'mujeres', 'alcanzada_mujer']
    extra = 1

class ParticipacionComisionExtraAdmin(admin.TabularInline):
    model = ParticipacionComisionExtra
    filter_horizontal = ['municipios']
    extra = 1
    
class ProyectoAdmin(BaseAdmin):
    list_display = ['organizacion', 'codigo', 'nombre', 'fecha_inicio', 'fecha_fin']    
    list_filter = ['organizacion', 'modalidad']
    search_fields = ['nombre', 'organizacion__nombre', 'organizacion__nombre_corto']
    
    inlines = [TemaTrabajoInline, PoblacionMetaDirectaInline, 
               PoblacionMetaIndirectaInline, ParticipacionComisionExtraAdmin]   
    
admin.site.register(Donante)
admin.site.register(Tema)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Proyecto, ProyectoAdmin)

class ResultadoAdmin(BaseAdmin):
    search_fields = ['nombre_corto', 'descripcion']    

admin.site.register(Resultado, ResultadoAdmin)

