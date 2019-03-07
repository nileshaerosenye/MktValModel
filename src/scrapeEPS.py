# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

print ("Hello Spyder for Financial Analysis")

ticker="MSFT"
fName=ticker+".out"
fOut= open(fName,'w')


pageLoc="https://ycharts.com/companies/" + ticker + "/eps"
pageData = urlopen( pageLoc )

soup = BeautifulSoup(pageData)

i=0
rows = soup.find_all('tr')
for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    i+=1
    print(cols)
    fOut.write(" | ".join(cols))
    fOut.write("\n")
    
# close the file
fOut.close()