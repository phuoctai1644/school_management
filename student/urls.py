from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('edit/<int:pk>', views.edit_student, name='Edit'),
    path('delete/<int:pk>', views.delete_student, name='Delete Student'),
    path('<int:pk>', views.student_detail, name='Detail'),
    path('', views.student_list, name='List')
]
