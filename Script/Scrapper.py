from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException
import argparse
import pandas as pd
import string



def ScrapData1():
  datas = []
  rank_ =  []
  uni =[]
  loc = []
  avg = []
  adm = []
  student_info =[]
  uni_rank = []
  uni_point = []
  row =[]
  links = []
  data=[]
  
  print('''\n\n\n\n\n==========================>>>Take a Deep Sleep , It\'ll take 4 hours to set All things :)<<<================\n\n\n\n\n\n
        =================================>>>AND Do not Touch or Minimize anything  <<<============\n\n\n\n\n\n 
        =========================================>>>Best Of Luck <<<============================\n\n\n\n\n''')
  
  path =r'https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/life-sciences-medicine'
  
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get(path)
  driver.refresh()
  time.sleep(5)
  
  for i in range(50):
          rows = driver.find_element(By.ID,"ranking-data-load")
          row_ind = rows.find_elements(By.XPATH,"//div[contains(@class,'row') and contains(@class , 'ind ')]")
          
          for x in row_ind:
                  row.append(x.text)
                  links.append(x.find_element(By.TAG_NAME,'a').get_attribute('href'))
          
          next_button  = driver.find_element(By.XPATH,'//a[contains(@class,"page-link") and contains(@class,"next")]')
          next_button.click()
          time.sleep(2)

  for i in range(len(row)):
          print('==========>    ',i)
          rank_.append(row[i].split('\n')[0])
          uni.append(row[i].split('\n')[1])
          loc.append(row[i].split('\n')[2])
          if len(row[i].split('\n'))== 4:
                  avg.append(row[i].split('\n')[3])
          else:
                  avg.append('-')
          
          driver.get(links[i])
          
          time.sleep(2)
          try:
                  admission = driver.find_elements(By.CLASS_NAME,"univ-subsection-full-width-parent")
                  admm ={}
                  for ind in admission:
                          admm[ind.text.split('\n')[0]] = ind.text.split('\n')[1:]

                  if len(admm) > 0:
                          adm.append(admm)  
                  else:
                          adm.append(None)
          except NoSuchElementException:
                  adm.append(None)
          
          try:
                  
                  clickable = driver.find_element(By.XPATH,"//a[contains(text(),'Students & Staff')]")

                  actions = ActionChains(driver)
                  time.sleep(2)
                  actions.click(clickable)
                  actions.perform()
                  time.sleep(2)  
                  
                  student = driver.find_element(By.XPATH,"//div[contains(@class,'tab-pane') and contains(@class,'fade') and contains(@class,'active') and contains(@class,'show')]")
                  print('\n\n\n')
                  student_info.append(student.text.split('\n'))
          
          except NoSuchElementException:  #spelling error making this code not work as expected
                  student_info.append(None)
          #rnk-list-wrp pos-relative
          try:
                  rank = driver.find_element(By.XPATH,'//div[contains(@class,"rnk-list-wrp") and contains(@class,"pos-relative")]')
                  print('\n\n\n')
                  uni_rank.append(rank.text.split('\n'))
          except NoSuchElementException:  #spelling error making this code not work as expected
                  uni_rank.append(None)

          try:
                  point = driver.find_element(By.CLASS_NAME,"criteria-wrap")
                  print('\n\n\n')
                  uni_point.append(point.text.split('\n'))
          except NoSuchElementException:
                  uni_point.append(None)  
            
  cols = ['Rank','University Name','Location','Point','Admission-Info','Local-Foreiner','Rank Details','Point-Details']  

  for i in range(len(uni)):
          data.append([rank_[i],uni[i],loc[i],avg[i],adm[i],student_info[i],uni_rank[i],uni_point[i]])

  data = pd.DataFrame(data,columns=cols)
  data.to_csv('data1.csv')
  driver.close()
  return 

def ScrapData2():
  
  datas = []
  uni =[]
  loc = []
  avg = []
  adm = []
  student_info =[]
  uni_rank = []
  uni_point = []
  y = []
  data = []

  driver = webdriver.Chrome(arg.ChromePath+"\chromedriver.exe")
  driver.maximize_window()
  for year in [2018,2019,2020,2021,2022]:
    path =f'https://www.topuniversities.com/university-rankings/university-subject-rankings/{year}/life-sciences-medicine'
    driver.get(path)
    time.sleep(5)
    print('Year - ',year)
    for i in range(35):
        rows = driver.find_element(By.ID,"ranking-data-load")
        row_ind = rows.find_elements(By.XPATH,"//div[contains(@class,'row') and contains(@class , 'ind ')]")

        for x in row_ind:
          datas.append(x.text)

        next_button  = driver.find_element(By.XPATH,'//a[contains(@class,"page-link") and contains(@class,"next")]')
        next_button.click()
        time.sleep(2)

    for j in datas:
      y.append(year)
      uni_rank.append(j.split('\n')[0])
      uni.append(j.split('\n')[1])
      loc.append(j.split('\n')[2])
      if len(j.split('\n')) == 4:
        avg.append(j.split('\n')[3])
      else:
        avg.append(None)
  
  for i in range(len(uni)):
    data.append([y[i],uni_rank[i],uni[i],loc[i],avg[i]])

  d = pd.DataFrame(data,columns=['Year','Rank','Name','Location','Point'])

  d.to_csv('data2.csv')

  driver.close()
  return

def ScrapData3():
  
    datas = []
    uni =[]
    loc = []
    avg = []
    adm = []
    student_info =[]
    uni_rank = []
    uni_point = []
    y = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    data = []
    
    path =f'https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/life-sciences-medicine'

    driver = webdriver.Chrome(arg.ChromePath+"\chromedriver.exe")
    driver.maximize_window()
    driver.get(path)
    time.sleep(10)

    action = ActionChains(driver)
    button = driver.find_element(By.XPATH,'//*[@id="block-tu-d8-content"]/div/article/div/div/div[3]/div/div[1]/div/div[1]/div/div/ul/li[2]/a')
    action.click(button).perform()

    for i in range(40):
      rows = driver.find_element(By.XPATH,'//*[@id="ranking-data-load_ind"]')
      row_ind = rows.find_elements(By.XPATH,'//div[contains(@class,"row") and contains(@class,"ind-row")]')


      for x in row_ind:
          datas.append(x.text)

      time.sleep(10)
      next_button  = driver.find_element(By.XPATH,'//a[contains(@class,"page-link") and contains(@class,"next")]').click()
      time.sleep(5)
        
    for j in range(len(datas)):
        one.append(datas[j].split('\n')[1])
        two.append(datas[j].split('\n')[3])
        three.append(datas[j].split('\n')[4])
        four.append(datas[j].split('\n')[5])
        five.append(datas[j].split('\n')[6])
        six.append(datas[j].split('\n')[7])
        seven.append(datas[j].split('\n')[8])
    
    for i in range(len(one)):
        data.append([one[i],two[i],three[i],four[i],five[i],six[i],seven[i]])

    d = pd.DataFrame(data,columns=['Name','Overall Score','International Research Network','H-index Citations','Citations per Paper','Academic Reputaion','Employer Reputation'])

    d.to_csv('data3.csv')

    print(d.head())

    driver.close()
    return 
