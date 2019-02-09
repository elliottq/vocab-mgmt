import unittest

from FetchList import FetchList

class TestFetchList(unittest.TestCase):

  def setUp(self):
    self.fetcher = FetchList()

  def test_formUrl_success(self):
    listId      = 1234
    listName    = 'foo'
    expectedUrl = 'http://spanishdict.com/lists/1234/foo'
    
    testUrl = self.fetcher.formUrl(listId, listName)
    self.assertEqual(expectedUrl,testUrl)

  def test_getList_200(self):
    testListId = '148070'
    testListName = 'verbs-followed-by-a'
    self.fetcher.getList(testListId, testListName)
    self.assertEqual(self.fetcher.page.status_code, 200)

if __name__ == '__main__':
  unittest.main()
