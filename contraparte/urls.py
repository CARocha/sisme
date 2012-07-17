from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('sisme.contraparte.views',
    (r'^indicadores/$', 'indicadores'),
    
    #------------- Indicadores de resultado 1.1 ------------------------    
    (r'^impulsando-politicas-publicas/$', 'impulsando_politicas_publicas'),    
    
    #------------- Indicadores de resultado 1.2 ------------------------    
    (r'^demandando-justicia/$', 'demandando_justicia'),
    
    #------------- Indicadores de resultado 2.1 ------------------------
    (r'^involucramiento-poblacion/$', 'involucramiento_poblacion'),
    (r'^acciones-reflexion/$', 'acciones_reflexion'),
    
    #------------- indicadores resultado 2.2 -------------------------
    (r'^prevencion-violencia/$', 'prevencion_violencia'),
    
    #------------- indicadores resultado 2.3 -------------------------
    (r'^acceso-a-servicios/$', 'acceso_a_servicios'),
    
    #------------- indicadores resultado 3.1 -------------------------
    (r'^capacidad-tecnica/$', 'capacidad_tecnica'),
    
    #Area de influencia
    (r'^influencia/$', 'influencia'),
    (r'^organizacion/(?P<id>\d+)/$', 'organizacion_detail'),

    #------------------participacion generos por organizacion --------
    (r'^participacion_mujeres/$', 'mujeres_pvbg'),
    (r'^participacion_hombres/$', 'hombres_pvbg'),
    (r'^participacion_lgbt/$', 'lgbt_pvbg'),
    (r'^participacion_hombre_discapasitado/$', 'hombres_discapasitado_pvbg'),
    (r'^participacion_mujeres_discapasitada/$', 'mujeres_discapasitada_pvbg'),
    (r'^participacion_hombre_etnia/$', 'hombres_etnia_pvbg'),
    (r'^participacion_mujeres_etnia/$', 'mujer_etnia_pvbg'),
    (r'^participacion_hombre_vih/$', 'hombres_vih_pvbg'),
    (r'^participacion_mujeres_vih/$', 'mujer_vih_pvbg'),
)