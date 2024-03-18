from django.urls import path
from . import views
urlpatterns = [
    path('resource/', views.import_from_excel),
    path('collection/', views.ApplicationView.as_view())
]
