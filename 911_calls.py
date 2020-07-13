import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/911.csv')

# Check top 5 Townships for 911 Calls
print('Top 5 townships for 911 calls')
print(df['twp'].value_counts().head(5))

# Extract the 'Reason' for a 911 Call from the 'titles' column and create a new column
df['Department'] = df['title'].apply(lambda x: x.split(':')[0])

# Check the most common reason for a 911 call based on this new column
print('Most common departments for a 911 call: ')
print(df['Department'].value_counts())

# Plot this
plt.figure()  # start new figure
ax = sns.countplot(x='Department', data=df)
ax.set_title('911 Calls for Various Departments')
plt.savefig('911_call_department.png')

# Convert the timestamp column from string format to pandas DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# Create Hour, Month, and Day of Week columns in the dataframe
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

# Map the integer values for Day of Week to string names for day of the week
dmap = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

# Plot count of calls vs. day of week with hue based on Reason
plt.figure()
ax2 = sns.countplot(x='Day of Week', data=df,
                    hue='Department', palette='viridis')
ax2.set_title('911 Calls by Day of Week')
plt.legend(bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=0.2)
plt.tight_layout()
plt.savefig('Calls-by-Day-of-Week.png')

# Plot count of calls vs. month with hue based on Reason
plt.figure()
ax3 = sns.countplot(x='Month', data=df, hue='Department', palette='viridis')
ax3.set_title('911 Calls by Month')
plt.legend(bbox_to_anchor=(1.0, 1), loc=2, borderaxespad=0.2)
plt.tight_layout()
plt.savefig('Calls-by-Month.png')

# Plot heatmap of vehicle accidents by day of week vs hours
# create new column based on reason for calls
df['Reason'] = df['title'].apply(lambda x: x.split(':')[1][1:-2])
# Restructure dataframe so day of week is rows and hour is columns, and only accidents are represented
accidents = df[df['Reason'] == 'VEHICLE ACCIDENT'].groupby(
    by=['Day of Week', 'Hour']).count()['e'].unstack()
plt.figure()
ax3 = sns.heatmap(accidents)
ax3.set_title('Heatmap of Accidents by Time and Day of Week')
plt.savefig('Accidents-Heatmap.png')
