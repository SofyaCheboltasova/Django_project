from django.db import models

class Universities(models.Model):
    id = models.IntegerField(verbose_name = "ID университета", primary_key=True)
    fullName = models.CharField(verbose_name = "Полное название", max_length=50, unique=True)
    shortName = models.CharField(verbose_name = "Сокращенное название", max_length=6)
    year = models.IntegerField(verbose_name = "Год основания")
    
    def __str__(self):
        return self.fullName
    
class Students(models.Model):
    id = models.IntegerField(verbose_name = "ID студента", primary_key=True)
    fullName = models.CharField(verbose_name = "ФИО")
    birthDate = models.DateField(verbose_name = "Дата рождения")
    university = models.ForeignKey(Universities, on_delete=models.CASCADE, verbose_name = "Университет",  to_field='id', related_name='student')
    admissionYear = models.DateField(verbose_name = "Дата поступления")
    
    def __str__(self):
        return self.fullName
  