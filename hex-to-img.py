import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import re

width = 2
height = 2

string = "001122abcdef000000ffffff"

data = re.findall('......', string)

imgRGB = []

for h in data:
    # rgb = matplotlib.colors.to_rgb(h)
    imgRGB.append(h)

# print(imgRGB)

# data = list(map(lambda x: list(x), np.reshape(imgRGB, (width, height))))

data = np.random.random(size=(width, height))
# data[0][0] = 0

print(matplotlib.colors.to_hex(data))

print(data, type(data))

plt.imshow(np.real(data), interpolation='nearest')

plt.savefig('output.png', dpi=100)