import requests

#### DELETE THIS
#url='https://www.spanishdict.com/lists/146312/las-palabras'
#
#print("Get the web page...")
#page = requests.get(url)
#
#fileName='palabras.html'
#
#with open(fileName,'w') as dst:
#  dst.write(page.content)


class FetchList:

  def __init__(self):
    self.domain   = 'http://spanishdict.com/lists/'
    self.dstName  = 'palabras.html'
    self.page     = None

  def getList(self, listId, listName):
    url = self.formUrl(listId,listName)
    self.page = requests.get(url)

  def formUrl(self, listId, listName):
    return self.domain + str(listId) + '/' + str(listName)

  def saveListWebPage():
    with open(self.dstName, 'w') as dst:
      dst.write(self.page.content)

