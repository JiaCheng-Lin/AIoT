from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

targetURL ="https://aiot.kaitechstudio.com/Login/" # 
ID = "ttu410606152"

driver = webdriver.Chrome() # ChromeDriver 88.0.4324.96 

driver.get(targetURL) 


element = driver.find_element_by_name("userID")    
element.send_keys(ID) 
driver.find_element_by_name("userID").send_keys(Keys.ENTER) 
# driver.find_element_by_xpath("/html/body/form/button").click()

preQ1Text = ''
preQ2Text = ''
while True:
    while True :
        Q1 = driver.find_element_by_id("Q1").get_attribute('value')
        if Q1 != '' and preQ1Text != Q1:
            preQ1Text = Q1
            break
    while True :
        Q2 = driver.find_element_by_id("Q2").get_attribute('value')
        if Q2 != '' and preQ2Text != Q2:
            preQ2Text = Q2
            break

    # print(Q1)
    # print(Q2)

    for i in range(1000):
        try:
            count = driver.find_element_by_id('succesCounter').text
        except:
            time.sleep(0.2)
        else:
            break
    
    print(count)
    if count == '200' :
        driver.refresh()
        break

    Q1Answer = ''
    for i in Q1 :
        if i.isalpha() or i.isnumeric() :
            Q1Answer += i
        elif i == '|' :
            Q1Answer += ID


    Q2Answer = ''
    a = ''
    b = ''
    sign = ''
    flag=  1
    for i in Q2 :
        if i.isnumeric() and flag==1 :
            a += i
        elif i.isnumeric() and flag==0 :
            b += i
        elif i == '+' :
            sign = '+'
            flag = 0
        elif i == '-' :
            sign = '-'
            flag = 0
        elif i == '*' :
            sign = '*'
            flag = 0
        elif i == '/' :
            sign = '/'
            flag = 0
        elif i == '%' :
            sign = '%'
            flag = 0

        if i == '=' :
            if(sign == '+'):
                Q2Answer = str(int(a) + int(b))
            elif(sign == '-') :
                Q2Answer = str(int(a) - int(b))
            elif(sign == '*') :
                Q2Answer = str(int(a) * int(b))
            elif(sign == '/') :
                Q2Answer = str(int(a) / int(b))
            elif(sign == '%') :
                Q2Answer = str(int(a) % int(b))

    print(Q1Answer)
    print(Q2Answer)

    for i in range(1000):
        try:
            driver.find_element_by_id("Q1a").send_keys(Q1Answer)
        except:
            time.sleep(0.2)
        else:
            break
    
    for i in range(1000):
        try:
            driver.find_element_by_id("Q2a").send_keys(Q2Answer)
        except:
            time.sleep(0.2)
        else:
            break

    for i in range(1000):
        try:
            driver.find_element_by_id("btnSubmit").click()
        except:
            time.sleep(0.2)
        else:
            break

    # time.sleep(1)