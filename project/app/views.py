from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.response import TemplateResponse
from app import forms
from django.db import models

def index(request):
    if request.method == "POST":
        #Если мы ввели данные в формы, и нажали на кнопку "Send Product", то тогда метод запроса будет POST(как мы указали в шаблоне),
        #и соответственно, выполнится этот блок, который просто перенаправит нас на страницу с информацией об продукте
        prod_name = request.POST.get("name")
        prod_cost = request.POST.get("cost")
        return HttpResponseRedirect(f"/product/{prod_cost}/{prod_name}")
    else:
        #Если же мы просто открыли страницу, то выполнится этот блок, который выведет нам форму
        data = {"form": forms.ProductForm()}
        return TemplateResponse(request, "index.html", data)

#Теперь мы получаем продукт по id, и если такого продукта нет, возвращаем ошибку 
def product(request, prod_id):
    try:
        curr_prod = models.Product.objects.get(id=prod_id)
        data = {"prod_name": curr_prod.name, "prod_cost":curr_prod.cost}
        return TemplateResponse(request, "product.html", data)
    except models.Product.DoesNotExist:
        return HttpResponseNotFound("Продукта с таким id не существует")


def create_product(request):
    if request.method == "POST":
        prod_name = request.POST.get("name")
        prod_cost = request.POST.get("cost")
        #Добавляем продукт в базу данных
        product = models.Product.objects.create(name = prod_name, cost = prod_cost)
        #Получаем id добавленного для того, чтобы перейти на его страницу
        new_id = product.id
        return HttpResponseRedirect(f"/product/{new_id}")
    else:
        data = {"form": forms.ProductForm()}
        return TemplateResponse(request, "create_product.html", data)
    
def delete_product(request, prod_id):
    try:
        product = models.Product.objects.get(id=prod_id)
        product.delete()
        return HttpResponseRedirect("/product/")
    except models.Product.DoesNotExist:
        return HttpResponseNotFound("Продукта с таким id не существует")

def product_list(request):
    #Получаем все продукты из базы
    all_prods = models.Product.objects.all()
    data = {"products": all_prods}
    return TemplateResponse(request, "product_list.html", data)