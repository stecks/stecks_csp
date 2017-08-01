#######################################
# Scott Steckel and John Kim


import PIL 
import matplotlib.pyplot as plt
import os.path              




# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
image_file = os.path.join(directory, 'figure_01.png')

# Open and show the student image in a new Figure window
image_02 = PIL.Image.open(image_file)
#image_03=PIL.Image.solarize(image_02, threshold=128) 
image_03=image_02.transpose(PIL.Image.ROTATE_180)

fig, ax = plt.subplots(1, 1)
ax.imshow(image_03, interpolation='none')

fig.show()







