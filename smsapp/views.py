from django.shortcuts import render
from django.http import HttpResponse
import json, ssl
import urllib.request
import urllib.parse
from twilio.rest import Client



# Create your views here.
def home(request):

    return render(request,'index.html')

def twilio(request):
    if "submitt" in request.POST:
        print("Submitted")
    account_sid = 'AC5b053d8700e46a530776090952c3d430'
    auth_token = '59dc6c5051d84fc65f28878a64a8e12d'
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
                .create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+15005550006',
                        to='+919962341331 '
                    )

        print(message.sid)
        return render(request,'index.html')
    except Exception as e:
        print(str(e))
        return render(request,'twilio.html',context={'error':str(e)})
    
def textlocal(request):
    data =  urllib.parse.urlencode({'apikey': 'NTQ1OTQ2NzM2ZTc0NDY1NDMxNWEzNDc5NzM0ZDdhNTc=', 'numbers': '919962341331',
        'message' : 'hello', 'sender': 'TESTIN'})
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    data = data.encode('utf-8')
    requestt = urllib.request.Request("https://api.textlocal.in/send/?",)
    f = urllib.request.urlopen(url=requestt, data=data,context=ctx,)
    fr = f.read()
    print(fr)
