"""
@Michael Ochieng
Assignment 5
Implementing Simple Linear Regression Algorithm using python
"""
import csv
import numpy as np
import math
from matplotlib import pyplot as plt

def linearRegressionExample(csv_file,x_col,y_col):
    reader = csv.reader(open(csv_file),delimiter=',',quoting=csv.QUOTE_NONE)

    #Get the csv headers
    headers = reader.next()
    dataset=list()
    mid_row=0


    for row in reader:
        if not row:
            continue
        dataset.append(row)

    print dataset
    num_rows=len(dataset)

    if (num_rows %3) == 0:
        mid_row = ((num_rows/3)*2)
    else:
        mid_row=int(math.ceil(((num_rows/3)*2)))
        print mid_row


    training_dataset = dataset[0:mid_row]
    test_dataset = dataset[mid_row:]

    c,m = coefficients(training_dataset,x_col,y_col)
    predicted_results=prediction(test_dataset,c,m,x_col,y_col)
    x = [float(row[x_col]) for row in test_dataset]
    y = [float(row[y_col]) for row in test_dataset]
    print "c--m-->>",c,m

    print "pred y--", predicted_results


    #Generating Scatter plot
    colors = np.random.rand(50)
    area = np.pi * (15 * np.random.rand(50)) ** 2  # 0 to 15 point radii
    #plt.xticks(month_index, month_list)
    plt.title(headers[x_col]+' VS '+headers[y_col]+' Scatter plot')
    plt.xlabel(headers[x_col])
    plt.ylabel(headers[y_col])

    plt.plot(x, predicted_results)
    plt.scatter(x, y, s=area,  alpha=0.5)

    plt.show()


def mean(colvalues):

    return sum(colvalues)/len(colvalues)


def variance(colvalues,mean):
    var = [(colvalues[i]-mean)**2 for i in range(len(colvalues))]
    return sum(var)

# Calculate covariance between x and y
def covariance(x, x_mean, y, y_mean):

	covar = 0.0
	for i in range(len(x)):
		covar += (x[i] - x_mean) * (y[i] - y_mean)
	return covar

# Calculate coefficients
def coefficients(training_dataset,x_col,y_col):
    x = [float(row[x_col]) for row in training_dataset]
    y = [float(row[y_col]) for row in training_dataset]

    x_mean, y_mean = mean(x), mean(y)

    print x_mean
    m = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    c = y_mean - m * x_mean
    return [c, m]

def prediction(test_dataset,c,m,x_col,y_col):
    predicted_values=list()
    x=[float(row[x_col]) for row in test_dataset]
    y = [float(row[y_col]) for row in test_dataset]
    print "x--",x
    print "y--",y
    print len(x)

    for i in range(len(x)):
        predicted_price = c + float(m)*x[i]
        predicted_values.append(predicted_price)

    return predicted_values


if __name__ == '__main__':
    linearRegressionExample("File_path.csv",x_col_rownum,y_col_rownum)
