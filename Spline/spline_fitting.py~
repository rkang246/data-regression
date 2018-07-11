#A sample python script that fits a spline to a set of data and #replots that data with a set domain.

from scipy import interpolate
import matplotlib.pyplot as plt

def plot(data_file):
	fp = open(data_file)

	x_points = []
	y_points = []

	#Read data
	for line in fp:
		line = line.strip()
		line = line.decode('utf-8-sig').encode('utf-8')
		row = line.split(',')
		x_points.append(row[0])
		y_points.append(row[1])
	
	#Spline Function
	def f(x):
		tck = interpolate.splrep(x_points, y_points,w=None,k=2)
		return interpolate.splev(x, tck)

	#The set of data to be replotted
	x = []
	y = []

	for i in range(0, 331):
		x.append(i)
		y.append(f(i))

	plt.title(data_file)
	plt.plot(x, y)
	plt.show()

plot('sample data/wt.csv')

