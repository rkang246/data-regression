#Reads from file
#csv x,y
file_object = open("test_data.csv", "r")

data = []

for line in file_object.readlines():
	if len(line) != 1:
		data.append(line.split(","))

file_object.close()

def mean(dt):
	s = 0
	for i in dt:
		try:
			s += float(i)
		except ValueError, e:
			print e

	return s / len(dt)
m = 0
den = 0
x_avg = mean([i[0] for i in data])
y_avg = mean([i[1] for i in data])

for i in range(0, len(data)):
	m += (float(data[i][0]) - x_avg) * (float(data[i][1]) - y_avg);
	den += (float(data[i][0]) - x_avg)**2

m /= den

b = y_avg - m * x_avg

equation = "y = " + str(m) + "x + " + str(b)
print "Linear Regression:", equation

		

