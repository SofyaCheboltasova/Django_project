from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from app import forms

def index(request):
    if request.method == "POST":
        #Если мы ввели данные в формы, и нажали на кнопку "Send Product", то тогда метод запроса будет POST(как мы указали в шаблоне),
        #и соответственно, выполнится этот блок, который просто перенаправит нас на страницу с информацией об продукте
        prod_name = request.POST.get("name")
        prod_cost = request.POST.get("cost")
        return HttpResponseRedirect(f"/app/product/{prod_cost}/{prod_name}")
    else:
        #Если же мы просто открыли страницу, то выполнится этот блок, который выведет нам форму
        data = {"form": forms.ProductForm()}
        return TemplateResponse(request, "index.html", data)
