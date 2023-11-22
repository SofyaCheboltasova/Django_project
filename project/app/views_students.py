import datetime
from django.db import IntegrityError

from django.shortcuts import render
from .models import Universities, Students

def validate_dates(birth_date, admission_year):
    birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
    admission_year = datetime.datetime.strptime(admission_year, "%Y-%m-%d").date()
    today = datetime.date.today()

    min_age = 17
    max_admission_year = today.year

    age = today.year - birth_date.year
    is_admission_year_valid = admission_year.year <= max_admission_year

    if age < min_age or not is_admission_year_valid:
        return False
    return True


def students_table(request):
    students = Students.objects.all().order_by('id')
    universities = Universities.objects.all().order_by('id')
    return render(request, 'students.html', {'students': students, 'universities': universities})


def create_student(request):
    id = request.POST.get("id")
    fullName = request.POST.get("fullName")
    birthDate = request.POST.get("birthDate")
    university = request.POST.get("university")
    admissionYear = request.POST.get("admissionYear")
    error_message = ""
    
    if not (id and fullName and birthDate and admissionYear):
      error_message = "Необходимо заполнить все поля"
    else:
      try:
        university = Universities.objects.get(id=university)
        Students.objects.create(id=id, fullName=fullName, birthDate=birthDate, 
                                university=university, admissionYear=admissionYear)
      except IntegrityError:
        error_message = "Студент с таким ID уже существует. Проверьте введенные данные."    
        
    students = Students.objects.all().order_by('id')
    universities = Universities.objects.all().order_by('id')
    return render(request, 'students.html', {'students': students, 'universities': universities, 'error_message': error_message})

   
def edit_student(request, id):
    student = Students.objects.get(id=id)
    universities = Universities.objects.all().order_by('id')
    error_message = ""

    if request.method == "POST":
      student.id = request.POST.get("id")
      student.fullName = request.POST.get("fullName")
      student.birthDate = request.POST.get("birthDate")
      student.admissionYear = request.POST.get("admissionYear")

      university_id = request.POST.get("university")
      student.university = Universities.objects.get(id=university_id)
            
      if not (student.id and student.fullName and student.birthDate and student.university and student.admissionYear):
          error_message = "Необходимо заполнить все поля"
          return render(request, 'edit_student.html', {'student': student, 'universities': universities, 'error_message': error_message})
      elif not validate_dates(student.birthDate, student.admissionYear):
          error_message = "Недопустимые даты"
          return render(request, 'edit_student.html', {'student': student, 'universities': universities, 'error_message': error_message})
      else:
          student.save()
          students = Students.objects.all().order_by('id')
          return render(request, 'students.html', {'students': students, 'universities': universities})
    else:
      return render(request, "edit_student.html", {'student': student, 'universities': universities})


def delete_student(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    students = Students.objects.all().order_by('id')
    universities = Universities.objects.all().order_by('id')
    return render(request, 'students.html', {'students': students, 'universities': universities})