from xml.dom import minidom

class TermDict():
  def __init__(self, term, docList, df):
    self.term = term
    self.docList = docList
    self.df = df
    
  def __str__(self):
    return "Term: " + self.term + ", Documents: " + self.docList + ", df: " + self.df

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
termsDict = []

for term in terms:
  docList = {}
  for key in dictionary:
    docArr = dictionary.get(key).split()
    counter = docArr.count(term)
    if (counter > 0):
      docList[key] = counter
  termDict = TermDict(term, docList, len(docList))
  termsDict.append(termDict)
