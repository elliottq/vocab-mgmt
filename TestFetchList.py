import unittest

from FetchList import FetchList

class TestFetchList(unittest.TestCase):

  def setUp(self):
    self.testListId = '148070'
    self.testListName = 'verbs-followed-by-a'
    self.exampleId      = 1234
    self.exampleName    = 'foo'
    self.fetcher = FetchList(self.testListId, self.testListName)

  def test_formUrl_success(self):
    expectedUrl = 'http://spanishdict.com/lists/1234/foo'
    
    testUrl = self.fetcher.formUrl(self.exampleId, self.exampleName)
    self.assertEqual(expectedUrl,testUrl)

  def test_getList_200(self):
    self.fetcher.getList()
    self.assertEqual(self.fetcher.page.status_code, 200)

  def test_getNonExistentList_ExpectException(self):
    fetchNothing = FetchList("12", "list that does not exist")
    self.assertRaises(Exception, fetchNothing.getList)

  def test_processTestPage_success(self):
    spanishExpected = ['bajar', 'acercarse']
    englishExpected = ['to go down', 'to approach']

    self.fetcher = FetchList(self.testListId, self.testListName)
    self.fetcher.extractVocabulary()

    self.assertEqual(spanishExpected, self.fetcher.spanishVocab)
    self.assertEqual(englishExpected, self.fetcher.englishVocab)

if __name__ == '__main__':
  unittest.main()
