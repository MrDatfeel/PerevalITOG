from django.contrib import admin
from django.urls import path, include
from .swagger import schema_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fstr_app.urls')),

    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
