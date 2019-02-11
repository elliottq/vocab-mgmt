import unittest
import filecmp

from FetchList import FetchList
from ProcessVocabulary import ProcessVocabulary

class TestProcessVocabulary(unittest.TestCase):

  def test_writeTestList_success(self):
    fileName = 'tmpPairs.csv'
    basePath = '/home/sean/code/vocab-mgmt/resource/'
    fetcher = FetchList('148070', 'verbs-followed-by-a')
    fetcher.extractVocabulary()
    
    processor = ProcessVocabulary(fetcher.getPairs(), fileName)
    processor.savePairs()
    self.assertTrue(filecmp.cmp(basePath + fileName, basePath + 'testPairs.csv'))
    

if __name__ == '__main__':
  unittest.main()
