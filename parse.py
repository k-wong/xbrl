#e = xml.etree.ElementTree.parse('aapl-20150328.xml').getroot()

#for atype in e.findall('type'):
    #print(atype.get('foobar'))

from xml.dom import minidom

xmldoc = minidom.parse('aapl-20150328.xml')
print(xmldoc)
itemlist = xmldoc.getElementsByTagName('us-gaap:AccountsPayableCurrent')
for s in itemlist:
	print (dir(s))


#print(len(xmldoc))
#print(itemlist[0].attributes['name'].value)
#for s in itemlist:
    #print(s.attributes['name'].value)


# python-xbrl ----------------------------------------------------------------------------------------------------
#from xbrl import XBRLParser, GAAP, GAAPSerializer
#xbrl_parser = XBRLParser()
#xbrl = xbrl_parser.parse(file("aapl-20150328.xml"))
#gaap_obj = xbrl_parser.parseGAAP(xbrl, doc_date="20150328", doc_type="10-Q", context="current", ignore_errors=0)


#<us-gaap:AccountsPayableCurrent contextRef="eol_PE2035----1510-Q0005_STD_0_20150328_0" decimals="-6" id="id_4752856_746BA5DF-ACE9-4E9F-B0D2-C0D17A2FFDE0_1_19" unitRef="iso4217_USD">23159000000</us-gaap:AccountsPayableCurrent>

#<us-gaap:AccountsPayableCurrent contextRef="eol_PE2035----1510-Q0005_STD_0_20140927_0" decimals="-6" id="id_4752856_746BA5DF-ACE9-4E9F-B0D2-C0D17A2FFDE0_2_19" unitRef="iso4217_USD">30196000000</us-gaap:AccountsPayableCurrent>
