from django.urls import path
from . import views
urlpatterns = [
    path('resource/', views.import_from_excel, name='import_excel'),
    path('credit/resource/', views.credit_info_from_excel, name='credit_import_excel'),
    path('credit/credit-payment/', views.credit_payment_from_excel, name='credit_payment'),
    path('collection/', views.ApplicationView.as_view()),
    path('info/client/', views.CreditView.as_view()),
    path('info/payment/', views.PaymentView.as_view()),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
]
