# Now I will start the task of Smartwatch Data Analysis by importing the necessary Python libraries and the dataset:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


data = pd.read_csv("dailyActivity_merged.csv") # Load the dataset which is the csv file
print("The dataset has been loaded successfully!") # Display a message to confirm that the dataset has been loaded successfully
print(data.head()) # Display the first few rows of the dataset
print("\n") # Display a blank line

#check if it has any null values or not in the dataset
print("Checking for null values in the dataset:")
print(data.isnull().sum()) # Check for null values in the dataset
print("\n")

#check for more information about the columns in the dataset
print("Checking for more information about the dataset:")
print(data.info()) # Check for more information about the dataset
print("\n")


print("ActivityDate column in the dataset:")
# Changing datatype of ActivityDate column from object to datetime in the data table
data["ActivityDate"] = pd.to_datetime(data["ActivityDate"], format="%m/%d/%Y") # to_datetime() function is used to convert the datatype of the "ActivityDate" column to datetime 
print(data.info()) 
print("\n")

print("Total number minutes spent in different activities:")
# Adding a new column "TotalMinutes" to the data table which shows the total number of minutes spent in different activities which the table columns
data["TotalMinutes"] = data["VeryActiveMinutes"] + data["FairlyActiveMinutes"] + data["LightlyActiveMinutes"] + data["SedentaryMinutes"]
print(data["TotalMinutes"].sample(5))
print("\n")

print("Descriptive statistics of the dataset:")
print(data.describe()) # Display the descriptive statistics of the dataset
print("\n")

print("Relationship between calories burned and the total steps walked in a day:")
print("Displaying the graph in browser...")
# Now I will plot a graph with the x-axis representing the "ActivityDate" column and the y-axis representing the "TotalSteps" column: 
figure = px.scatter(data_frame = data, x="Calories", y="TotalSteps", size="VeryActiveMinutes", trendline="ols", title="Relationship between Calories & Total Steps") #scatter is a function used to plot the graph
#size is for the circle size in the graph of the scatter plot
#trendline is for the linear regression line in the graph
figure.show() # Display the graph
print("\n")

#average total number of active minutes in a day:
print("Pie graph showing average total number of active minutes in a day:")
print("Displaying the graph in browser...")
label = ["Very Active Minutes", "Fairly Active Minutes", 
         "Lightly Active Minutes", "Inactive Minutes"]
counts = data[["VeryActiveMinutes", "FairlyActiveMinutes", 
               "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['purple','green', "red", "blue"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Total Active Minutes')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
print("\n")

#observations of the data
# 81.3% of Total inactive minutes in a day
# 15.8% of Lightly active minutes in a day
# On an average, only 21 minutes (1.74%) were very active
# and 1.11% (13 minutes) of fairly active minutes in a day