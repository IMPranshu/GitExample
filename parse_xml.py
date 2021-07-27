#import xml.etree.ElementTree as ET
from lxml import etree as ET

#Get the XML File data
stream = open('sample_xml.xml','r')

#Parse the data into an ElementTree Object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElementTree
root = xml.getroot()

#Iterate through each child of the root element
for e in root:

    #Print the stringified version of the element
    print(ET.tostring(e))
    print("")
    
    #Print the 'Id' attribute of the Element objeect
    print(e.get("Id"))