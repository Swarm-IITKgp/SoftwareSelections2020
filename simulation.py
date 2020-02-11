import requests, time
from PIL import Image
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
from api import *

plt.show(block=False)

while True:
    imgplot = plt.imshow(get_Map())
    plt.pause(1)
