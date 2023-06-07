from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('social-login/', include('social_login.api.v1.urls')),
    path('api/v1/', include('users.api.v1.urls')),
    path('api/v1/', include('stores.api.v1.urls')),
    path('api/v1/', include('payments.api.v1.urls')),
    path('auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "E-Commerce API"
admin.site.site_title = "E-Commerce Admin Portal"
admin.site.index_title = "E-Commerce Admin"

# swagger
api_info = openapi.Info(
    title="E-Commerce API",
    default_version="v1",
    description="API documentation for E-Commerce App",
)

schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)

urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs"),
    # path("firebase-messaging-sw.js", TemplateView.as_view(template_name="firebase-messaging-sw.js",
    #     content_type='application/javascript'))
]

urlpatterns += [path("", TemplateView.as_view(template_name='index.html'))]
urlpatterns += [re_path(r"^(?:.*)/?$",
                TemplateView.as_view(template_name='index.html'))]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))]
