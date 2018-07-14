
# coding: utf-8

# In[1]:


import bs4
import sys
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pdfkit
import os
import os.path
from os import path


# In[ ]:


url = raw_input()
#url.replace("/","\/")
uClient = uReq(url)
rsp = uClient.read()
uClient.close()
rsp_soup = soup(rsp,"html.parser")
items = rsp_soup.findAll(["head","article"])
title = rsp_soup.findAll("h1",{"class":"entry-title"})
ftitle = title[0].text.encode('utf8')
ftitle = ftitle.replace("\xe2\x80\x93","")
ftitle = ftitle.replace("|","")
#ftitle = ftitle.replace("|","")
print ftitle


# In[ ]:


x = str(items[0]) + str(items[1])
#html = items[i].prettify("utf-8")
stri = ftitle
stri += ".html"
if path.exists(stri):
    print "file already exists please delete it and try again"
else:
    with open(stri, "wb") as file:
        file.write(x)
    stre = ftitle
    stre += ".pdf"
    try:
        pdfkit.from_file(stri,stre)
    except:
        print "Stage 1"
    os.startfile(stre)

