import numpy as np
from PIL import Image

from keras.models import load_model

from settings import *

model = load_model('palm_model.mdl')
fname = 'data/ 5.jpg'

X = np.array(
    Image.open(fname).resize((IMG_WIDTH, IMG_HEIGHT)).getdata(),
    np.uint8,
).reshape(1, IMG_WIDTH, IMG_HEIGHT, 3) / 255
prediction = model.predict(X)[0]
love = prediction[0]
job = prediction[1]
health = prediction[2]
print(love, job, health)
