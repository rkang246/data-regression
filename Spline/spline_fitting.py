#!/usr/bin/env python2
#
# ======================================================
#	Program:	spline_fitting.py
#	Author:		Robert Kang
#			(rkang246@gmail.com)
#	Created:	2018-07-11
#	Modified	2018-07-12
# ------------------------------------------------------
# Use: To plot a set of data and fit curve with
#      spline function fitting
# ======================================================
#

from scipy import interpolate
import matplotlib.pyplot as plt

def readData(data_file):
	"""
	Reads the data from the input file
	
	Args:
		data_file: data_file: A file in csv format with
			   "x,y" for each row

	Returns:
		A 2D list x_y such that x_y[0] contains the
		x-values of the data_file and x_y[1] contains
		the y-values of the data_file.
	"""
	fp = open(data_file)
	x_y = [[], []]

	for line in fp:
		line = line.strip()
		line = line.decode('utf-8-sig').encode('utf-8')
		row = line.split(',')
		x_y[0].append(row[0])
		x_y[1].append(row[1])

	return x_y


def weight(x_points, y_points):
	"""
	Generates the weighting for the spline fitting.
	
	Args:
		x_points: A float array of x-values
		y_points: A float array of y-values
	
	Returns:
		A float array of weights based on the
		y-value's distance from the average.
	"""
	avg = 0
	wt = []
	for i in y_points:
		avg += float(i)
	avg /= len(y_points)
	for i in y_points:
		wt.append(abs(float(i) - avg))
	return wt


def f(x, x_points, y_points, wt):
	"""
	Performs spline fitting based off of a given set
	of data.
	
	Args:
		x: An integer x-value to best fit
		x_points: A float array of x-values
		y_points: A float array of y-values
		wt: A float array of weights
	
	Returns:
		A float y-value that corresponds to the
		inputted x-value using the spline fit
	"""
	tck = interpolate.splrep(x_points, y_points,w=wt,k=2)
	return interpolate.splev(x, tck)


def plot(x_points, y_points, wt, rangeMin, rangeMax, data_file):
	"""
	Plots a set of data in a given range using 
	spline fitting
	
	Args:
		x_points: A float array of x-values
		y_points: A float array of y-values
		wt: A float array of weights
		rangeMin: An integer starting value for
			  the domain to be plot
		rangeMax: An integer ending value for
			  the domain to be plot
		data_file: A file in csv format with
			   "x,y" for each row
	
	Returns:
		none
		
	"""
	x = []
	y = []

	for i in range(rangeMin, rangeMax + 1):
		x.append(i)
		y.append(f(i, x_points, y_points, wt))

	plt.title(data_file)
	plt.plot(x, y)
	plt.show()


def main(data_file, rangeMin, rangeMax):

	read_data = readData(data_file)
	x_points = read_data[0]
	y_points = read_data[1]

	wt = weight(x_points, y_points)

	plot(x_points, y_points, wt, rangeMin, rangeMax, data_file)


if __name__ == "__main__":
	main('sample data/wt.csv', 0, 330)

