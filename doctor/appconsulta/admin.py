from django.contrib import admin
from appconsulta.models import TomarSignoVital, Historia, Receta, DetalleReceta, HistoriaDetalle


admin.site.register(TomarSignoVital)
admin.site.register(Historia)
admin.site.register(Receta)
admin.site.register(DetalleReceta)
admin.site.register(HistoriaDetalle)