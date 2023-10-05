# Capstone-Project
## Overview

Major League Soccer Player's Association(MLSPA) has been keeping salary data on its players for years and would like to utilize that data with player's statistics data to evaluate player performance and its relationship to player salary. By anazlying this data, I hope to create a predictive model that can highlight this link and the particular aspects of player performance that are most tied to salary.

## Business Problem

MLS has growing rapidly and gaining in popularity, increasing their number of teams from just 13 in 2007 to 29 today. Likewise, the average team revenue increased from 37 million USD in 2008 to 579 million USD in 2022. https://huddleup.substack.com/p/how-lafc-became-major-league-soccers This also saw an increase in player salary over the years. In order to figure out what a player's salary should be, I analyzed a player's statistics by year in order to come up with recommendations to further bolster future analysis.

## Data Understanding

The statistics datasets in this analysis come from Mlssoccer.com, provided via a source on Kaggle who used webscraping before the website changed how it displayed information.https://www.kaggle.com/datasets/josephvm/major-league-soccer-dataset The salary datasets come directly from the MLSPA(Major League Soccer Players Association) on mlsplayers.org. I analyzed over 6000 players from the combined dataframe of these sources ranging from 2007-2022.

The statsistics datasets were csv files containing information about a field player's performance on during a season. The field dataset includes information such as goals, assists, games played, total minutes played, and more.

## Data Preparation

MLS wants to continue to expand and entice players the likes of Lionel Messi into the league. In order to understand the current salaries of players in the league, I combined the statistics and salary datasets.

I trained a Linear Regression Model, Random Forest Regression Model, and KNearestNeighbors Regression Model. I utilized a Pipeline and GridSearch for each of these to crossvalidate scores and iterate over many different models. I added and modified several feature columns, including Penaly Kick Conversion Rates, whether a player made the Postseason, a one-hot encoded breakdown of player position, and more. My final dataframe contained XX features that were used by these models to more accurately predict Player salary. I used r2 score, MSE, RMSE, and MAE to help evaluate how well my models were performing, but ultimately looked at r2 score and RMSE as my most important metrics to measure how far off a model was predicting salary.

## Data Cleaning

There was quite a lot of cleaning to do to get these datasets together. For the statistics dataframe, I dropped any information before 2007 as this is our start year for salary information with the designated player rule. I also removed postseason statistics as they are a miniscule addition to a player’s stats and most players do not make the poststeason in a year. 

For salary, I had a separate dataframe for each year from 2007-2020, and had to match the column names to combine as they were not consistent for each year. I also had to remove all goalkeepers, as they do not get paid based on the same statistics information as field players.

In order to join the two dataframes, I had to match information based on the player name and year. There were problems with the entry of player names, so I had to run a program that would identify the closest match in name between the two datasets so that the datasets would combine nicely.
Due to discrepancies in this data entry between the two sources however,  about 10% of the data was lost during this process of string matching. 

## Evaluation Metrics

In order to evaluate my models, I looked at three different metrics: r2 score, Root Mean Squared Error, and Mean Absolute Error. Simply put, the r2 score measure of much of the variance in the target variable, Base Salary this case, is explained by the independent variable, our statistics. The Root Mean Squared Error is the mean error between our observed and predicted salary, while the Mean Absolute error is the mean of the absolute values of those errors. Both the Root Mean Squared Error and Mean Absolute Error values are easier to understand as they operate in the same units as our target variable.

We will be looking at the Mean Absolute Error when discussing model performance,  while also touching on r2 score.

(RMSE and MAE operate in the units of target variable)

## Models

I trained the data on three different predictive models with several iterations each to evaluate the impact of player performance on salary. Ultimately, the Random Forest Regression performed the best, with a mean absolute error of $146,429. This means that the model on average predicted salary within $146,429 of a players actual salary utilizing their performance data. While it is the best of the three models, it’s still not performing incredibly well. There are many players in the MLS who don’t even make a salary that high.

The reason for this can be explained by the model’s r2 score, which sits at .53. As explained before, this means that the statistic features explain just about half of the variance in a player’s salary. 

## Permutation Importances
![Sheet 2](https://github.com/m-romanski/Capstone-Project/assets/113048559/1c3691f3-ca42-4bd7-a9a2-30ffa834d315)


I extracted the 10 most important features to the Random Forest regression. These features, when individually removed from the model, account for the largest increase in Mean Absolue Error. The bubbles in Orange represent features that were already a part of the dataset while the bubbles in black represent features that were added by me to help the performance of the model. 

Total Minutes Played ranks in at the top, with games started and games played also making the list. This makes sense considering players who play the most minutes on a team are usually those who are considered starters and are vitally important to the success of a team.

Interestingly, Shots, Shots on goals, and Goals are also towards the top. This could pose an issue when the model is predicting salary for defenders,  whose value to the team isn’t  measured on how many goals they score.

## Recommendations
<img width="879" alt="Random Forest Train Data" src="https://github.com/m-romanski/Capstone-Project/assets/113048559/ac91df5b-0199-4b2e-bb27-6b4ecf8d2d8f">

I plotted out the the data for my model’s predicted salaries vs a player’s actual salary, with players above the line having a higher actual salary than predicted salary, and players below the line having a lower actual salary than predicted salary. This is done to predict who in the league is getting underpaid or overpaid based upon their performance in a season. When looking at the graph, there is a noticeable trend. All of those players at the top of the graph are designated players. Because of this, they are being overpaid in comparison to what their statistics say they should be paid. 

Based on this, I recommend that MLSPA negotiates for an increased Salary Minimum and maximum. In 2020, the Salary minimum was $81,375 while the salary maximum was $612,500. This range pales in comparison to some of the highest paid MLS players who sign a DP contract as high as $7,000,000. By keeping the Salary Minimum and Maximum so tight, and with only 3 DP slots available for team, this current structure  limits the potential for those MLS players who are developed in the league and break out to remain in the league at a fair level of compensation based upon their performances.

Additionally, an increased Salary cap helps MLS teams keep more quality players and pay them more. The 2020 MLS team salary cap sat at $4,900,000, less than some players in the leagues entire contracts are worth on a yearly basis. The imbalance between the average league player and the DP’s salary are far too evident.

My model’s performance is not working well enough for me to recommend its use in negotiations with the MLS at this time. Fortunately, the new CBA negotiations will not come until 2027, so there is time for it to improve. 

## Next Steps

When testing on unseen data, my model predictions lose some of its interpretation.  In order to improve my model’s performance in preparation for the next CBA negotiations, there are some steps I’d like to take. 

First, I would like to gather more statistics that cover a wider range of skills on the field. Data like pass completion percentage, tackles, and duels won may be more valuable to midfielders and defenders and help inform on why they are getting the salary they are.

Additionally, I would like to see better data entry so that I don’t have to lose up to 10% of the data in the future, as the amount of data available for MLS statistics is already quite small considering its a fairly young league. 

Finally, I would like to get other features that aren't relevant to player performance. Something like a popularity score, jersey sales data, and more could help inform on the other reasons a player may be getting paid the salary they are.
