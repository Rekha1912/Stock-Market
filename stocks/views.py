from django.shortcuts import render, redirect
from .models import Userstock, Cash, StockQuantity
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
        api = "AAPL DATA ERROR..."

    api_request1 = requests.get("https://cloud.iexapis.com/stable/stock/GOOG/quote?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api1 = json.loads(api_request1.content)
    except Exception as e:
        api1 = "GOOG DATA ERROR..."
    
    api_chart_request = requests.get("https://cloud.iexapis.com/stable/stock/AAPL/chart/5d?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api_chart = json.loads(api_chart_request.content)
    except Exception as e:
        api_chart = "APPL CHART ERROR..."
    time1 = [];
    price1 = [];
    for item in api_chart:
        time1.append(item['date'])
        price1.append(item['high'])

    fig, ax = plt.subplots()
    ax.plot(time1,price1)

    ax.set(xlabel='date(yyyy-mm-dd)', ylabel='price ($)',
        title='APPL weekly Stock Chart')
    ax.grid()

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    htmlimg = 'data:image/png;base64,{}'.format(encoded)
    
    api_chart_request1 = requests.get("https://cloud.iexapis.com/stable/stock/GOOG/chart/5d?token=pk_eb2cdb77af5847bb94c4ec9b9dfc076e")
    try:
        api_chart = json.loads(api_chart_request1.content)
    except Exception as e:
        api_chart = "GOOG CHART ERROR..."
    time2 = [];
    price2 = [];
    for item in api_chart:
        time2.append(item['date'])
        price2.append(item['high'])

    fig, ax = plt.subplots()
    ax.plot(time2, price2)

    ax.set(xlabel='date(yyyy-mm-dd)', ylabel='price ($)',
        title='GOOG weekly Stock Chart')
    ax.grid()

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    htmlimg1 = 'data:image1/png;base64,{}'.format(encoded)

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
    
    quantity = 0
    latvalue = 0
    latvalue1 = 0
    display_message = ''

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stock added"))
            if request.POST['action'] == 'buy':
                cash_instance, created = Cash.objects.get_or_create(username=request.POST['username'])
                quantity_instance, created = StockQuantity.objects.get_or_create(username=request.POST['username'], stockname=request.POST['stockname'])
                quantity = request.POST['quantity']
                calclatvalue = float(request.POST['lastprice']) * int(quantity)
                totalvalue = float(cash_instance.cashvalue) - float(calclatvalue)
                if totalvalue >= 0:
                    cashlatvalue = totalvalue
                    cash_instance.cashvalue = totalvalue
                    quantity_instance.quantity = quantity_instance.quantity + int(quantity)
                    cash_instance.save()
                    quantity_instance.save()
                else:
                    display_message = "Insufficient cash to BUY"
            else:
                cash_instance, created = Cash.objects.get_or_create(username=request.POST['username'])
                quantity_instance, created = StockQuantity.objects.get_or_create(username=request.POST['username'], stockname=request.POST['stockname'])
                quantity = request.POST['quantity']
                calclatvalue = float(request.POST['lastprice']) * int(quantity)
                totalvalue = float(cash_instance.cashvalue) + float(calclatvalue)
                if int(quantity) <= quantity_instance.quantity:
                    cashlatvalue = totalvalue
                    cash_instance.cashvalue = totalvalue
                    quantity_instance.quantity = quantity_instance.quantity - int(quantity)
                    cash_instance.save()
                    quantity_instance.save()
                else:
                    display_message = "Insufficient stock to SELL"

            #return redirect('user')
            aapl_quantity_instance, created = StockQuantity.objects.get_or_create(username=request.POST['username'], stockname='AAPL')
            goog_quantity_instance, created = StockQuantity.objects.get_or_create(username=request.POST['username'], stockname='GOOG')
            latvalue = api['latestPrice'] * int(aapl_quantity_instance.quantity)
            latvalue1 = api1['latestPrice'] * int(goog_quantity_instance.quantity)
            return render(request, 'user.html', {'api':api,'api1':api1, 'latvalue':latvalue,'latvalue1':latvalue1,'a_quantity':aapl_quantity_instance.quantity,'g_quantity':goog_quantity_instance.quantity,'cashlatvalue':cash_instance.cashvalue, 'message':display_message})

        #quantity = request.POST['quantity']
        #latvalue = api['latestPrice'] * int(quantity)
        #latvalue1 = api1['latestPrice'] * int(quantity)

    else:
        addstock = Userstock.objects.all()
        cash_instance, created = Cash.objects.get_or_create(username=request.GET['username'])
        aapl_quantity_instance, created = StockQuantity.objects.get_or_create(username=request.GET['username'], stockname='AAPL')
        goog_quantity_instance, created = StockQuantity.objects.get_or_create(username=request.GET['username'], stockname='GOOG')
        latvalue = api['latestPrice'] * int(aapl_quantity_instance.quantity)
        latvalue1 = api1['latestPrice'] * int(goog_quantity_instance.quantity)
        return render(request, 'user.html', {'api':api,'api1':api1, 'latvalue':latvalue,'latvalue1':latvalue1,'addstock':addstock,'a_quantity':aapl_quantity_instance.quantity,'g_quantity':goog_quantity_instance.quantity,'cashlatvalue':cash_instance.cashvalue})
        