#!/usr/bin/env python2
#
# ======================================================
#	Program:	plot_data.py
#	Author:		Robert Kang
#			(rkang246@gmail.com)
#	Created:	2018-08-01
#	Modified	2018-08-01
# ------------------------------------------------------
# Use: To plot a set of data and connect each data point
#      with a simple line.
# ======================================================
#

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

def plot(x_values, y_values, std, title):
	"""
	Plots a set of data with error bars.
	
	Args:
		x_values: A float array of x-values
			  used for error bar purposes
		y_values: A float array of y-values
			  used for error bar purposes
		std: The standard deviation error.
		title: The string graph title
	
	Returns:
		none
	"""
	plt.plot(x_values, y_values, color='blue')

	plt.errorbar(x_values, y_values, yerr=std, fmt='o')

	plt.title(title)
	plt.xlabel("Time (Minutes)")
	plt.ylabel("Length (Microns)")
	plt.grid(True)
	plt.show()

def main(data_file, title):
	read_data = readData(data_file)
	x_values = read_data[0]
	y_values = read_data[1]
	std = read_data[2]

	plot(x_values, y_values, std, title)

	

if __name__ == "__main__":
	main('sample data/wt.csv', "Wildtype Cilium Regrowth")
	main('sample data/pf18.csv', "PF18 Cilium Regrowth")
