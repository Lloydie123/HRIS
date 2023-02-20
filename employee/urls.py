from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = 'employee'
urlpatterns = [
     path('index/', views.EmployeeListView.as_view(), name='index'),
     path('<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
     path('create/', views.CreateEmployee.as_view(), name='create'),
     path('<int:pk>/update/', views.UpdateEmployee.as_view(), name='update'),
     path('<int:pk>/delete/', views.DeleteEmployee.as_view(), name='delete'),
     path("signup/", views.SignUpView.as_view(), name="signup"),
     path('', TemplateView.as_view(template_name='employee/base.html'), name='base'),
     
     
     # For Department  
     path('dep', views.dep),  
     path('show_dep',views.show_dep),  
     path('edit_dep/<int:id>', views.edit_dep),
     path('update_dep/<int:id>', views.update_dep),  
     path('delete_dep/<int:id>', views.destroy_dep), 
     
]
