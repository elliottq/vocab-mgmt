import os

from FetchList import FetchList

class ProcessVocabulary:

  def __init__(self, vocabulary, fileName, delimiter = '\t'):
    self.vocabulary = vocabulary
    self.fileName = fileName
    self.delimiter = delimiter

  def savePairs(self):
     curpath = os.path.abspath(os.curdir)
     dstDir  = str(curpath) + '/resource/'
     fileLoc = dstDir + self.fileName
     print "Writing pairs to ", fileLoc
     with open(fileLoc, 'w') as myFile:
       for self.spanish, self.english in self.vocabulary:
         myFile.write(self.spanish.encode("UTF-8") + self.delimiter + self.english.encode("UTF-8"))
         myFile.write("\n")
