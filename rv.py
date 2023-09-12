import requests

print("Requests version:", requests.__version__)


url = "http://google.com/"
url_get = requests.get(url)
#print(url_get.text)

#print(requests.get("")) # Insert raw github URL to python script once pushed
