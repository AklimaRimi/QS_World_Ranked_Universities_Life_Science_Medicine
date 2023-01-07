# Welcome To this Project. 
## Name : Top Universities according QS World Ranking for Life Science Medicine
# Motive
  1. Scrape Data from that [Website](https://www.topuniversities.com/university-rankings/university-subject-rankings/2022/life-sciences-medicine)
  
  2. Transform the data and 
  
  3. Create a Dashboard and find a story using the dataset.


# Data collection
 ***Data consist of every university rank, name , location, points from 2018 to 2022. Not only that, inside of each university, their latest information is also collected.***
 
You can run this code and collect  datasets. Thus you can build your own tableau Dashboard. To do this you have to follow these instructions.

  1. Download [Google Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.25/) from based on your device:  
     unzip the downloaded file and  collect the path where The Driver is saved.
  
  2. Install Python on your device from [Here](https://www.python.org/downloads/)
  
  3.  Download this [Folder](https://github.com/AklimaRimi/Data-Analysis---QS-World-Ranked-Universities-Life-Science-and-Medicine) file, unzip the downloaded file, And Rename the file name.
  
  4. (Optional) Create an environment for this project inside of the unzipped file. Click right button of mouse and select **Open in Terminal** and write these code one by one
  ``` 
  Set-ExecutionPolicy Unrestricted
  ```
  ```
  pip install virtualenv  
  or 
  pip3 install virtualenv
  ```
  ```
  virtualenv env
  ```
  ```
  env\Scripts\Activate.ps1
  ```
  
  5. Then in the terminal write
  ```
  pip install -r requirements.txt 
  or 
  pip3 install -r requirements.txt
  ```
     
  6. After Completing install packages, write
  ```
  cd Script
  ```
  Hit Enter 
  
  7. Then Write
  
  ```
  python Data_Creation_and_Transform.py 
  ```
  
  
  8. Hit Enter and Wait for 5 hours, Please Do not Touch Anything. 
  
  
  
  ***After Completeing all of works You'll get 5 Outputs in csv Formate***
  
  
  Unprocessed Data:
  
  1. `data1.csv`

  2. `data2.csv`

  3. `data3.csv`
    
  Processed or Transformed Data:
  
  1. `QS_World_Universities_Data_Life_Science_Medicine.csv`

  2. `Qs_World_Ranked_University_Name_Point_2018_to_2022_Life_Science_Medicine.csv`
  
  
  
## Data Transform

If you did everything according to the above instructions then Data Transformation has already been done already.\
In the data transformation a few things were completed..

  1. Dropping unnecessary columns.
  
  2. Clearing data from unwanted punctuation.
  
  3. Creating a new Row based on a particular column(s).
  
  4. Converting data type of columns.
  
  5. Splitting one column into two.
  
  6. Save Clear wanted dataset.
  
  
## Analysis and Stories
  1. Using '[QS_World_Universities_Data_Life_Science_Medicine.csv](https://github.com/AklimaRimi/Data-Analysis---QS-World-Ranked-Universities-Life-Science-and-Medicine-/blob/main/Output/QS_World_Universities_Data_Life_Science_Medicine.csv)' dataset I've created [This Dashboard](https://public.tableau.com/app/profile/aklima.akter.rimi/viz/WorldRankedUniversityLifeScienceandMedicine/Dashboard1) 
      with [That Story](https://public.tableau.com/app/profile/aklima.akter.rimi/viz/StoryofQSWorldRankedUniversitiesin2022/Story1)
      
      ![](https://github.com/AklimaRimi/Data-Analysis---QS-World-Ranked-Universities-Life-Science-and-Medicine-/blob/main/Tableau_Dashboard/Dashboard1.png)
      
      ## Story or Findings:
        1. USA, UK, Australia still open for Bachelor admissions.
        2. Sydney and Monash University have the largest number of international students. Due to better living opportunities,
          job benefits, scholarships and deductible expenses.
        3. More faculty or more students does not improve a university's score. Improved by education.
        4. The USA offers the best General programs in the world. Always open for International students.
        5. Most top universities have an average of 55-70 H-Index citations.
        6. There are very few opportunities for students who want to do Masters in Europe.
         
  2. Based on '[Qs_World_Ranked_University_Name_Point_2018_to_2022_Life_Science_Medicine.csv](https://github.com/AklimaRimi/Data-Analysis---QS-World-Ranked-Universities-Life-Science-and-Medicine-/blob/main/Output/Qs_World_Ranked_University_Name_Point_2018_to_2022_Life_Science_Medicine.csv)' dataset another [Dashboard](https://public.tableau.com/app/profile/aklima.akter.rimi/viz/UniversityRankandPointsover5years/Dashboard1) has been created with [Story](https://public.tableau.com/app/profile/aklima.akter.rimi/viz/Storyoveryears/Story1)
  
      ![](https://github.com/AklimaRimi/Data-Analysis---QS-World-Ranked-Universities-Life-Science-and-Medicine-/blob/main/Tableau_Dashboard/Dashboard2.png)  
  
      ## Story or Findings:
        1. We can see that even on average Canada has the Most good ranked Universities.
        2. In 2018 Harverd was the 1st ranked university among all Universities in the world.
        3. China has numerous best universities in Asia.
        4. The better the point, the better the rank.
        5. Harvard, Oxford universities retain their ranks as in the past, some universities like Duke University have their ranks changing over the years.


# Conclusion
This entire project is for `Data Analysis`. 

It's suitable for beginners. This project can be executed by anyone. 

Due to the webdriver's extensive website trip, data collection takes a lengthy time.

Data might be changed over time.
