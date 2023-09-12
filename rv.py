import requests

print("Requests version:", requests.__version__)


url = "http://google.com/"
url_get = requests.get(url)
print(url_get.text)

print(requests.get("https://raw.githubusercontent.com/anjelica-m/C404Lab1/master/rv.py")) # Insert raw github URL to python script once pushed
