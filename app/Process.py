from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt


def emotion_analysis(emotions):
    plt.bar(y_pos, emotions, align="center", alpha=0.9)
    plt.tick_params(axis="x", which="both", pad=10, width=4, length=10)
    plt.xticks(y_pos, objects)
    plt.ylabel("percentage")


# instantializing variables
ind = 0
objects = ("angry", "disgust", "fear", "happy", "sad", "surprise", "neutral")
y_pos = np.arange(len(objects)) * 33
imgFile = "nutaj.jpg"

# load the model we saved
model = load_model("model.h5")
model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=["accuracy"])

img = image.load_img(imgFile, grayscale=True, target_size=(48, 48))
show_img = image.load_img(imgFile, grayscale=False, target_size=(200, 200))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

x /= 255

# making the prediction based on our model
custom = model.predict(x)
emotion_analysis(custom[0])

# finding the most likely expression
m = 0.000000000000000000001
a = custom[0]
for i in range(0, len(a)):
    if a[i] > m:
        m = a[i]
        ind = i

plt.title(objects[ind])
print("Expression Prediction:", objects[ind])

plt.gray()
plt.imshow(show_img)
plt.show()
