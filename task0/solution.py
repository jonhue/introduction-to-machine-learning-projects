import numpy as np

data = np.genfromtxt('test.csv', delimiter=',')
ys = np.mean(data[1:,1:], axis=1)
output = np.hstack((data[1:,0].reshape(-1, 1), ys.reshape(-1, 1)))
np.savetxt('output.csv', output, delimiter=',', header='Id,y', comments='')
