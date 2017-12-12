import matplotlib.pyplot 
from euclideanSimilarity import euclideansimilarity
x_plot=[1,2,3,4,5,6,7,8,9,10]

matplotlib.pyplot.plot(x_plot,euclideansimilarity)
matplotlib.pyplot.xlabel('x-axis')
matplotlib.pyplot.ylabel('y-axis')
matplotlib.pyplot.title('Euclidean Similarity plot')
matplotlib.pyplot.show()