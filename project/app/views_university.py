from django.template.response import TemplateResponse
from django.db import IntegrityError

from django.shortcuts import render
from .models import Universities

def index(request):
    return TemplateResponse(request, "index.html")

def universities_table(request):
    universities = Universities.objects.all().order_by('id')
    return render(request, 'universities.html', {'universities': universities})

def create_university(request):
    id = request.POST.get("id")
    fullName = request.POST.get("fullName")
    shortName = request.POST.get("shortName")
    year = request.POST.get("year")
    error_message = ""
    
    if not (id and fullName and shortName and year):
      error_message = "Необходимо заполнить все поля"
    else:
      try:
        Universities.objects.create(id=id, fullName=fullName, shortName=shortName, year=year)
      except IntegrityError:
        error_message = "Университет с таким ID уже существует. Проверьте введенные данные."    
        
    universities = Universities.objects.all().order_by('id')
    return render(request, 'universities.html', {'universities': universities, 'error_message': error_message})

def edit_university(request, id):
    university = Universities.objects.get(id=id)
    error_message = ""
 
    if request.method == "POST":
      university.id = request.POST.get("id")
      university.fullName = request.POST.get("fullName")
      university.shortName = request.POST.get("shortName")
      university.year = request.POST.get("year")
      
      if not (university.id and university.fullName and university.shortName and university.year):
        error_message = "Необходимо заполнить все поля"
        return render(request, 'edit_university.html', {'university': university, 'error_message': error_message})
      else:
        university.save()
        universities = Universities.objects.all().order_by('id')
        return render(request, 'universities.html', {'universities': universities})
    else:
      return render(request, "edit_university.html", {'university': university})
     		 
def delete_university(request, id):
    university = Universities.objects.get(id=id)
    university.delete()
    universities = Universities.objects.all().order_by('id')
    return render(request, 'universities.html', {'universities': universities})
