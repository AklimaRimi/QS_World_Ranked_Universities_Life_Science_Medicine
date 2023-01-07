## Import Dependencies
import time
import pandas as pd
import string
import numpy as np
from Scrapper import *


## Transforming Collected
def Transform():
  val = []
  data1 = pd.read_csv('data1.csv')
  data2 = pd.read_csv('data2.csv')
  data3 = pd.read_csv('data3.csv')

  data2 = data2.drop(columns = ['Unnamed: 0'])
  print(data2.head(5))

  def splitting(x):
    # print(x)
    if ',' in x:
      return x.split(',')[0],x.split(',')[1]
    else:
      return '-',x

  data2['City'] = data2['Location'].apply(lambda x: splitting(x)[0])
  data2['Country'] = data2['Location'].apply(lambda x: splitting(x)[1])

  data2 = data2.drop(columns = ['Location'])

  for i in range(len(data2['Country'])):
    if data2['Country'][i] == ' China (Mainland)':
        data2['Country'][i] = 'China'
      
  for i in range(len(data2['Country'])):
    if data2['Country'][i] == ' Hong Kong SAR':
      data2['Country'][i] = 'Hong Kong'
      
  data2['Rank'] = data2['Rank'].apply(lambda x: x.replace('=',''))
  data2['Rank'] = data2['Rank'].astype('int')

  data1['City'] = data1['Location'].apply(lambda x: splitting(x)[0])
  data1['Country'] = data1['Location'].apply(lambda x: splitting(x)[1])
  data1 = data1.drop(columns = ['Unnamed: 0','Location'])

  data1['Admission-Going-On'] = data1['Admission-Info'].apply(lambda x: 0 if pd.isna(x) else 1)
  data1['Internationally-Allowed'] =  data1['Local-Foreiner'].apply(lambda x: 0 if pd.isna(x) else 1)


  p = data1['Local-Foreiner']
  for i in range(len(p)):
    if pd.isna(p[i]) == False:

      if len(p[i]) > 230:
        p[i] = p[i][:230]
      elif len(p[i]) ==  230:
        p[i] = p[i]
      else:
        p[i] = 'None'
    else:
      p[i] = 'None'
      
  for i in range(len(p)):
    if pd.isna(p[i]) == False:
      p[i] = p[i].split("',")
      
  for i in range(len(p)):

    for j in range(len(p[i])):
      p[i][j] = p[i][j].translate(str.maketrans('', '', string.punctuation)) 
      
      
  cols = ['Total students','International students','Total faculty staff']
  
  for i in p:
    if len(i) == 17:
      val.append([i[1],i[7],i[13]])
    else:
      val.append([0,0,0])

  data1 = data1.drop(columns = ['Local-Foreiner','Rank Details',	'Point-Details'])

  number = pd.DataFrame(val,columns = cols)
  data1 = data1.merge(number,left_index=True, right_index=True)
  data1['Admission-Info'] = data1['Admission-Info'].apply(lambda x: '0' if pd.isna(x) else x)
  data1 = data1.drop(columns = ['Admission-Info'])
  
  for i in range(len(data1['Point'])):
    if data1['Point'][i] == '-':
      data1['Point'][i] = 0

  for i in range(len(data3)):
    if data3['International Research Network'][i] == 'QS Stars':
      data3['International Research Network'][i] = 100

  for j in range(len(data3['Overall Score'])):
      data3['Overall Score'][j] = data3['Overall Score'][j].translate(str.maketrans('', '', string.punctuation))
      
  data3 = data3.drop(columns = ['Unnamed: 0'])
  data1['Rank'] = data1['Rank'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    
  data3['Overall Score']  = data3['Overall Score'].astype('float')
  data3['International Research Network']  = data3['International Research Network'].astype('float')

  data1 =  data1.merge(data3, right_on = 'Name',left_on = 'University Name')
  data1 = data1.drop(columns = ['Name','Overall Score'])
  
  data1.to_csv('QS_World_Universities_Data_Life_Science_Medicine.csv',index = False)
  data2.to_csv('Qs_World_Ranked_University_Name_Point_2018_to_2022_Life_Science_Medicine.csv',index = False)
  return


  
if __name__ == '__main__':
  ScrapData1()
  ScrapData2()
  ScrapData3()
  Transform()
  
