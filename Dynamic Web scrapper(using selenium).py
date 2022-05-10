#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

s=Service(r"D:\Users\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://www.amazon.in/Redmi-Horizon-Qualcomm%C2%AE-SnapdragonTM-Included/dp/B09QSBXK96/?_encoding=UTF8&pd_rd_w=rdztZ&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_r=PHZ2ZWS8NA1FEE7HP8K2&pd_rd_r=67046156-a2a9-4b26-83b5-ed63fff0c786&pd_rd_wg=o0I2X&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
driver.get(url)
time.sleep(5)

html = driver.page_source


soup = BeautifulSoup(html, "html.parser")
p_name = soup.find('span', class_ = 'a-size-large product-title-word-break')
if p_name!=None:
    print(p_name.text)
                     
elif p_name==None:
    print('error')
p_price = soup.find('span', class_ = 'a-offscreen')
if p_price!=None:
    print(p_price.text)
                     
elif p_price==None:
    print('error')
    
   

driver.close() 


# In[ ]:





# In[ ]:




