from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro" ),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('ativar_conta/<str:token>/', views.ativar_conta, name="ativar_conta")

    

]