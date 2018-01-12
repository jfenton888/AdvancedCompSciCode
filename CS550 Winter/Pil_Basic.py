from PIL import Image
import numpy as np

pixels = np.asarray(Image.open('BernerPuppies.jpg'))


avg = pixels.mean(axis=2)
pixels = Image.fromarray(np.uint8(((pixels+25)*-1)*2))

pixels.show()

#img.save('ChowPuppy_butdifferent.png')