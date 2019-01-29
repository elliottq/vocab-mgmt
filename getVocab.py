import requests

url='https://www.spanishdict.com/lists/146312/las-palabras'

print("Get the web page...")
page = requests.get(url)

fileName='palabras.html'
with open(fileName,'w') as dst:
  dst.write(page.content)
