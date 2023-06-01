#!user/bin/env pythons3

import requests
 
x = requests.get('https://www.google.com')

if x.status_code == 200:
    print('yah!')
else:
    print("uh oh!")