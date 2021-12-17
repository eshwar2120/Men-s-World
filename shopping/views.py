from django.db.models.query_utils import Q
from django.shortcuts import redirect, render
from .models import user_details,products, user_products
from django.contrib import messages
from passlib.hash import pbkdf2_sha256

# Create your views here.
def home(request):
    sho1 = products.objects.filter(category='shoe')
    sh1 = products.objects.filter(category='shirt')
    je1 = products.objects.filter(category='jean')
    shoe = sho1[0:2]
    shirt = sh1[0:2]
    jean = je1[0:2]
    featured = []
    featured.append(shirt[0])
    featured.append(jean[0])
    return render(request,'index.html',{'shirt':shirt,'shoe':shoe,'jean':jean,'featured':featured})
def register(request):
    print('hello')
    email = request.session['email']
    return render(request,'register.html','user':email)
def login(request):
    email = request.session['email']
    return render(request,'login.html','user':email)
def about(request):
    email = request.session['email']
    return render(request,'about.html','user':email)
def contact(request):
    email = request.session['email']
    return render(request,'contact.html','user':email)
def product(request):
    shoe = products.objects.filter(category='shoe')
    shirt = products.objects.filter(category='shirt')
    jean = products.objects.filter(category='jean')
    email = request.session['email']

    return render(request,'products.html',{'shoe':shoe,'shirt':shirt,'jean':jean,'user':email})
    
def index(request):
    sho1 = products.objects.filter(category='shoe')
    sh1 = products.objects.filter(category='shirt')
    je1 = products.objects.filter(category='jean')
    shoe = sho1[0:2]
    shirt = sh1[0:2]
    jean = je1[0:2]
    featured = []
    featured.append(shirt[0])
    featured.append(jean[0])
    email = request.session['email']
    return render(request,'index.html',{'shirt':shirt,'shoe':shoe,'jean':jean,'featured':featured,'email':email,'user':email})
def mycart(request):
    email_id = request.session['email']
    obj = user_products.objects.filter(email=email_id)
    return render(request,'mycart.html',{'obj':obj})
def logout(request):
    del request.session['email']
    return render(request,'index.html')
def register_user(request):
    full_name = request.POST['name']
    password = request.POST['password']
    con_pass = request.POST['con_pass']
    email = request.POST['email']
    state = request.POST['state']
    address = request.POST['address']
    zip_code = request.POST['zip_code']
    if not(full_name):
        messages.error(request,'Enter the name')
        return render(request,'register.html')
    elif not(password):
        messages.error(request,'Enter the password')
        return render(request,'register.html')
    elif not(con_pass):
        messages.error(request,'Enter the confirm password')
        return render(request,'register.html')
    elif not(email):
        messages.error(request,'Enter the email id')
        return render(request,'register.html')
    elif not(state):
        messages.error(request,'Enter the state')
        return render(request,'register.html')
    elif not(address):
        messages.error(request,'Enter the address')
        return render(request,'register.html')
    elif not(zip_code):
        messages.error(request,'Enter the zipcode')
        return render(request,'register.html')

    hash_pass = pbkdf2_sha256.hash(password)
    obj = user_details()
    obj.name = full_name
    obj.password = hash_pass
    obj.email = email
    obj.address = address
    obj.zip_code = zip_code
    obj.save()
    request.session['email']=email
    return render(request,'index.html',{'email':email})
def user_login(request):
    email_id = request.POST['email']
    password = request.POST['password']
    if not(email_id):
        print(123)
        messages.error(request,'Enter the email id')
        return render(request,'login.html')
    elif not(password):
        messages.error(request,'Enter the password field')
        return render(request,'login.html')
    try:
        obj = user_details.objects.get(email=email_id)
        db_pass = obj.password
    except:
        messages.error(request,'user does not exists')
        return render(request,'login.html')
        result = False
    result = False
    if pbkdf2_sha256.verify(password,db_pass):
            
            result = True
            request.session['email']=email_id
    if result==True:
        messages.error(request,'valid user')
        return render(request,'index.html',{'email':email_id})
    else:
        messages.error(request,'invalid credentials')
        return redirect('/login')
def details(request):
    pr_id = request.GET['id']
    obj = products.objects.get(id=pr_id)
    return render(request,'demo.html',{'obj':obj})
def addtocart(request):
    
    email_id = request.session['email']
    p_id = request.POST['id']
    name = request.POST['name']
    price = request.POST['price']
    obj = user_products()
    obj.pro_id = p_id
    obj.name = name
    obj.price = price
    obj.email = email_id
    obj.save()
    obj1 = products.objects.get(id=p_id)
    messages.error(request,"Product addedd to Cart")
    return render(request,'demo.html',{'obj':obj1})
def success(request):
    email = request.GET['email']
    id = request.GET['id']
    name = request.GET['name']
    obj = user_products.objects.filter(email=email,id=id,name=name)
    obj.delete()
    return render(request,'success.html')
