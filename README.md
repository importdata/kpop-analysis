# Kpop-Analysis

## Intro 
- As someone who was born and raised in South Korea, I grew up listening to K-pop. Over the years, K-pop became a global phenomenon and it still blows my mind how popular it became.
- So, I thought it would be cool to analyze K-pop using machine learning to explore interesting insights. Thank you Chanin (aka. Data Professor) for the idea!

## Data Collection
- I had to do a little bit of googling to find the dataset. After some searching, I came across this website with an excel file. It’s a survey conducted for a study on social media and K-pop which I found very interesting. I liked the questions they asked and I also liked that the survey was conducted recently.
- The dataset contains 240 K-pop fans from all over the world and there were 22 survey questions.
Dataset link: Rraman, Saanjanaa (2020): KPOP DATA.xlsx. figshare. Dataset. https://doi.org/10.6084/m9.figshare.12093648.v2

## Data Cleaning
- Data cleaning is an important step as you want the cleanest data for EDA and model building. If you put garbage in, then you get garbage out from the model.
- Datasets might have leading and trailing white spaces. So, I decided to remove those white spaces using this function. Then I removed the first column “Timestamp” as it’s not useful.
- Since the column names are the questions and they are too long, I decided to give them code names to simply the columns.
  ![](/images/1.png)
- There are three columns with null values. First, let’s check the columns with only one null value.
  ![](/images/2.png)
- I found out that the null values in life_chg and money_src were “n/a”, so I simply replaced them with a string “none”.
- For the “daily_MV_hr” column, I decided to replace the null values with the average. There are multiple ways of handling null values (deleting the row, assigning a unique category, or you can run a regression model to predict the missing values, etc), but I thought replacing them with the average value would be the best choice.
  ![](/images/3.png)
- I took the mean of 1 and 4 which is 2.5 hrs and removed the word “hours”. I noticed that some of the categories were in ranges, so I took the average of those ranges for the sake of simplicity. I created a special function to take care of this.
- I realized that this dataset is kind of messy. So I repeated similar steps to clean each column.
- I saved the cleaned data frame to a CSV file for the next part of the tutorial.
