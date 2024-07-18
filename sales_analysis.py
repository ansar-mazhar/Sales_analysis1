# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:46:23 2024

@author: STAR LAPTOP
"""
# SALES ANALYSIS FOR AN EVENT
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Diwali Sales Data.csv", encoding="unicode-escape")
#DATA CLEANSING
df.drop(['unnamed1', 'Status'], axis=1, inplace=True)
a = pd.isnull(df).sum()
df.dropna(inplace=True)
a = pd.isnull(df).sum()
df['Amount'] = df['Amount'].astype(int)
#EXPLORATORY DATA ANALYSIS
def func1():
    sns.displot(df['Gender'])
    plt.show
#WOMEN HAS MORE PURCHASING POWER THAN MEN
def func2():
    sns.displot(df['Age Group'])
    plt.show
def func3():
    sales_gen = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_gen)
def func4():
    sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state, x = 'State',y= 'Orders')
def func5():
    sales_state1 = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state1, x = 'State',y= 'Amount')
def func6():
    sns.displot(df['Marital_Status'])
    plt.show
def func7():
    sns.displot(df['Occupation'])
    plt.figure(figsize=(20, 6))
    plt.show 
def func8():
    sns.displot(df['Product_Category'])
    plt.figure(figsize=(20, 6))
    plt.show 
def func9():
    sales_state1 = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
    sns.set(rc={'figure.figsize':(15,5)})
    sns.barplot(data = sales_state1, x = 'Product_Category',y= 'Amount')
func1()
func2()
func3()
func4()
func5()
func6()
func7()
func8()
func9()

   