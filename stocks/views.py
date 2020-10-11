from django.shortcuts import render, redirect
from .models import Userstock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import base64
    from io import BytesIO
    
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/AAPL/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "ERROR..."

    api_request1 = requests.get("https://cloud.iexapis.com/stable/stock/GOOG/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api1 = json.loads(api_request1.content)
    except Exception as e:
        api1 = "ERROR..."
    

    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='Apple Stock Chart')
    ax.grid()

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    htmlimg = 'data:image/png;base64,{}'.format(encoded)

    # Data for plotting
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
        title='Google Stock Chart')
    ax.grid()

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    htmlimg1 = 'data:image1/png;base64,{}'.format(encoded)

    #plt.show()

    return render(request, 'home.html', {'api':api,'api1':api1,'image':htmlimg,'image1':htmlimg1})

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
        
    except Exception as e:
        api1 = "ERROR..."
    
   # total = api['latestPrice'] api1['latestPrice']
    
    quantity = 0
    latvalue = 0
    latvalue1 = 0

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stock added"))
            return redirect('user')

        #quantity = request.POST['quantity']
        #latvalue = api['latestPrice'] * int(quantity)
        #latvalue1 = api1['latestPrice'] * int(quantity)

    else:
        addstock = Userstock.objects.all()
        return render(request, 'user.html', {'api':api,'api1':api1, 'latvalue':latvalue,'latvalue1':latvalue1,'addstock':addstock,'quantity':quantity})
        