from django.urls import path

from . import views

app_name = 'iet'

urlpatterns = [
    path('', views.Dashboard, name="dashboard"),
    path('download_pdf/', views.generate_pdf_view, name='download-pdf'),
    path('send_mail/', views.send_mail, name='send-mail'),
    path('ajax-query/', views.ajax_query, name='ajax-query'),

]
