import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_dataset.csv' with the actual file path)
data = pd.read_csv('tour_package.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Get an overview of the dataset including data types and missing values
print(data.info())

# Summary statistics for numerical features
print(data.describe())

# Unique values for categorical features
print(data['Gender'].unique())  # Replace 'Gender' with actual column names

import matplotlib.pyplot as plt
import seaborn as sns

# A. Distribution of customer ages and relation to product purchase
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, kde=True)
plt.title('Distribution of Customer Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='ProdTaken', y='Age', data=data)
plt.title('Relation of Age to Product Purchase')
plt.xlabel('Product Taken')
plt.ylabel('Age')
plt.show()

# B. Type of contact and its influence on product purchase
plt.figure(figsize=(10, 6))
sns.countplot(x='TypeofContact', hue='ProdTaken', data=data)
plt.title('Type of Contact vs. Product Purchase')
plt.xlabel('Type of Contact')
plt.ylabel('Count')
plt.show()

# C. Correlation between city tier and monthly income
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CityTier', y='MonthlyIncome', data=data)
plt.title('Correlation between City Tier and Monthly Income')
plt.xlabel('City Tier')
plt.ylabel('Monthly Income')
plt.show()

# D. Average duration of pitch for customers who purchased a product vs. those who did not
plt.figure(figsize=(10, 6))
sns.boxplot(x='ProdTaken', y='DurationOfPitch', data=data)
plt.title('Average Duration of Pitch for Product Purchase')
plt.xlabel('Product Taken')
plt.ylabel('Duration of Pitch')
plt.show()

# E. Distribution of occupation types among customers and its relation to product purchase
plt.figure(figsize=(10, 6))
sns.countplot(x='Occupation', hue='ProdTaken', data=data)
plt.title('Occupation Types vs. Product Purchase')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# F. Gender-based preferences for product pitched
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', hue='ProductPitched', data=data)
plt.title('Gender vs. Product Pitched')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# G. Relationship between the number of trips taken by a customer and their likelihood to purchase a new travel product
plt.figure(figsize=(10, 6))
sns.countplot(x='NumberofTrips', hue='ProdTaken', data=data)
plt.title('Number of Trips vs. Product Purchase')
plt.xlabel('Number of Trips')
plt.ylabel('Count')
plt.show()

# H. Correlation between having a passport and number of trips taken or likelihood of purchasing a travel product
plt.figure(figsize=(10, 6))
sns.countplot(x='Passport', hue='ProdTaken', data=data)
plt.title('Passport vs. Product Purchase')
plt.xlabel('Passport')
plt.ylabel('Count')
plt.show()

# I. Satisfaction with the pitch and its influence on product purchase
plt.figure(figsize=(10, 6))
sns.boxplot(x='ProdTaken', y='PitchSatisfactionScore', data=data)
plt.title('Pitch Satisfaction vs. Product Purchase')
plt.xlabel('Product Taken')
plt.ylabel('Pitch Satisfaction Score')
plt.show()

# J. Impact of the number of children on travel product purchases for customers with children
plt.figure(figsize=(10, 6))
sns.countplot(x='NumberOfChildrenVisited', hue='ProdTaken', data=data)
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

# L. Impact of marital status on travel preferences and product purchases
plt.figure(figsize=(10, 6))
sns.countplot(x='MaritalStatus', hue='ProdTaken', data=data)
plt.title('Marital Status vs. Product Purchase')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()

# M. Relationship between number of children and travel product interest
plt.figure(figsize=(10, 6))
sns.countplot(x='NumberOfChildrenVisited', hue='ProdTaken', data=data)
plt.title('Number of Children vs. Product Purchase')
plt.xlabel('Number of Children Visited')
plt.ylabel('Count')
plt.show()

# N. Influence of owning a car on travel decisions
plt.figure(figsize=(10, 6))
sns.countplot(x='OwnCar', hue='ProdTaken', data=data)
plt.title('Own Car vs. Product Purchase')
plt.xlabel('Own Car')
plt.ylabel('Count')
plt.show()

# O. Income level and product choice
plt.figure(figsize=(10, 6))
sns.boxplot(x='MonthlyIncome', y='ProductPitched', data=data)
plt.title('Monthly Income vs. Product Pitched')
plt.xlabel('Monthly Income')
plt.ylabel('Product Pitched')
plt.show()
