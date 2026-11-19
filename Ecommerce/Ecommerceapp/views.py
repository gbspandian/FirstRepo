from django.shortcuts import render
from .models import Users, Address, Producttype, Productdetails, Productimages, ProductReviews, Orderconfirm, Orderdetails, Cartitems
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    
    showproducts = Productdetails.objects.select_related('productid').all()
    paginator = Paginator(showproducts,12)
    page_num = request.GET.get('page')
    productdetails = paginator.get_page(page_num)

    context = {'productdetails':productdetails}
    if(request.POST):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if(Users.objects.filter(username=username).exists() and Users.objects.filter(password=password).exists()):            
            request.session['is_logged_in'] = True
            loginuserdetails = Users.objects.get(username=username)
            request.session['name'] = loginuserdetails.name
            return render(request,'home.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'home.html', context)

def about(request):    
    return render(request,'about.html')

def logout(request):    
    request.session.flush() 
    return render(request,'home.html')

def login(request):    
    return render(request,'login.html')

def register(request):    
    return render(request,'register.html')

def regsuccess(request):
    name = request.POST.get("name")
    age = request.POST.get("age")
    gender = request.POST.get("gender")
    emailID = request.POST.get("emailID")
    phone = request.POST.get("phone")
    username = request.POST.get("username")
    password = request.POST.get("password")
    confirmpassword = request.POST.get("confirmpassword")
    adminuser = request.POST.get("adminuser")
    userphoto = request.POST.get("userphoto")
    if password != confirmpassword:
        messages.info(request,'Password and Confirm Password does not match')
        return render(request,'register.html')
    else:
        obj_register = Users()
        obj_register.name = name
        obj_register.age = age
        obj_register.emailID = emailID
        obj_register.phone = phone
        obj_register.username = username
        obj_register.password = password
        obj_register.adminuser = adminuser
        obj_register.userphoto = userphoto
        obj_register.genter = gender
        if(Users.objects.filter(username=username).exists() or Users.objects.filter(emailID=emailID).exists() or Users.objects.filter(phone=phone).exists()):        
            messages.info(request,'User name or Email or Phone number already exist!')
            return render(request,'register.html') 
        else:
            obj_register.save()
            return render(request,'regsuccess.html')
 
def productdetail(request):
    productid = request.GET['productid']
    showproduct = Productdetails.objects.get(id=productid)
    showimages = Productimages.objects.filter(productid=showproduct)
    showreviews = ProductReviews.objects.filter(productid=showproduct)
    showtype = Producttype.objects.get(id=showproduct.productid)
    context = {'productdetails':showproduct, 'productimages':showimages, 'productreviews':showreviews}

    return render(request,'productdetail.html',context)