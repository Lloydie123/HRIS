from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'employee'
urlpatterns = [
     path('index/', views.ListView.as_view(), name='index'),
     path('create/', views.CreateEmployee.as_view(), name='create'),
     path('<int:pk>/update/', views.UpdateEmployee.as_view(), name='update'),
     path('<int:pk>/delete/', views.DeleteEmployee.as_view(), name='delete'),
     path("signup/", views.SignUpView.as_view(), name="signup"),
     path('', TemplateView.as_view(template_name='employee/base.html'), name='base'),
]
