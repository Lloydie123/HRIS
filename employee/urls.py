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
     
     # For Dashboard 
     path('dashboard/', views.dashboard, name='dashboard'), 
     
     # For Department
     
     path('dep', views.dep, name='create_department'),  
     path('show_dep',views.show_dep,  name='show_department'), 
     path('edit_dep/<int:id>', views.edit_dep, name='edit_department'),
     path('update_dep/<int:id>', views.update_dep,  name='update_department'),  
     path('delete_dep/<int:id>', views.destroy_dep, name='delete_department'), 
     
     # For Attendance
     path('attendance/', views.attendance, name='attendance'), 
     
     # For Leaves
     path('leaves/', views.leave, name='leaves'), 
     
     # For Payroll
     path('payroll/', views.payroll, name='payroll'), 
     
     # For Analytics and Reports
     path('analytics/', views.analytics, name='analytics'), 
     # For Settings
     
     # For Analytics and Reports
     path('settings/', views.settings, name='settings'), 
     # For Settings
     
]
