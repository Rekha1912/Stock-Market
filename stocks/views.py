from django.shortcuts import render

def home(request):
    import requests
    import json
    

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/AAPL/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "ERROR..."

    api_request1 = requests.get("https://cloud.iexapis.com/stable/stock/GOOG/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api1 = json.loads(api_request1.content)
        xxx = api1['latestPrice'] * 100
    except Exception as e:
        api1 = "ERROR..."
    return render(request, 'home.html', {'api':api,'api1':api1, 'xxx':xxx})

    

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

def user(request):
    return render(request, 'user.html', {})