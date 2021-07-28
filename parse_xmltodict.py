import xmltodict

#Get the XML File
stream = open('sample_xml.xml','r')

#Parse the XML file into an OrderedDictionary
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)