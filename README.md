# 911_calls
A python script that reads in data on 911 call and cleans it up in order to create plots and gain insight on emergency calls.

This script makes use of a number of packages. These need to be installed in order for the script to function. They include Numpy, Pandas, matplotlib, seaborn, geopandas, descartes, and plotly. Some may already be included depending on your installation of Python.

The data file used can be downloaded from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). It consists of emergency calls made in Montgomery County, PA. The csv data file should be stored in a directory labeled 'data' in the working directory.

This script gives general information such as a ranking of the departments called by volume, the townships that make the most calls, etc. It also produces some plots to help visualize the data and saves them as png files. Where plotly is used to make interactive plots, the files are saved as html files. Shown below are examples of the plots produced.

![Accidents Heatmap](/plots/Accidents-Heatmap.png)

![Calls by Day of Week](/plots/Calls-by-Day-of-Week.png)

