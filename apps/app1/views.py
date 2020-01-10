from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import User, Lister,Dates
from django.contrib import messages
import requests
import json


def index(request):
    return render(request, 'app1/index.html')


def signUp(request):
    return render(request, 'app1/signup.html')


def login(request):
    return render(request, 'app1/login.html')


def listerLoginReg(request):
    return render(request, 'app1/listerlogin.html')


def userLogReg(request):
    return render(request, 'app1/userlogin.html')

def listdashboard(request):
    user = Lister.objects.get(id = request.session['uid'])
    context = {'user':user}
    return render(request,'app1/listerdashboard.html',context)

def userdashboard(request):
    return render(request,'app1/userdashboard.html')

def yourTrip(request):
    
    yourtrip =[]
    
    uid = request.session['uid']
    dates = Dates.objects.all()
    for date in dates:
        if date.user.id == uid:
            # print(date)
            yourtrip.append(date)
    
    print(yourtrip)
    context = {'trips':yourtrip}
    
    return render(request,'app1/yourtrip.html',context)

def search(request):
    if request.method == "POST":
        result = []
        # print(request.POST)
        # print(type(request.POST['start_date']))
        searches = Lister.objects.filter(location= request.POST['location'])
        
        for search in searches:
            checks = search.dates.all()
            # print('*'*30)
            # print(checks.values())
            # print('*'*30)
            if len(checks)>0:
                for check in checks:
                    print(type(check.start_date))
                    print(type(request.POST['start_date']))
                    if str(check.start_date)!= request.POST['start_date']:
                        result.append(search)
            else:
                result.append(search)
        # print('*'*30)
        print(result)
        
        # location
        location= request.POST['location']
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key=your api key').json()
        # y= json.la(response)
        # print(response['results'][0]['geometry']['location']['lat'])
        lat = response['results'][0]['geometry']['location']['lat']
        lon =response['results'][0]['geometry']['location']['lng']
        context ={"searches":result,
                  'lati':lat,'lon':lon}
        # print(context)
        print('*'*30)
        print(type(context['searches']))
        return render(request,'app1/usercarbook.html',context)

def yourbooking(request,car_id):
    print(car_id)
    return render(request,'app1/dropcaruser.html')
        


    


def registerlister(request):
    if request.method == "POST":
        print(request.POST)
        pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())

        # error = User.objects.basic_validation(request.POST)

        # if len(error) > 0:
        #     for val in error.values():
        #         messages.error(request, val)
        #         return redirect("/")
        # else:
        
        address = f"{request.POST['address']} {request.POST['location']}"
        
        print(address)
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key=your api key').json()
        print(response)
        lat = response['results'][0]['geometry']['location']['lat']
        lon =response['results'][0]['geometry']['location']['lng']
        
        print(f'lat is {lat}  ****** long is {lon}')

        # print(request.FILES["car_image"])
        store_user = Lister.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"], password=pw_hash,location=request.POST["location"],car_type=request.POST["car_type"],car_model=request.POST["car_model"],
                                           rental_price=int(request.POST["rental_price"]),image = request.FILES["car_image"],latitude=lat,longitude=lon)
        # print(store_user)
        request.session['uid'] = store_user.id
        return redirect('/listdashboard')
        
        
    #     first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    # email = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    # car_type = models.CharField(max_length=100)
    # car_model = models.CharField(max_length=100)
    # rental_price = models.FloatField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # latitude = models.FloatField(null = True)
    # longitude = models.FloatField(null = True)


def loglister(request):
    if request.method == "POST":
        print(request.POST)
        user = Lister.objects.filter(email=request.POST["email"])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST["password"].encode(), log_user.password.encode()):
                request.session['uid'] = log_user.id
                print("checked password")
                return redirect('/listdashboard')
        #     else:
        #         val = "Invalid Password"
        #         messages.error(request, val)
        #         return redirect('/')
        # else:
        #     val = "Invalid Email"
        #     messages.error(request, val)
        #     return redirect('/')

def registeruser(request):
    if request.method == "POST":
        print(request.POST)
        pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())

        # error = User.objects.basic_validation(request.POST)

        # if len(error) > 0:
        #     for val in error.values():
        #         messages.error(request, val)
        #         return redirect("/")
        # else:

        store_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST["email"], password=pw_hash,location=request.POST["location"])
        print(store_user)
        request.session['uid'] = store_user.id
        return redirect('/userdashboard')
        
def loguser(request):
    if request.method == "POST":
        print(request.POST)
        user = User.objects.filter(email=request.POST["email"])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST["password"].encode(), log_user.password.encode()):
                request.session['uid'] = log_user.id
                print("checked password")
                return redirect('/userdashboard')

def bookCar(request,car_id):
    book_car = Lister.objects.get(id = car_id)
    context = {'car':book_car}
    
    return render(request,'app1/bookcar.html',context)

def bookthiscar(request):
    if request.method == "POST":
        print(request.POST)
        user = User.objects.get(id = request.session['uid'])
        lister = Lister.objects.get(id = request.POST['lister_id'])
        booking = Dates.objects.create(start_date=request.POST['start_date'],end_date=request.POST['end_date'],user=user,lister=lister)
        # context = {'bookings':booking}
        
        return redirect('/yourtrip')
        
       
        
        
        
    #     start_date = models.DateField()
    # end_date = models.DateField()
    # user = models.ForeignKey(User,related_name="dates")
    # lister = models.ForeignKey(Lister,related_name="dates")
        
    
    
    
        
def logout(request):
    del request.session["uid"]
    return redirect('/')

