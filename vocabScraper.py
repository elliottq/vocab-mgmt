from bs4 import BeautifulSoup

srcFile = '/home/sean/code/palabras.html'
dstFile = '/home/sean/code/vocabulary.csv'
delimiter = '\t'

# Read word web page from file
# Parse html with Beautiful Soup
print("Read the web page from text...")
with open(srcFile, 'r') as myFile:
    page = myFile.read()
soup = BeautifulSoup(page, 'html.parser')

# Scan for spanish words and english translations
print("Get the vocabulary...")
spanishList = soup.find_all("span","source--1F2Ol")
englishList = soup.find_all("span","translation--2F5zL")

# Write the pairs to file, delimited
with open(dstFile, 'w') as myFile:
    for spanishWord,englishWord in zip(spanishList,englishList):
        myFile.write(str(spanishWord) + delimiter + str(englishWord))
