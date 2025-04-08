from django.shortcuts import render
from django.http import JsonResponse
from .tasks import send_notification

import requests
import os

def index(request):
    return render(request, 'suggest/index.html')

def notify(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        chatid = request.POST.get('chatid')
        # TODO: Delay message
        send_notification(chatid, message)
        return JsonResponse({'status': 'ok'})

def search_name(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/fio"
        headers = {
            "Authorization": f"Token {os.getenv('DADATA_API_KEY')}",
            "Content-Type": "application/json"
        }
        data = {"query": query}
        response = requests.post(url, json = data, headers = headers)
        return JsonResponse(response.json())