from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
		path('admin/', admin.site.urls),
		path('universities/list', views.universities_table, name='universities_table'),
		path("universities/create/", views.create_university, name='create_university'),
    path("universities/edit/<int:id>/", views.edit_university, name='edit_university'),
    path("universities/delete/<int:id>", views.delete_university, name='delete_university'),
    # path('students/', views.students, name='students'),
]