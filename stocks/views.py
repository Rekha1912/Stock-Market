from django.shortcuts import render

def home(request):
    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/AAPL/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "ERROR..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})