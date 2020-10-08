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

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/FB/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "ERROR..."
    return render(request, 'home.html', {'api':api})

def search(request):
    import requests
    import json

    if request.method == 'POST':
        search = request.POST['search']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + search + "/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "ERROR..."
        return render(request, 'search.html', {'api':api})
    else:
        return render(request, 'search.html', {'search':"Enter symbol above...."})

def about(request):
    return render(request, 'about.html', {})