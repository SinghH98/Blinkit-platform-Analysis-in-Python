#!/usr/bin/env python
# coding: utf-8

# ## **DATA ANALYSIS PYTHON PROJECT - BLINKIT ANALYSIS**

# ### **Import Libraries**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### **Import Raw Data**

# In[2]:


df = pd.read_csv("D:\Power BI\Blinkit Analysis\BlinkIT Grocery Python Data.csv")


# In[3]:


df.head(10)


# ### **Sample Data**

# In[4]:


df.tail(10)


# ### **Size of Data**

# In[5]:


print("size of data: ", df.shape)


# ### **Field Informtion**

# In[6]:


df.columns


# ### **Data Types**

# In[7]:


df.dtypes


# ## **Data Cleaning**

# In[8]:


print(df['Item Fat Content'].unique())


# In[9]:


df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat',
                                                        'low fat': 'Low Fat',
                                                         'reg': 'Regular'
                                                        })


# In[10]:


print(df['Item Fat Content'].unique())


# ## **Business Requirements**

# ### **KPI Requirements**

# In[11]:


#Total Sales
total_sales = df['Sales'].sum()

#Average Sales
avg_sales = df['Sales'].mean()

#Number of Items Sold
no_of_items_sold = df['Sales'].count()

#Average Ratings
avg_rating = df['Rating'].mean()

#Display
print(f"Total Sales: ${total_sales:,.1f}")
print(f"Average Sales: ${avg_sales:,.1f}")
print(f"No Of Items: {no_of_items_sold:,.1f}")
print(f"Average Rating: {avg_rating:,.1f}")


# ### **Charts Requirements**

# #### **Total Sales By Fat Content**

# In[12]:


sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

plt.pie(sales_by_fat, labels = sales_by_fat.index,
                       autopct = '%.1f%%',
                       startangle = 90)
plt.title('Sales By Fat Content')
plt.axis('equal')
plt.show()


# #### **Total Sales By Item Type**

# In[13]:


sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)

plt.xticks(rotation=-90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales By Item Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
           f'{bar.get_height():,.0f}', ha='center', va='bottom', fontsize=8)
    
plt.tight_layout()
plt.show()


# #### **Fat Content By Outlet For Total Sales**

# In[14]:


grouped = df.groupby(['Outlet Location Type', 'Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular', 'Low Fat']]

ax = grouped.plot(kind='bar', figsize=(8,5), title='Outlet Tier By Item Fat Content')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()


# #### **Total Sales By Outlet Establishment**

# In[15]:


sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x,y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x,y, f'{y:,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()



# #### **Sales By Outlet Size**

# In[16]:


sales_by_size = df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(4,4))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')

plt.tight_layout()
plt.show()


# #### **Sales By Outlet Location**

# In[17]:


sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_loaction = sales_by_location.sort_values('Sales', ascending=False)

plt.figure(figsize=(8, 3)) #Smaller height, enough width
ax = sns.barplot(x='Sales', y='Outlet Location Type', data=sales_by_location)

plt.title('Total Sales by Outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')

plt.tight_layout() #Ensure Layout fits without scroll
plt.show()


# In[ ]:




