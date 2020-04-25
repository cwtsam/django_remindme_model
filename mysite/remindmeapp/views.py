
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random


import demo_cli
#print(demo_cli.maux())
print(demo_cli.maux("hi",1))

def home(request, template_name="home.html"):
	context = {'title': 'RemindMe'}
	return render(request, template_name, context) ## allow rendering of the home page

@csrf_exempt
def get_response(request):
    response = {'status': None}

    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data['message'] # string message from user
        print(message)
        chat_response = "hello there"#demo_cli.maux("")#"hello there" # chatterbox response to message
        audio_source = random.choice(['hello','remindme'])
        print(chat_response)
        print(audio_source)
        response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True, 'audio': audio_source}
        response['status'] = 'ok'
    else:
        response['error'] = 'no post data found'
    return HttpResponse(json.dumps(response), content_type="application/json") 