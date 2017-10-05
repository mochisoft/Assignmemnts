import random
import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

"""
Class Assignment 2:
1. Generate Temperature values for a year
2. Calculate the standard deviation.
3. Generate scatter plots showing standards deviation for each month
"""

def get_month_days(x):
    max_days= {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'Jun':30,'Jul':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}

    return max_days[x]

def generateTemp():

    month_list=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    month_index=[1,2,3,4,5,6,7,8,9,10,11,12]
    avg_year_temp=[]

    for i in range(len(month_list)):
        avg_year_temp.append(random.sample(range(0, get_month_days(month_list[i])), get_month_days(month_list[i])))

    temp_dict={}

    for i in range(len(month_list)):
        #print i
        temp_dict.update({month_list[i]:avg_year_temp[i]})

    print temp_dict
    #Calculating mean temperature
    print "-------------Calculating mean------------------"
    temp_mean =[ sum(avg_year_temp[i]) / get_month_days(month_list[i]) for i in range(len(month_list))]
    print temp_mean

    #Calculating Variance
    print "-------------Calculating Variance------------------"
    temp_variance = [[(temp_mean[2] - x) * (temp_mean[2] - x) for x in avg_year_temp[2]] for y in range(len(month_list))]
    print temp_variance
    #Get final variance
    print "-------------Generating Variance------------------"
    variance=[sum(temp_variance[i])/get_month_days(month_list[i]) for i in range(len(temp_variance))]
    print variance
    #Calculating standard deviation
    print "-------------Standard Deviation------------------"
    sd=[math.sqrt(i) for i in variance]
    print sd

    #Generating Scatter plot
    colors = np.random.rand(50)
    area = np.pi * (15 * np.random.rand(50)) ** 2  # 0 to 15 point radii
    plt.xticks(month_index, month_list)
    plt.title('Monthly Temperature Deviation')
    plt.xlabel("Month of the Year")
    plt.ylabel("Standard Deviation")

    plt.scatter(month_index, sd, s=area,  alpha=0.5)
    plt.show()

if __name__ == '__main__':
    generateTemp()

