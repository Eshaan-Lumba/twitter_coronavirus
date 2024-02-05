# Analysing 2020 Tweets for Coronavirus

In this repository, I performed some data analysis on geotagged tweets in 2020 to monitor the spread of covid-19. The biggest challenges from this project was learning to work with large datasets (1.1 billion tweets) and writing parallel code to optimize scripts. 

## Tweet Data

The tweets were stored in the format `geoTwitterYY-MM-DD.zip` indicating that we had a single `.zip` file for each day. Within each file, there were 24 files containing the tweets for each hour in the day. 

## Methods

As mentioned previously, writing parallel code was essential to processing the data. Hence, we used the **MapReduce** procedure in order to categorize the tweets depicted below: 
<img src=mapreduce.png width=100% />

In the `src/map.py` file, we process an individual zip file of the above format (a day's tweets) and process it to categorize the tweets from that day by their hashtags, and subcategorize them by their country and language. For example, running `src/map.py` on `geoTwitter20-01-01.zip` and would have the following output if subcategorized by country (the complete output is omitted for brevity):
```
{
    "_all": {
        "US": 17561323,
        "ZW": 29274,
        "CO": 783258,
        "IT": 516817,
        "GB": 3512795,
        "NOCOUNTRY": 123488,
        ...
    },
    "#flu": {
        "ID": 1,
        "BR": 7,
        "CO": 2,
        ...
    },
    "#doctor": {
        "GB": 622,
        "US": 80,
        "BR": 20,
        ...
    },
    "#hospital": {
        "US": 139,
        "CA": 12,
        "JP": 2,
        ...
    },
    "#corona": {
        "BR": 4,
        "MX": 3,
        "CO": 2,
        ...
    },
    "#cough": {
        "GB": 2,
        "US": 4
    },
    "#nurse": {
        "GB": 20,
        "ZA": 1,
        "US": 87,
        ...
    },
    "#sick": {
        "GB": 5,
        "US": 23,
        "IN": 1,
        ...
    },
    "#virus": {
        "IN": 4,
        "MX": 1
    },
    "#sneeze": {
        "US": 1
    }
}
```
The `shell/run_maps.sh` script allows us to run `src/map.py` on all the files in the dataset from the year 2020 in parallel, also utilizing the `nohup` command to run in the background. This script generates two new files for each day, one subcategorized by country and the other by language. 

Next, the `src/reduce.py` file combines all the subcategorized "country" files into one and all the subcategorized "country" files into another one to have two files summarizing the data. Finally, the `src/visualize.py` file generates bar graphs of this data given a hashtag to display the number of tweets containing the provided hashtag by each country or language. 

The `src/alternative_reduce.py` file takes multiple hashtags as an input, and outputs a line graph for each hashtag indicating the number of tweets containing that hashtag throughout the year. 

## Results

We now show some of our generated results and graphs from our processed data.

### Top Countries with Tweets containing "#coronavirus"
![Image Alt text](/plots/COUNTRY_\#coronavirus.png)

**Task 5: Uploading**

Commit all of your code and images output files to your github repo and push the results to github.
You must:
1. Delete the current contents of the `README.md` file
1. Insert into the `README.md` file a brief explanation of your project, including the 4 generated png files.
    This explanation should be suitable for a future employer to look at while they are interviewing you to get a rough idea of what you accomplished.
    (And you should tell them about this in your interviews!)

## Submission

Upload a link to you github repository on sakai.
I will look at your code and visualization to determine your grade.

**Grading:**

The assignment is worth 32 points:

1. 8 points for getting the map/reduce to work
1. 8 points for your repo/readme file
1. 8 points for Task 3 plots
1. 8 points for Task 4 plots

The most common ways to miss points are:
1. having incorrect data plotted (because the map program didn't finish running on all of the inputs)
1. having illegible plots that are not "reasonably" formatted

Notice that we are not using CI to grade this assignment.
There's two reasons:

1. You can get slightly different numbers depending on some of the design choices you make in your code.
    For example, should the term `corona` count tweets that contain `coronavirus` as well as tweets that contain just `corona`?
    These are relatively insignificant decisions.
    I'm more concerned with your ability to write a shell script and use `nohup`, `&`, and other process control tools effectively.

1. The dataset is too large to upload to github actions.
    In general, writing test cases for large data analysis tasks is tricky and rarely done.
    Writing correct code without test cases is hard,
    and so many (most?) analysis of large datasets contain lots of bugs.
