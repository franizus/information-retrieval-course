from xml.dom import minidom

class MyStruct():
    def __init__(self, term, df):
        self.term = term
        self.docList = []
        self.df = df

# parse an xml file by name
mydoc = minidom.parse('doc.xml')

docs = mydoc.getElementsByTagName('doc')

dictionary = {}
terms = []

for doc in docs:
  docno = doc.getElementsByTagName('docno')
  docData = str(doc.childNodes[1].data).replace("'", " ").lower()
  dictionary[docno[0].firstChild.data] = docData
  for term in docData.split():
    terms.append(term)

terms = list(set(terms))
terms.sort()
termsDict = {}


for term in terms:
  docList = []
  for key in dictionary:
    if term in dictionary.get(key):
      docList.append(key)
  termsDict[term] = docList

print(termsDict)