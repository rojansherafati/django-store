from django.shortcuts import render
from django.http import JsonResponse
from app01 import models

# Create your views here.

def index(request):
    return render(request,"index.html")
def customers_index(request):
    return render(request,"customers_index.html")
def customers_get_all(request):
    customers=models.Customer.objects.all()
    cts=[]
    for customer in customers:
        cts.append({
            "id":customer.id,
            "name":customer.name,
            "family":customer.family,
            "birth_year":customer.birth_year,
            "ssn":customer.ssn,
            "tel":customer.tel,
            "address":customer.address
        })
    return JsonResponse({"customers":cts})
def customers_delete(request,id):
    customers = models.Customer.objects.filter(id=id)
    customers.delete()
    return JsonResponse({"message":"saved"})
def customers_store(request):
    id=int(request.POST["id"])
    if id == 0:
        name=request.POST["name"]
        family=request.POST["family"]
        birth_year=request.POST["birth_year"]
        ssn=request.POST["ssn"]
        tel=request.POST["tel"]
        address=request.POST["address"]
        models.Category.objects.create(name=name,family=family,birth_year=birth_year,ssn=ssn,tel=tel,address=address)
        return JsonResponse({"message":"saved"})
    else:
        customer=models.Customer.objects.get(id=id)
        customer.name=request.POST["name"]
        customer.family=request.POST["family"]
        customer.birth_year=request.POST["birth_year"]
        customer.ssn=request.POST["ssn"]
        customer.tel=request.POST["tel"]
        customer.address=request.POST["address"]
        customer.save()
        return JsonResponse({"message":"saved"})
def customers_edit(request,id):
    customer=models.Customer.objects.get(id=id)
    content={"id":customer.id,
             "name":customer.name,
             "family":customer.family,
             "birth_year":customer.birth_year,
             "ssn":customer.ssn,
             "tel":customer.tel,
             "address":customer.address}
    return JsonResponse(content)


def sellers_index(request):
    return render(request,"sellers_index.html")
def sellers_get_all(request):
    sellers=models.Seller.objects.all()
    sls=[]
    for seller in sellers:
        sls.append({
            "id":seller.id,
            "name":seller.name,
            "address":seller.address
        })
    return JsonResponse({"sellers":sls})
def sellers_delete(request,id):
    sellers = models.Seller.objects.filter(id=id)
    sellers.delete()
    return JsonResponse({"message":"saved"})
def sellers_store(request):
    id=int(request.POST["id"])
    if id == 0:
        name=request.POST["name"]
        address=request.POST["address"]
        models.Category.objects.create(name=name,address=address)
        return JsonResponse({"message":"saved"})
    else:
        seller=models.Seller.objects.get(id=id)
        seller.name=request.POST["name"]
        seller.address=request.POST["address"]
        seller.save()
        return JsonResponse({"message":"saved"})
def sellers_edit(request,id):
    seller=models.Seller.objects.get(id=id)
    content={"id":seller.id,
             "name":seller.name,
             "address":seller.address}
    return JsonResponse(content)


def products_index(request):
    return render(request,"products_index.html")
def products_edit(request,id):
    return render(request,"products_form.html")
def products_get_one(request):
    product=models.Product.objects.get(id=request.POST["id"])
    content={"id":product.id,
            "name":product.name,
            "price":product.price,
            "brand":product.brand.name,
            "categories":product.categories.name}
    return JsonResponse(content)
def products_get_all(request):
    products=models.Product.objects.all()
    pds=[]
    for product in products:
        cts=[]
        for category in product.categories.all():
            cts.append(category.name)
        pds.append({
            "id":product.id,
            "name":product.name,
            "price":product.price,
            "brand":product.brand.name,
            "categories":cts
        })
    return JsonResponse({"products":pds})
def products_delete(request,id):
    products = models.Product.objects.filter(id=id)
    products.delete()
    return JsonResponse({"message":"saved"})
def products_store(request):
    name=request.POST["name"]
    price=request.POST["price"]
    brd=request.POST["brand"]
    product=models.Product.objects.create(name=name,price=price,brand=models.Brand.objects.get(id=brd))
    categories=request.POST.getlist("categories")
    for category in categories:
        product.categories.add(models.Category.objects.get(id=category))
    return JsonResponse({"message":"saved"})
def products_form(request):
    return render(request,"products_form.html")


def categories_get_all(request):
    categories=models.Category.objects.all()
    cts=[]
    for category in categories:
        cts.append({
            "id":category.id,
            "name":category.name,
        })
    return JsonResponse({"categories":cts})
def categories_get_data(request):
    categories=models.Category.objects.all()
    cas=[]
    for category in categories:
        cas.append({"id":category.id,
                     "name":category.name
        })
    return JsonResponse({"categories":cas})
def categories_delete(request,id):
    categories=models.Category.objects.get(id=id)
    products=models.Product.objects.filter(categories=categories)
    if len(products) == 0:
        categories.delete()
        return JsonResponse({"error":False,"message":"succeed"})
    else:
        return JsonResponse({"error":True,"message":"brand is already in use"})
def categories_modal_store(request):
    name=request.POST["name"]
    if models.Category.objects.filter(name=name):
        return JsonResponse({"message":"error"})
    else:
       models.Category.objects.create(name=name)
       return JsonResponse({"message":"saved"})
def categories_store(request):
    id=int(request.POST["id"])
    if id == 0:
        name=request.POST["name"]
        models.Category.objects.create(name=name)
        return JsonResponse({"message":"saved"})
    else:
        category=models.Category.objects.get(id=id)
        category.name=request.POST["name"]
        category.save()
        return JsonResponse({"message":"saved"})
def categories_index(request):
    return render(request,"categories_index.html")
def categories_edit(request,id):
    category=models.Category.objects.get(id=id)
    content={"id":category.id,
             "name":category.name}
    return JsonResponse(content)

def brands_get_all(request):
    brands=models.Brand.objects.all()
    brs=[]
    for brand in brands:
        brs.append({
            "id":brand.id,
            "name":brand.name,
        })
    return JsonResponse({"brands":brs})
def brands_get_data(request):
    brands=models.Brand.objects.all()
    brs=[]
    for brand in brands:
        brs.append({"id":brand.id,
                     "name":brand.name
        })
    return JsonResponse({"brands":brs})
def brands_delete(request,id):
    brand=models.Brand.objects.get(id=id)
    products=models.Product.objects.filter(brand=brand)
    if len(products) == 0:
        brand.delete()
        return JsonResponse({"error":False,"message":"succeed"})
    else:
        return JsonResponse({"error":True,"message":"brand is already in use"})
def brands_modal_store(request):
    name=request.POST["name"]
    if models.Brand.objects.filter(name=name):
        return JsonResponse({"message":"error"})
    else:
       models.Brand.objects.create(name=name)
       return JsonResponse({"message":"saved"})
def brands_store(request):
    id=int(request.POST["id"])
    if id == 0:
        name=request.POST["name"]
        models.Brand.objects.create(name=name)
        return JsonResponse({"message":"saved"})
    else:
        brand=models.Brand.objects.get(id=id)
        brand.name=request.POST["name"]
        brand.save()
        return JsonResponse({"message":"saved"})
def brands_index(request):
    return render(request,"brands_index.html")
def brands_edit(request,id):
    brand=models.Brand.objects.get(id=id)
    content={"id":brand.id,
             "name":brand.name}
    return JsonResponse(content)