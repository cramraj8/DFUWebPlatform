from django.shortcuts import render


# Create your views here.
import pyrebase
from django.shortcuts import render
from django.contrib import auth
config = {
    'apiKey': "AIzaSyCcNlDbs4TTjWyO1y8EBj3deI9Cmk7ZR98",
    'authDomain': "dfumonitoring.firebaseapp.com",
    'databaseURL': "https://dfumonitoring.firebaseio.com",
    'projectId': "dfumonitoring",
    'storageBucket': "dfumonitoring.appspot.com",
    'messagingSenderId': "52399712278"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


def signIn(request):
    return render(request, "signIn.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "invalid credentials"
        return render(request, "signIn.html", {"messg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')


def signUp(request):
    return render(request, "signup.html")


# Delete this later
def welcome(request):
    return render(request, "welcome.html")


def entryform(request):
    return render(request, 'entryForm.html')


def formdata(request):
    return render(request, 'formdata.html')


def about(request):
    return render(request, 'about.html')


def imagedata(request):
    return render(request, 'imagedata.html')


def downloaddata(request):
    return render(request, 'downloaddata.html')


def uploaddata(request):
    return render(request, 'uploaddata.html')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def post_create(request):
    # Just added source code for post_create function/view
    import time
    from datetime import datetime, timezone
    import pytz
    tz = pytz.timezone('Asia/Colombo')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    print("mili" + str(millis))

    # ++++++++++++++++++++++++++++++++++++++++++++
    #               ++++++++++++++++++
    #                       8 inputs
    patientId = request.POST.get('patient_id')
    fullName = request.POST.get('fullname')
    email = request.POST.get('email')
    address = request.POST.get('address')
    age = request.POST.get('age')
    DOB = request.POST.get('dob')
    phone = request.POST.get('phone')
    dateOfFirstVisit = request.POST.get('dateoffirstvisit')
    #                    Medical Data
    #                      5 inputs
    height = request.POST.get('height')
    weight = request.POST.get('weight')
    bmi = request.POST.get('bmi')
    dateOfLastVisit = request.POST.get('dateoflastvisit')
    medicalHistory = request.POST.get('medicalhistory')
    #               Diabetic Related Data
    #                      3 inputs
    diabeticType = request.POST.get('diabetictype')
    dateOfIdentification = request.POST.get('dateofidentification')
    DFUCondition = request.POST.get('dfucondition')

    # ++++++++++++++++++++++++++++++++++++++++++++
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    print("info" + str(a))

    # ++++++++++++++++++++++++++++++++++++++++++++
    #               ++++++++++++++++++
    data = {
        "patientId": patientId,
        "fullName": fullName,
        "email": email,
        "address": address,
        "age": age,
        "DOB": DOB,
        "phone": phone,
        "dateOfFirstVisit": dateOfFirstVisit,
        # Medical Data
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "dateOfLastVisit": dateOfLastVisit,
        "medicalHistory": medicalHistory,
        # Diabetic Related Data
        "diabeticType": diabeticType,
        "dateOfIdentification": dateOfIdentification,
        "DFUCondition": DFUCondition,
    }
    # ++++++++++++++++++++++++++++++++++++++++++++

    database.child('users').child(a).child('reports').child(millis).set(data)
    name = database.child('users').child(a).child('details').child('name').get().val()
    return render(request, 'welcome.html', {'e': name})


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def post_check(request):

    import datetime

    time = request.GET.get('z')

    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    # work = database.child('users').child(a).child('reports').child(time).child('work').get().val()
    # progress = database.child('users').child(a).child('reports').child(time).child('progress').get().val()
    # img_url = database.child('users').child(a).child('reports').child(time).child('url').get().val()
    fullname = database.child('users').child(a).child('reports').child(time).child('fullname').get().val()

    progress = database.child('users').child(a).child('reports').child(time).child('email').get().val()

    img_url = database.child('users').child(a).child('reports').child(time).child('age').get().val()

    print(fullname)
    i = float(time)
    dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request, 'post_check.html', {'w': fullname, 'p': progress, 'd': dat, 'e': name, 'i': img_url})


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def check(request):
    import datetime
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']

    timestamps = database.child('users').child(a).child('reports').shallow().get().val()
    lis_time = []
    for i in timestamps:

        lis_time.append(i)

    lis_time.sort(reverse=True)

    print(lis_time)
    work = []

    for i in lis_time:

        # wor = database.child('users').child(a).child('reports').child(i).child('work').get().val()
        wor = database.child('users').child(a).child('reports').child(i).child('fullName').get().val()
        work.append(wor)
    print(work)

    date = []
    for i in lis_time:
        i = float(i)
        # dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        dat = datetime.datetime.fromtimestamp(i).strftime('%H:%M %d-%m-%Y')
        date.append(dat)

    print(date)

    comb_lis = zip(lis_time, date, work)
    name = database.child('users').child(a).child('details').child('name').get().val()

    return render(request, 'check.html', {'comb_lis': comb_lis, 'e': name})


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def get_data(request):
    fullName = request.POST.get('fullname')

    # idtoken = request.session['uid']
    # a = authe.get_account_info(idtoken)
    # a = a['users']
    # a = a[0]
    # a = a['localId']
    # print("info" + str(a))

    users = database.child("users").get()

    return render(request, 'formdata.html', {'e': users.val()})
