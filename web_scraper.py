# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.ticketweb.com/event/sunday-spotlight-with-track-45-the-bluebird-cafe-tickets/11405155"
# headers = {
#     #'host': 'www.ticketweb.com',
#     'user-agent': 'PostmanRuntime/7.28.4',
# }
# page = requests.get(URL, headers=headers)

# soup = BeautifulSoup(page.content, "html5lib")
# #print(soup.p)

# event_info_section = soup.find(id="eventInfo")
# status_section = event_info_section.find_all("div", class_="section-status")

# for c in status_section:
#     print(c)
# # print(len(list(sections.children)))
# # for s in sections.children:
# #     print(s.get('id'))

# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
from email.message import EmailMessage
from smtplib import SMTP

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'justinc328@gmail.com'
    password = 'wecjrkfpwckjiiyx'
    msg['from'] = user

    server = SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

# setting the URL you want to monitor
url = Request('https://www.ticketweb.com/event/sunday-spotlight-with-track-45-the-bluebird-cafe-tickets/11405155',
			headers={'User-Agent': 'PostmanRuntime/7.28.4'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")

time.sleep(10)
while True:
    try:
        # perform the get request and store it in a var
        response = urlopen(url).read()

        # create a hash
        currentHash = hashlib.sha224(response).hexdigest()

        # wait for 30 seconds
        time.sleep(30)

        # perform the get request
        response = urlopen(url).read()

        # create a new hash
        newHash = hashlib.sha224(response).hexdigest()

        # check if new hash is same as the previous hash
        if newHash == currentHash:

            continue

        # if something changed in the hashes
        else:
            # notify
            print("something changed")
            email_alert('Somethings Changed', 'GO GO GO', 'justinc328@gmail.com, jenniemac2020@gmail.com')

            # again read the website
            response = urlopen(url).read()

            # create a hash
            currentHash = hashlib.sha224(response).hexdigest()

            # wait for 30 seconds
            time.sleep(30)
            continue

    # To handle exceptions
    except Exception as e:
        print("error")

