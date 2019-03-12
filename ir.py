from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('doc.xml')

docs = mydoc.getElementsByTagName('doc')

dictionary = {}

for doc in docs:
  docno = doc.getElementsByTagName('docno')
  dictionary[docno[0].firstChild.data] = doc.childNodes[1].data

print(dictionary)