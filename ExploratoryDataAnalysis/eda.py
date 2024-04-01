import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
data = pd.read_csv('tour_package.csv')
print(data)

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Get an overview of the dataset including data types and missing values
print(data.info())
print(data.dtypes)
print(data.shape)

# Summary statistics for numerical features
print(data.describe())

# Unique values for categorical features
print(data['Gender'].unique())  # Replace 'Gender' with actual column names

import matplotlib.pyplot as plt
import seaborn as sns

# A. What is the distribution of customerages, and how does age relate to product purchase (ProdTaken)?

print(data.Age.describe())
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

print(pd.crosstab(data.ProdTaken,data.Age))
plt.figure(figsize=(10, 6))
sns.boxplot(x='ProdTaken', y='Age', data=data)
plt.title('Relation of Age to Product Purchase')
plt.xlabel('Product Taken')
plt.ylabel('Age')
plt.show()

d1=data['Age'].value_counts()
print(d1)
print(d1.sort_index())
df2=pd.pivot_table(data,values="ProdTaken" ,index='Age',aggfunc=np.sum)
print(df2)

# B. How does the type of contact(type of contact)influence the likelihood of purchasing a travel product?

contact_types=pd.pivot_table(data,values='ProdTaken' , index="TypeofContact" , aggfunc=np.sum)
print(contact_types)
plt.figure(figsize=(10, 6))
sns.countplot(x='TypeofContact', hue='ProdTaken', data=data)
plt.title('Type of Contact vs. Product Purchase')
plt.xlabel('Type of Contact')
plt.ylabel('Count')
plt.show()

# C.  Is there a correlation between the city tier(citytier)and monthly income (monthly income) of customers?

correlation = pd.pivot_table(data,values='MonthlyIncome' , index="CityTier" , aggfunc=np.sum)
print(correlation)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CityTier', y='MonthlyIncome', data=data)
plt.title('Correlation between City Tier and Monthly Income')
plt.xlabel('City Tier')
plt.ylabel('Monthly Income')
plt.show()

# D. What is the average duration of a pitch (duration of pitch)for customers who purchased a product versus those who did not?

durationavg= pd.pivot_table(data,values="DurationOfPitch" ,index="ProdTaken" , aggfunc='mean')
print(durationavg)
plt.figure(figsize=(10, 6))
sns.boxplot(x='ProdTaken', y='DurationOfPitch', data=data)
plt.title('Average Duration of Pitch for Product Purchase')
plt.xlabel('Product Taken')
plt.ylabel('Duration of Pitch')
plt.show()

# E. How do occupation types(occupation)distribute among customers,and is there an occupation type that is more likely to purchase a travel product?

occupationdist = data.groupby("Occupation")['CustomerID'].count()
print(occupationdist)
occupationtopurchasetp= data.groupby("Occupation")["ProdTaken"].mean()
print(occupationtopurchasetp)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='Occupation', hue='ProdTaken', data=data)
plt.title('Occupation Types vs. Product Purchase')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# F.  Are there any gender-based preferences for the type of product pitched (ProductPitched)?

gender = pd.pivot_table(data,values="ProductPitched", index="Gender" , aggfunc="count")
print(gender)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', hue='ProductPitched', data=data)
plt.title('Gender vs. Product Pitched')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# G. What is the relationship between the number of trips(number of trips)taken by a customer and their likelihood to purchase a new travel product?

tripswithprodtaken = pd.pivot_table(data,values='ProdTaken',index='NumberOfTrips',aggfunc=np.sum)
print(tripswithprodtaken)
# Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='NumberOfTrips', hue='ProdTaken', data=data)
plt.title('Number of Trips vs. Product Purchase')
plt.xlabel('Number of Trips')
plt.ylabel('Count')
plt.show()

# H. Does having a passport(passport)correlate with a higher number of trips taken or a higher likelihood of purchasing a travel product?

passport = data.groupby('Passport')['NumberOfTrips'].mean()
print(passport)
likelihood =data.groupby('Passport')['ProdTaken'].mean()
print(likelihood)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='Passport', hue='ProdTaken', data=data)
plt.title('Passport vs. Product Purchase')
plt.xlabel('Passport')
plt.ylabel('Count')
plt.show()

# I. How satisfied are customers with the pitch (pitch satisfaction score),and does this satisfaction influence product purchase?

satisfaction = data.groupby('PitchSatisfactionScore')['CustomerID'].count()
print(satisfaction)
checkingsatisfaction = data.groupby("PitchSatisfactionScore")["ProdTaken"].sum()
print(checkingsatisfaction)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='ProdTaken', y='PitchSatisfactionScore', data=data)
plt.title('Pitch Satisfaction vs. Product Purchase')
plt.xlabel('Product Taken')
plt.ylabel('Pitch Satisfaction Score')
plt.show()

# J. Among customers with children (number of children visiting), how does the number of children impact travel product purchases?

NumberOfChildrenVisiting = data.groupby('NumberOfChildrenVisiting')['ProdTaken'].mean()
print(NumberOfChildrenVisiting)
Genderpreferences = pd.pivot_table(data, index='Gender', columns='ProductPitched',aggfunc='size', fill_value=0)
print(Genderpreferences)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='NumberOfChildrenVisiting', hue='ProdTaken', data=data)
plt.title('Number of Children vs. Product Purchase (Customers with Children)')
plt.xlabel('Number of Children Visited')
plt.ylabel('Count')
plt.show()

# K. Gender preferences for product types pitched
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', hue='ProductPitched', data=data)
plt.title('Gender vs. Product Pitched')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# L. Impact of marital status on travel preferences: does marital status affect the choice of travel product, and if so, how do different marital statuses correlate with product purchases (prod taken) ?

impactofmaritialstatus = pd.pivot_table(data, index='MaritalStatus', columns='ProductPitched', aggfunc='size', fill_value=0)
print(impactofmaritialstatus)
Maritialstatuscorr = data.groupby('MaritalStatus')['ProdTaken'].mean()
print(Maritialstatuscorr)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='MaritalStatus', hue='ProdTaken', data=data)
plt.title('Marital Status vs. Product Purchase')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()

# M. Relationship between number of children and travel product interest: how does the number of children visiting (number of children visiting) impact the likelihood of purchasing a travel product?

NumberOfChildrenVisiting =  data.groupby('NumberOfChildrenVisiting')['ProdTaken'].mean()
print(NumberOfChildrenVisiting)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='NumberOfChildrenVisiting', hue='ProdTaken', data=data)
plt.title('Number of Children vs. Product Purchase')
plt.xlabel('Number of Children Visited')
plt.ylabel('Count')
plt.show()

# N. Influence of owning a car on travel decisions: is there a correlation between owning a car (own car) and the number of trips taken (number of trips) or the type of travel product purchased?

corrownbycartrips = data.groupby('OwnCar')['NumberOfTrips'].mean()
print(corrownbycartrips)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.countplot(x='OwnCar', hue='ProdTaken', data=data)
plt.title('Own Car vs. Product Purchase')
plt.xlabel('Own Car')
plt.ylabel('Count')
plt.show()

# O. Income level and product choice: how does the monthly income (monthly income) of customers influence their choice of travel products, and is there a preferred product for different income levels?

income = pd.pivot_table(data, index='MonthlyIncome', columns='ProductPitched', aggfunc='size', fill_value=0)
print(income)
#Data Visualization
plt.figure(figsize=(10, 6))
sns.boxplot(x='MonthlyIncome', y='ProductPitched', data=data)
plt.title('Monthly Income vs. Product Pitched')
plt.xlabel('Monthly Income')
plt.ylabel('Product Pitched')
plt.show()
