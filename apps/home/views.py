from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import website,DurationUsage,Availaible_ip,logs_generated,logs_json
from django.shortcuts import redirect , render 
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone
import time
from datetime import  datetime
import csv
from .blocker import block
import re
import json
import urllib.request

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print(external_ip)



@login_required(login_url="/login/")
def index(request):
    
    objects=website.objects.filter(author=request.user)
    objects2=DurationUsage.objects.all()
    objects3=Availaible_ip.objects.all()
    
    if request.method=='POST' and  'add_websites' in request.POST:
        blocked_websites=request.POST.get('blocked')
        if str(blocked_websites) not in [ x.website_url for x in objects]:
             weburl= request.POST.get('blocked')
             data=website(author=request.user,website_url=weburl)
             data.save()
             return redirect(reverse(("home")))
        
    if request.method=='POST' and  'generate' in request.POST:
        for w in objects:
            block(replace(str(w.website_url)))
        duration=request.POST.get('Duration')
        usage=request.POST.get('Usage')
        ip_address=request.POST.get('ip_address')
        data2=DurationUsage(author=request.user,duration=duration,usage=usage,ip_address=ip_address)
        if duration and usage and ip_address:
            data2.save()

        with open('apps\home\data.csv', 'r') as csv_file:
            print("helllooo")
            reader = csv.reader(csv_file)
            delimeter=next(reader)


    # Iterate over each row of the CSV file and create a new model instance
            for row in reader:
                date=datetime.now().strftime("%H:%M:%S")
                ip_src=row[1]
                ip_dst=row[2]
                action=row[3]
                logs=logs_generated(author=request.user,date=date,ip_address_src=ip_src,ip_address_dst=ip_dst,action=action)
                logs.save()
                time.sleep(1)
                print(logs)

        with open("apps\home\logs.json","r") as f:
            json_object = json.load(f)
        for i in json_object["packet"]:
            lenght=i["lenght"]
            Layer_ETH=""
            Layer_IP=""
            Layer_UDP=""
            Layer_ARP=""
            Layer_TCP=""
            Layer_TLS=""
            Layer_DNS=""
            try:
                Layer_ETH=i["Layer ETH"]
            except:
                pass
            try:
                Layer_IP=i["Layer IP"]
            except:
                pass
            try:
                Layer_UDP=i["Layer UDP"]
            except:
                pass
            try:
                Layer_ARP=i["Layer ARP"]
            except:
                pass
            try:
                Layer_TCP=i["Layer TCP"]
            except:
                pass
            try:
                Layer_TLS=i["Layer TLS"]
            except:
                pass
            try:
                Layer_DNS=i["Layer DNS"]
            except:
                pass
            
                

            json_logs=logs_json(author=request.user,lenght=lenght,Layer_ETH=Layer_ETH,Layer_IP=Layer_IP,Layer_UDP=Layer_UDP,Layer_ARP=Layer_ARP,Layer_TCP=Layer_TCP,Layer_TLS=Layer_TLS,Layer_DNS=Layer_DNS)
            json_logs.save()
            time.sleep(2)  


        
        

        
       
            
    generate_logs = logs_generated.objects.all()



    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

    context = {'segment': 'index',"blocked_websites":objects,"generated_proxy":objects2,"available_ips":objects3,"generate_logs":generate_logs,"ip":external_ip}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

    
@login_required(login_url="/login/")
def updateuser(request):
    if request.method =='POST' :
        id = request.user.id
        username = request.user.username  
        password = request.user.password
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        user=User(id=id,username=username,email=email, first_name=firstname,last_name=lastname,password=password)
        
        user.save(force_update=True)
        html_template = loader.get_template('home/user.html')
        return render(request,'home/user.html')
        
@login_required(login_url="/login/")
def getLogs(request):
    query_set=logs_generated.objects.filter(author=request.user)
    return JsonResponse({"logs":list(query_set.values())})

@login_required(login_url="/login/")
def getLogs_json(request):
    query_set=logs_json.objects.filter(author=request.user)
    return JsonResponse({"logs_json":list(query_set.values())})


@login_required(login_url="/login/")
def notifwebsites(request):
    objects=website.objects.filter(author=request.user)
    context = {"blocked_websites":objects}
    html_template = loader.get_template('home/notifications.html')
    return render(context, request, "home/notifications.html")



def replace(string) :
    match=re.search(r'([A-Za-z0-9]{3,13}\.[a-z]+(\.[a-z]+)?)', string)
    return match.group()

@login_required(login_url="/login/")
def ip_request(request):
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    context={"ip":external_ip}
    return render( request,"includes/sidebar.html",context)
