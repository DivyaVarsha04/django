from django.http import HttpResponseNotFound
from django.shortcuts import HttpResponse,redirect,render

def home(request):
    return redirect('login')
def signup(request):
    return HttpResponse('<h1> Signup page</h1> ')
# day=["Monday\n","Tuesday\n","Wednesday\n","Thursday\n","Friday\n","Saturday\n","Sunday\n"]
# def days(request):
#     return HttpResponse(day)
def login(request):
    return HttpResponse('Login Page.....')
def mainpg(request):
    return HttpResponse("<h1>Main Page......")
# def monday(request):
#     return HttpResponse("It's Monday")
# def tuesday(request):
#     return HttpResponse("It's Tuesday")
# def wednesday(request):
#     return HttpResponse("It's Wednesday")
# def thursday(request):
#     return HttpResponse("It's Thursday")
# def friday(request):
#     return HttpResponse("It's Friday")
# def saturday(request):
#     return HttpResponse("It's Saturday")
# def sunday(request):
#     return HttpResponse("It's Sunday")
weekday={"Monday":"go to study","Tuesday":"go to temple","Wednesday":"go to KFC","Thursday":"GO TO STUDY","Friday":"GO TO TEMPLE","Saturday":"GO TO MOVIE","Sunday":"GO TO SLEEPMODE"}
def days(request,day):
    day=day.capitalize()
    if  day in weekday:
        return HttpResponse(f"""<h1 style='color:green'>{weekday[day].capitalize()}</h1>""")
    else:
        return HttpResponse("""<h1 style='color:red'>Page Not found</h1>""")
    

    
week={"0":"Sunday","1":"Monday","2":"Tuesday","3":"Wednesday","4":"Thursday","5":"Friday","6":"Saturday"}
def weeks(request,wee):
    if wee in week:
        return HttpResponse(f'{week[wee]}')
    else:
        return HttpResponse("Not found")
    
s_details={'1':'ramu','2':'somu','3':'raju','4':'varsha'}
def sinfo(request,name):
    if name.isdigit():
        return redirect('i_s')
    elif name in s_details.values():
        return HttpResponse(f'hi {name}')
    else:
        return HttpResponse('bye')
def i_s(request,rollno):
    if rollno in s_details:
        return HttpResponse(s_details[rollno])

def home(request):
    return render(request,'home.html') 

def student(request):
    return render(request,'student.html')


weekdays={"Monday":"Go to Qspiders","Tuesday":"Go to temple","Wednesday":"Go to KFC","Thursday":"GO TO STUDY","Friday":"GO TO TEMPLE","Saturday":"GO TO MOVIE","Sunday":"GO TO SLEEPMODE"}

 
def main(request):
    info={
        "weekday": weekdays
        }

    return render(request,'main.html',info)

def days(request, days): 
    if days.capitalize() in weekdays:
        # return HttpResponse(f'{weekdays[days.capitalize()]}')
        task = {
            'task': weekdays[days.capitalize()]
        }
        return render(request, 'day.html', context=task)
    else:
        return render(request,'Error.html')
    
    
mon={"January":"Pongal","February":"Valentine month","March":"Public Exam","April":"April Fool...","May":"Summer ","June":"school Reopen","July":"Nothing ","August":"Independence day","September":"Teacher's Day","October":"Gandhi's brithday","November":"Children's day","December":"Merry Christmas"}
def main_month(request):
    div={
        "month": mon
    }
    return render(request,'main_month.html',div)

def months(request,month):   
    month=month.capitalize()
    if  month in mon:
        task1={
            'task1':mon[month]
        }
        return render(request,'month.html',context=task1)
    else:
        return render(request,'Error.html')



# def main(request):
#     info={"name": "Varsha","sid":413,"address":"Chennai","phno":9384}
#     return render(request,'main.html',context=info)
#render takes three arguments  request, which file to execute "file name',context or data to be send(dict format)
#Ginger tags/Django template tags (2  types) {% %}->looping and conditional stmt and oops,  {{key}}    --> for sending data from backend to frontend



