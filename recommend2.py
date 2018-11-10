import glob
import random
from PIL import Image

folders = glob.glob('hermitage/*')

folders = list(map(lambda x: x.strip('hermitage/'), folders))

n = len(folders)

default_prob = 1 / len(folders)

probability = [default_prob for i in range(n)]

prediction_rate = 0.05

command = ''

while 1:
    chosed = random.choices(folders, weights=probability)[0]
    print(chosed)
    path = 'hermitage/' + chosed
    images = glob.glob(path + '/*.jpg')
    image = images[random.randint(0, len(images) - 1)]
    img = Image.open(image)
    img.show()
    command = input()
    if command == 'like':
        for w in probability:
            w += -prediction_rate/(n-1)
        w[w.index(chosed)] += prediction_rate + prediction_rate/(n-1)
    elif command == 'dislike':
        for w in probability:
            w += prediction_rate/(n-1)
        w[w.index(chosed)] += -prediction_rate - prediction_rate/(n-1)
    else:
        break





