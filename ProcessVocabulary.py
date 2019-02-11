import os
from shutil import copyfile

from FetchList import FetchList

class ProcessVocabulary:

  def __init__(self, vocabulary, fileName, delimiter = '\t'):
    self.dropboxPath = '/home/sean/Dropbox/Apps/Flashcards Deluxe/'
    self.vocabulary = vocabulary
    self.fileName = fileName
    self.delimiter = delimiter

    self.curPath = str(os.path.abspath(os.curdir))

  def savePairs(self):
     dstDir  = self.curPath + '/resource/'
     fileLoc = dstDir + self.fileName
     print "Writing pairs to ", fileLoc
     with open(fileLoc, 'w') as myFile:
       for self.spanish, self.english in self.vocabulary:
         myFile.write(self.spanish.encode("UTF-8") + self.delimiter + self.english.encode("UTF-8"))
         myFile.write("\n")

  def moveToDropBox(self):
    print "Final move to DropBox..."
    finalFileSrc = self.curPath + '/resource/'  + self.fileName
    finalFileDst = self.dropboxPath + self.fileName
    copyfile(finalFileSrc, finalFileDst)



if __name__ == '__main__':
    listId = '146312'
    listName = 'las-palabras'
    fileName = 'test.csv'
        
    fetcher = FetchList(listId,listName)
    fetcher.extractVocabulary()

    processor = ProcessVocabulary(fetcher.getPairs(), fileName)
    processor.savePairs()
    processor.moveToDropBox()
