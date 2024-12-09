from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('memberspage/', views.membersPage, name="memberspage"),
    path('pricing/', views.pricing, name="pricing"),
    path('contact/', views.contact, name="contact"),
    path('logout/', views.logout, name='logout'),
    path('delete-account/', views.delete_account, name='delete_account'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)