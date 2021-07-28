import xmltodict

stream = open('sample_xml.xml','r')

xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)