import matplotlib.pyplot 
from jaccardSimilarity import jaccardsimilarity
x_plot=[1,2,3,4,5,6,7,8,9,10]

matplotlib.pyplot.plot(x_plot,jaccardsimilarity)
matplotlib.pyplot.xlabel('x-axis')
matplotlib.pyplot.ylabel('y-axis')
matplotlib.pyplot.title('Jaccard Similarity plot')
matplotlib.pyplot.show()