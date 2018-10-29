#import the library used to query a website
from urllib.request import urlopen
#import the library used to query a website
from urllib.request import urlopen

#specify the url
wiki = "https://en.wikipedia.org/wiki/Gal_Gadot"
#specify the url
wiki = "https://en.wikipedia.org/wiki/Gal_Gadot"

#Query the website and return the html to the variable 'page'
page = urlopen(wiki)
#Query the website and return the html to the variable 'page'
page = urlopen(wiki)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

all_tables=soup.find_all('table')
all_tables=soup.find_all('table')

right_table=soup.find('table', class_='wikitable sortable')
right_table=soup.find('table', class_='wikitable sortable')

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==5: #Only extract table body not heading
        temp = cells[0].find(text=True)
        A.append(temp)
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
    if len(cells)==4:
        A.append(temp)
        B.append(cells[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==5: #Only extract table body not heading
        temp = cells[0].find(text=True)
        A.append(temp)
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
    if len(cells)==4:
        A.append(temp)
        B.append(cells[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D

​
