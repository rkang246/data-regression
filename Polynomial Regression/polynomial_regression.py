#!/usr/bin/env python2
#
# ======================================================
#	Program:	polynomial_regression.py
#	Author:		Robert Kang
#			(rkang246@gmail.com)
#	Created:	2018-08-01
#	Modified	2018-08-01
# ------------------------------------------------------
# Use: 
# ======================================================
#

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt


def readData(data_file):
	"""
	Reads the data from the input file
	
	Args:
		data_file: A file in csv format with
			   "x,y,std" for each row

	Returns:
		A 2D list x_y_std such that x_y_std[0] contains the
		x-values of the data_file, x_y_std[1] contains
		the y-values of the data_file, and x_y_std[2] contains
		the standard deviation of the data_file.
	"""
	
	fp = open(data_file)
	x_y_std = [[], [], []]

	for line in fp:
		line = line.strip()
		line = line.decode('utf-8-sig').encode('utf-8')
		row = line.split(',')
		x_y_std[0].append(float(row[0]))
		x_y_std[1].append(float(row[1]))
		x_y_std[2].append(float(row[2]))
		

	return x_y_std

def f(x, y, degree):
	"""
	Performs polynomial regression on the "degree"th degree.
	
	Args:
		x: A float array of x-values
		y: A float array of y-values
		degree: The degree of polynomial regression
	
	Returns:
		An array of float values, of polynomial coefficients,
		highest power first.
	"""
	return np.polyfit(x, y, degree)

def getEquation(x_values, y_values, degree):
	"""
	Converts the regression into an equation.
	
	Args:
		x_values: A float array of x-values
		y_values: A float array of y-values
		degree: The degree of polynomial regression
	
	Returns:
		A string equation form.
	"""
	regression = f(np.array(x_values), np.array(y_values), degree)
	equation = ""
	for i in range(0, len(regression)):
		equation += "" + str(regression[i]) + "*x**" + str(degree - i)
		if i != len(regression) - 1:
			equation += "+"
	return equation
	
def plot(equation, x_min, x_max, x_values, y_values, std, title):
	"""
	Plots an equation in a given range.
	
	Args:
		equation: A string equation to graph
		x_min: An integer starting value for
			  the domain to be plot
		x_max: An integer ending value for
			  the domain to be plot
		x_values: A float array of x-values
			  used for error bar purposes
		y_values: A float array of y-values
			  used for error bar purposes
		std: The standard deviation error.
		title: The string graph title
	
	Returns:
		none
	"""
	x = np.array(range(x_min, x_max + 1))
	y = eval(equation)
	plt.plot(x, y)
	plt.errorbar(x_values, y_values, yerr=std, fmt='o')

	plt.title(title)
	plt.xlabel("Time (Minutes)")
	plt.ylabel("Length (Microns)")
	plt.grid(True)
	plt.show()

def main(data_file, degree, x_min, x_max, title):
	read_data = readData(data_file)
	x_values = read_data[0]
	y_values = read_data[1]
	std = read_data[2]
	equation = getEquation(x_values, y_values, degree)

	plot(equation, x_min, x_max, x_values, y_values, std, title)
	

if __name__ == "__main__":
	main('sample data/wt.csv', 4, 0, 330, "Wildtype Cilium Regrowth")
	main('sample data/pf18.csv', 6, 0, 360, "PF18 Cilium Regrowth")
