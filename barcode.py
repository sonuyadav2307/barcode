from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import pandas as pd
import xlrd
import xlsxwriter

df = pd.read_excel('barcode for webscraping.xlsx')

x = 1
list2 = []
fileloc = '/home/Sonu/Documents/Sonu Project/barcode for webscraping.xlsx'
workbook = xlrd.open_workbook(fileloc)
sheet = workbook.sheet_by_index(0)
    
driver = webdriver.Chrome(executable_path='/home/Sonu/Documents/Sonu/chromedriver')
driver.maximize_window()
for i in range(1771):

    driver.get('https://www.google.com/')
    driver.implicitly_wait(10)
    ele=driver.find_element_by_name('q')
    
    ele.send_keys(sheet.cell_value(x,0))
    x = x+1
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
    time.sleep(2)
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    time.sleep(2)
    if soup.find_all(class_='LC20lb DKV0Md'):
        
        print('true')
        
        list2.append('True')
        
    else:
        print('false')
        
        list2.append('false')
print(list2)        
wb = xlsxwriter.Workbook('divas.xlsx')
sheet = wb.add_worksheet()
writer = pd.ExcelWriter('divas.xlsx', engine='xlsxwriter')
writer.save()



    #dataframe Name and Age columns
df = pd.DataFrame({'barcode': list2})

    #Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('divas.xlsx', engine='xlsxwriter')

    #Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1', index=False)

    #Close the Pandas Excel writer and output the Excel file.
writer.save()

     
    

