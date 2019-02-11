import requests
from bs4 import BeautifulSoup

class FetchList:

  def __init__(self, listId, listName):
    self.domain   = 'http://spanishdict.com/lists/'
    self.dstName  = 'palabras.html'
    self.page     = None
    self.spanishVocab = []
    self.englishVocab = []

    self.listId = listId
    self.listName = listName

  """
    Helper function to make GET request
  """
  def getList(self):
    url = self.formUrl(self.listId,self.listName)
    print "Fetching: ", url
    self.page = requests.get(url)
    if self.page.status_code != 200:
      raise Exception("Could not successfully retrieve web page")

  """
    Helper function to form URL
  """
  def formUrl(self, listId, listName):
    return self.domain + str(listId) + '/' + str(listName)

  def getPairs(self):
    return zip(self.spanishVocab, self.englishVocab)

  """
    Main method to retrieve and parse vocabulary web page
  """
  def extractVocabulary(self):
    self.getList()
    
    soup = BeautifulSoup(self.page.content, 'html.parser')
    self.spanishVocab = [ word.string for word in soup.find_all("span","source--1F2Ol")] 
    self.englishVocab = [ word.string for word in soup.find_all("span","translation--2F5zL")]
