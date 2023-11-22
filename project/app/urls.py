from django.urls import path
from . import views_students, views_university
from django.contrib import admin

urlpatterns = [
    path('', views_university.index, name='home'),
		path('admin/', admin.site.urls),
		path('universities/list', views_university.universities_table, name='universities_table'),
		path("universities/create/", views_university.create_university, name='create_university'),
    path("universities/edit/<int:id>/", views_university.edit_university, name='edit_university'),
    path("universities/delete/<int:id>", views_university.delete_university, name='delete_university'),
    
		path('students/list', views_students.students_table, name='students_table'),
		path("students/create/", views_students.create_student, name='create_student'),
		path("students/edit/<int:id>/", views_students.edit_student, name='edit_student'),
		path("students/delete/<int:id>", views_students.delete_student, name='delete_student'),
]