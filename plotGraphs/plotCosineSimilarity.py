import matplotlib.pyplot
x_axis = [0.02048, 0.03337, 0.0181, 0.01446, 0.02106, 0.02456, 0.01584, 0.02113, 0.01306, 0.01409]
y_axis = [0,1,2,3,4,5,6,7,8,9]
unique=set()
for i in x_axis:
	unique.add(i)
print(len(unique))