# encoding: utf-8

import xml.dom.minidom
import urllib2

zwskey = "X1-ZWz1h1dp68sk5n_6ed93"


def getaddressdata(address, city):
    escad = address.replace(' ', '+')
    url = 'http://www.zillow.com/webservice/GetDeepSearchResults.htm?'
    url += 'zws-id=%s&address=%s&citystatezip=%s' % (zwskey, escad, city)
    doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
    code = doc.getElementsByTagName('code')[0].firstChild.data
    if code != '0':
        return None

    if 1:
        zipcode = doc.getElementsByTagName('zipcode')[0].firstChild.data
        use = doc.getElementsByTagName('useCode')[0].firstChild.data
        year = doc.getElementsByTagName('yearBuilt')[0].firstChild.data
        sqft = doc.getElementsByTagName('finishedSqFt')[0].firstChild.data
        bath = doc.getElementsByTagName('bathrooms')[0].firstChild.data
        bed = doc.getElementsByTagName('bedrooms')[0].firstChild.data
        rooms = bath + bed + 1  # doc.getElementsByTagName('totalRooms')[0].firstChild.data
        price = doc.getElementsByTagName('amount')[0].firstChild.data
    else:
        return None

    return (zipcode, use, int(year), float(bath), int(bed), int(rooms), price)


def getpricelist():
    l1 = []
    for line in file('addresslist.txt'):
        try:
            data = getaddressdata(line.strip(), 'Cambridge,MA')
        except Exception as e:
            print e
            continue
        l1.append(data)
    return l1


"""
house data columns
zipcode, usecode, build year, bathrooms, bedrooms, rooms, price
"""
house_data = [
    ["02140", "MultiFamily2To4", 1880, 1.0, 1, 1, "597560"],
    ["02138", "SingleFamily", 1847, 1.5, 2, 1, "1050763"],
    ["02139", "Triplex", 1884, 3.5, 5, 1, "1978160"],
    ["02138", "Condominium", 1925, 1.0, 1, 1, "831430"],
    ["02138", "MultiFamily2To4", 1910, 1.0, 1, 1, "515747"],
    ["02140", "Duplex", 1894, 3.5, 3, 1, "1456215"],
    ["02138", "Apartment", 1924, 1.5, 2, 1, "1730198"],
    ["02138", "SingleFamily", 1925, 3.0, 3, 1, "4556607"],
    ["02140", "SingleFamily", 1894, 2.5, 4, 1, "2572028"],
    ["02140", "SingleFamily", 1894, 2.5, 4, 1, "2491829"],
    ["02138", "SingleFamily", 1956, 3.0, 4, 1, "1673148"],
    ["02140", "SingleFamily", 1899, 1.5, 3, 1, "941178"],
    ["02138", "MultiFamily2To4", 1927, 1.0, 2, 1, "1187791"],
    ["02140", "Condominium", 1920, 1.0, 2, 1, "733374"],
    ["02138", "Condominium", 1900, 1.0, 2, 1, "754285"],
    ["02139", "Condominium", 1987, 1.5, 2, 1, "1052972"],
    ["02139", "Duplex", 1894, 2.5, 2, 1, "1129715"],
    ["02139", "Condominium", 1820, 2.5, 3, 1, "1145998"],
    ["02139", "MultiFamily2To4", 1873, 3.0, 3, 1, "1435767"],
    ["02139", "Duplex", 1854, 2.5, 4, 1, "1230853"],
    ["02139", "SingleFamily", 1873, 1.0, 1, 1, "1177462"],
    ["02138", "Townhouse", 1909, 2.0, 3, 1, "1791058"],
    ["02139", "SingleFamily", 1854, 1.0, 2, 1, "1706370"],
    ["02138", "MultiFamily2To4", 1922, 1.0, 1, 1, "1145752"],
    ["02138", "Condominium", 1985, 2.0, 1, 1, "1442654"],
    ["02141", "SingleFamily", 1984, 2.0, 3, 1, "1049906"],
    ["02139", "Condominium", 1996, 1.5, 3, 1, "491078"],
    ["02138", "Condominium", 1880, 1.5, 3, 1, "1099960"],
    ["02139", "MultiFamily2To4", 2015, 3.0, 4, 1, "1755153"],
    ["02139", "Duplex", 1854, 3.5, 6, 1, "1749147"],
    ["02139", "SingleFamily", 1873, 1.5, 2, 1, "1119380"],
    ["02138", "SingleFamily", 2009, 3.5, 4, 1, "4652725"],
    ["02138", "SingleFamily", 1948, 1.5, 3, 1, "759404"],
    ["02140", "SingleFamily", 1908, 1.5, 3, 1, "1769044"],
    ["02138", "Condominium", 1932, 2.0, 5, 1, "879743"],
    ["02139", "Condominium", 1903, 1.0, 3, 1, "959614"],
    ["02139", "MultiFamily2To4", 1903, 2.0, 3, 1, "2143843"],
    ["02140", "MultiFamily2To4", 1988, 1.5, 2, 1, "784671"],
    ["02139", "Duplex", 1854, 3.5, 6, 1, "1749147"],
    ["02138", "Condominium", 1923, 1.0, 2, 1, "806920"]]


def main():
    from treepredict import buildtree, entropy, drawtree
    # house_data = getpricelist()
    # print house_data
    print 'build tree'
    t = buildtree(house_data, scoref=entropy)
    print 'draw tree'
    drawtree(t, 'house_price_tree.jpeg')


if __name__ == '__main__':
    main()