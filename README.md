Name: Swarna Rekha Nadaradjamourty

Project title: Stock-Portfolio
Languages used: HTML, CSS, Python, Django
Code Editor: Visual studio code 
Repository: Github

Project description: Stock-Portfolio application is used to buy and sell shares. The new user have to create account by filling the sign up form and sign in with the login credentials. Once the user logged in, the user will be given with a default amount. With the sufficient amount the user can buy any number of shares. The user can also sell shares he/she owns. We can also search for the different tickers to find their latest updates.

Project details: The project consists of: 
HTML page - home.html, user.html, search.html, base.html and login.html
CSS page - base.css and Bootstrap
Python page - models.py, views.py, admin.py, forms.py and urls.py
Django project - stock_market
Django app - stocks, accounts
Django models - Userstock, Cash and StockQuantity

Future improvements:
1. Can buy any interest stocks.
2. Direct bank account transaction will be included.
3. User graph will be included.

Installation and Setup Instructions for the project.
1. Clone this repository:
    $ git clone https://github.com/Rekha1912/StockMarket
    $ cd StockMarket
2. Install:
    $ pipenv install django==3.0
    $ pipenv shell
3. To migrate:
    $ python manage.py migrate
4. To Start Server:
    $ python manage.py runserver
5. To Visit App:
    http://127.0.0.1:8000/

Heroku deployed URL - https://boiling-stream-78496.herokuapp.com/



