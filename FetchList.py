import requests

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

