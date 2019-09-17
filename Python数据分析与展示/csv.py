#csv
import numpy as np
a = np.arange(24).reshape(4,6)
np.savetxt("a.csv", a, fmt = "%d", delimiter=',')
money = np.random.rand(5, 10)*1000
np.savetxt("money.csv", money, fmt="%.2f", delimiter="$ ")

a.tofile("a1.csv", format = "%d", sep = ",")
a.tofile("a2.csv", sep = ",")
