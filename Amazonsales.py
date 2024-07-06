#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as mp
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv(r'C:\Users\DELL\Downloads\Amazon Sales data.csv')


# In[73]:


data.head(15)


# In[75]:


data.shape


# In[8]:


data = data[["Order Date","Order ID","Order Priority","Ship Date","Item Type","Region","Country","Sales Channel","Units Sold","Unit Price","Unit Cost","Total Revenue","Total Cost","Total Profit"]]


# In[ ]:





# In[74]:


data.head(15)


# In[76]:


#Checking the number of horizontal rows in the data.
data.axes[0]


# In[77]:


#Checking the data types of the each columns as each row contains different data types
data.dtypes


# In[12]:


#Checking whether any columns contain null values
data.columns.isnull()


# In[78]:


np.corrcoef(data.loc[:,'Total Revenue'].iloc[:],data.loc[:,'Total Profit'].iloc[:])


# In[80]:


data.head(15)


# In[17]:


data1 = data[["Units Sold","Unit Price","Unit Cost","Total Revenue","Total Cost","Total Profit"]]


# In[81]:


#Checking the covariance between different factors
data1.cov()


# In[82]:


#Checking correlation coefficient between different factors using the "pearson"method
data1.corr(method='pearson')


# In[83]:


#Calculating the average profit generated for a product
np.average(data1['Total Profit'])


# In[84]:


#Calculating the maximum profit earned
np.max(data1['Total Profit'])


# In[85]:


#Calculating the minimum profit earned
np.min(data1['Total Profit'])


# In[23]:


#Calculating the variance between the total Profit 
np.var(data1['Total Profit'])


# In[24]:


#Maximum and minimum profit generated are ₹ 1719922.04 and ₹ 1258.02
np.max(data1['Total Revenue'])


# In[25]:


np.min(data1['Total Revenue'])


# In[26]:


np.var(data1['Total Revenue'])


# In[27]:


np.percentile(data['Total Revenue'],50,axis=0,overwrite_input=True)


# In[28]:


np.median(data1['Total Revenue'])


# In[29]:


#Scatter plot between total profit and total revenue
mp.scatter(data1['Total Profit'],data['Total Revenue'])


# In[30]:


#hecking the total revenue in histogram graph
mp.hist(data1['Total Revenue'])


# In[86]:


#Calculating the correlation coefficient between total profit and total revenue
np.correlate(data1['Total Revenue'],data1['Total Profit'])


# In[32]:


np.histogram(data1['Total Cost'],bins=10)


# In[33]:


mp.hist(data1['Total Cost'],bins=20)


# In[34]:


data1.corr(method='pearson')


# In[35]:


mp.scatter(data1['Units Sold'],data1['Unit Cost'])


# In[41]:


mp.hist(data1['Unit Cost'])


# In[45]:


np.min(data1['Unit Cost'])


# In[46]:


np.max(data1['Unit Cost'])


# In[47]:


np.median(data1['Unit Cost'])


# In[48]:


np.var(data1['Unit Cost'])


# In[49]:


np.std(data1['Unit Cost'])


# In[ ]:


Maximum and minimum unit costs are ₹ 6.92 and ₹ 524.96 respectively
Average unit cost of a product is ₹ 191.05. 
The Unit Cost varies considerably throughout it's distribution. 
The median cost of a unit stands at ₹ 107.28.


# In[87]:


area_plot = data.plot.area(x='Unit Price',y='Total Profit',color='red',stacked=True,legend=None)
mp.ylabel('Total Profit')


# In[ ]:


From the above plot we can conclude that the maximum profit has been generated in the unit price range of ₹400-₹500.


# In[53]:


area_plot = data.plot.area(x='Unit Cost',y='Total Profit',color='b',stacked=True,legend=None)
mp.ylabel('Total Profit')


# In[ ]:


From the above plot we can conclude that the maximum profit has been generated in the unit cost range of ₹200-₹300.


# In[54]:


data1.plot.area(x='Units Sold',y='Total Profit',color='green',legend=None)
mp.ylabel('Total Profit')


# In[ ]:


From the above plot we can conclude that maximum profit has been generated
when the number of units sold were between 8000 and 10000. 
More the number of units sold, more will be the profit generated.


# In[56]:


data1.plot.area(x='Units Sold',y='Total Cost',color='purple',legend=None)
mp.ylabel('Total Cost')


# In[ ]:


From the above plot we can conclude that maximum cost has been generated
when the units sold were above 8000 and below 10000.


# In[57]:


data1.plot.area(x='Units Sold',y='Total Revenue',color='aqua',legend=None)
mp.ylabel('Total Revenue')


# In[ ]:


From the above plot we can conclude that maximum revenue has been generated 
when 8000-10000 units of products were sold.


# In[60]:


bar_plot = data.plot.bar(x='Units Sold',y=['Total Revenue','Total Cost','Total Profit'],color=['purple','red','blue'],stacked=True,rot=True)
mp.xticks(rotation=95)
mp.locator_params(nbins=39)
mp.tick_params(axis='y', which='major', labelsize=9)


# In[61]:


data.plot.barh(x='Item Type',y='Total Revenue',color='blue')
mp.locator_params(nbins=28)
mp.xlabel('Total Revenue')


# In[90]:


#Finding the unique values of all the categories of item type accordinding to the hash table.
data['Item Type'].unique()


# In[63]:


#Rearranging the items columnaccording to their Unique values.
items = ['Baby Food', 'Cereal', 'Office Supplies', 'Fruits', 'Household',
       'Vegetables', 'Personal Care', 'Clothes', 'Cosmetics', 'Beverages',
       'Meat', 'Snacks']


# In[64]:


data['Item Type'] = pd.Categorical(data['Item Type'],categories=items,ordered=True)


# In[89]:


#Checking the items are rearranged or not
data


# In[88]:


pd.pivot_table(data,values='Total Revenue',index='Item Type',aggfunc='count').plot(kind='bar')


# In[ ]:


From the above graph we can conclude that maximum revenue has been 
generated from the items 'Clothes' and 'Cosmetics' closely followed by 'Office Supplies'


# In[67]:


pd.pivot_table(data,values=['Total Revenue','Total Cost','Total Profit'],index='Units Sold',aggfunc='count').plot(kind='kde',color=['green','orange','red'],stacked=True)
mp.xlabel('Units Sold')


# In[91]:


data['Order Date'].unique()


# In[92]:


pd.pivot_table(data,values='Total Profit',index='Order Date',aggfunc='count').plot(kind='hist',color='blue',stacked=False,legend=None)
mp.xticks(rotation=90)
mp.ylabel('Total Profit')
mp.locator_params(nbins=32)
mp.xlabel('Order Date')


# In[71]:


data.describe()


# In[93]:


data


# In[94]:


mp.scatter(data['Units Sold'],data['Total Cost'])
mp.xlabel('Units Sold')
mp.ylabel('Total Cost')


# In[ ]:


From the above scatter plot we can conclude that more the number of units sold of a product,
more will be the total cost associated with it


# In[96]:


sn.barplot(x='Region',y='Total Cost',data=data)
mp.xticks(rotation=90)


# In[ ]:


Cost of items is maximum in Asia and North America, and minimum in Sub-Saharan Africa


# In[98]:


sn.pairplot(data)


# In[99]:


sn.heatmap(data1.corr(),annot=True)


# In[ ]:


From the above heatmap, we can infer that Total Cost is strongly related to Unit Price,Unit Cost and Total Profit.
Units Sold and {Unit Price and Unit Cost} are completely independent.
Unit Cost, Unit Price and Total Cost are almost completely independent of Total Revenue.


# In[100]:


data['Country'].unique()


# In[ ]:


countries=(['Tuvalu', 'Grenada', 'Russia', 'Sao Tome and Principe', 'Rwanda',
       'Solomon Islands', 'Angola', 'Burkina Faso',
       'Republic of the Congo', 'Senegal', 'Kyrgyzstan', 'Cape Verde',
       'Bangladesh', 'Honduras', 'Mongolia', 'Bulgaria', 'Sri Lanka',
       'Cameroon', 'Turkmenistan', 'East Timor', 'Norway', 'Portugal',
       'New Zealand', 'Moldova ', 'France', 'Kiribati', 'Mali',
       'The Gambia', 'Switzerland', 'South Sudan', 'Australia', 'Myanmar',
       'Djibouti', 'Costa Rica', 'Syria', 'Brunei', 'Niger', 'Azerbaijan',
       'Slovakia', 'Comoros', 'Iceland', 'Macedonia', 'Mauritania',
       'Albania', 'Lesotho', 'Saudi Arabia', 'Sierra Leone',
       "Cote d'Ivoire", 'Fiji', 'Austria', 'United Kingdom', 'San Marino',
       'Libya', 'Haiti', 'Gabon', 'Belize', 'Lithuania', 'Madagascar',
       'Democratic Republic of the Congo', 'Pakistan', 'Mexico',
       'Federated States of Micronesia', 'Laos', 'Monaco', 'Samoa ',
       'Spain', 'Lebanon', 'Iran', 'Zambia', 'Kenya', 'Kuwait',
       'Slovenia', 'Romania', 'Nicaragua', 'Malaysia', 'Mozambique']


# In[ ]:


data['Country'] = pd.Categorical(data['Country'],categories=countries,ordered=True)


# In[102]:


mp.figure(figsize=(15,6))
sn.barplot(x='Country', y='Total Revenue', data=data, ci=None)
mp.xticks(rotation=90)
mp.tick_params(axis='x', which='major', labelsize=10)


# In[ ]:


From the above we can conclude Mozambique is the country where maximum revenue has been generated followed by Kenya & Manaco


# In[103]:


data.sort_values(by='Unit Price')


# In[104]:


data.plot.bar(x='Unit Price',y='Total Cost',legend=None,figsize=(15,10),rot=0)
mp.ylabel('Total Cost')
mp.xticks(rotation=90)
mp.locator_params(nbins=90)


# In[ ]:


The above bar graph we can conclude that higher the value of unit price of a product, more will be the total cost of it.


# In[105]:


pd.pivot_table(data,index='Item Type',values='Total Profit',aggfunc=np.median).plot(kind='line',color='green',figsize=(15,5),legend=None)
mp.ylabel('Total Profit')


# In[ ]:





# In[ ]:


From the above plot we can conclude that maximum of the total profit is received by cosmetics item type.


# In[106]:


data.groupby('Region')['Total Profit'].count().plot(kind='area',color=['purple','brown','blue','green'])
mp.xticks(rotation=90)
mp.ylabel('Total Profit')


# In[ ]:


from the above plot we can conclude that 
the Maximum profit has been generated in the Sub-Saharan African region while minimum profit has been
generated in the North American region.


# In[108]:


data['Order Priority'].unique()


# In[109]:


order_priorities = ['H', 'C', 'L', 'M']


# In[110]:


data['Order Priority'] = pd.Categorical(data['Order Priority'],categories=order_priorities,ordered=True)


# In[112]:


data.groupby('Order Priority')['Total Revenue'].count().plot(kind='bar',color=['red','blue','green','pink'])
mp.ylabel('Total Revenue')


# In[ ]:


From the above bar graph we can conclude that maximum profit has been generated by products having order priority 'H'
while minimum profit has been obtained in case of 'C' priority product orders.


# In[113]:


mp.figure(figsize=(12,5))
data.groupby('Order Date')['Total Profit'].sum().plot(kind='line',color='blue')
mp.ylabel('Total Profit')


# In[ ]:


Above graph we can conclude that maximum profit has been achieved during the year 2012.


# In[114]:


mp.figure(figsize=(12,5))
data.groupby('Ship Date')['Total Profit'].sum().plot(kind='line',color='green')
mp.ylabel('Total Profit')


# In[115]:


data.plot.bar(x='Item Type',y='Unit Cost',legend=None,figsize=(15,10),rot=0)
mp.ylabel('Unit Cost')
mp.xticks(rotation=90)
mp.locator_params(nbins=90)


# In[117]:


From the above bar plot 
we can conclude that office supplies and some items has the maximum unit cost and fruits has minimum unit cost.


# In[118]:


data['Item Type'].dropna(inplace=True)


# In[119]:


labels = data['Item Type'].value_counts().index


# In[123]:


sizes = data['Item Type'].value_counts().values
colors = ['red','yellow','red','lime','purple','pink']


# In[121]:


mp.figure(figsize=(7,7))
mp.pie(sizes,labels=labels,colors=colors,autopct='%1.2f%%')
mp.title('Distribution of Item Types',fontsize=15,color='blue')


# In[ ]:


the above pie chart we can conclude that clothes and cosmetics are the most purchased items 
while meat and snacks are the least purchased ones.


# In[ ]:


labels = data['Region'].value_counts().index


# In[ ]:


sizes = data['Region'].value_counts().values
colors = ['blue','green','red','brown','purple','lime']


# In[122]:


mp.figure(figsize=(7,7))
mp.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
mp.title('Distribution of Total Revenue per Region',fontsize=15,color='blue')


# In[125]:


sn.lmplot(x='Unit Cost',y='Total Profit',data=data,height=5,aspect=1,hue='Sales Channel',logx=False,truncate=True,ci=100,y_jitter=2.2,scatter=True,fit_reg=True,markers=['o','x'])


# In[126]:


pd.pivot_table(index='Order Date',values='Total Revenue',data=data,aggfunc='count').plot(kind='line',color='red',legend=True)
mp.ylabel('Total Revenue')
mp.yticks(fontsize=12,color='lime')
mp.xticks(fontsize=12,color='purple')
mp.title('Revenue generated per Order Date',fontsize=16,color='blue')


# In[ ]:




