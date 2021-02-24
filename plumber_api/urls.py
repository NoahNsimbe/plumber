from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from users.api import ClientViewSet, PlumberViewSet

admin.AdminSite.site_header = 'Plumbers.com Administration'
admin.AdminSite.site_title = 'Plumbers.com Admin'

router = routers.DefaultRouter()
router.register('clients', ClientViewSet)
router.register('plumbers', PlumberViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<version>/', include(router.urls)),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
