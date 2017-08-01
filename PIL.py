#######################################
# Scott Steckel and John Kim


import PIL 
import matplotlib.pyplot as plt
import os.path              




# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
image_file = os.path.join(directory, 'world.png')





# Open and show the  image in a new Figure window
#image_01 = PIL.Image.open(image_file)
image_01=plt.imread(image_file)






col=len(image_01[0])
row=len(image_01)

print ("row is "+str(row))
print ("col is "+str(col))

for row in range(0,315):
   for col in range(0,315):
       if image_01[row][col][0]*255>230:
          image_01[row][col]=[226/255.,226/255.,225/255.]
       else:
          image_01[row][col]=[1,1,1]


            
            
fig, axes = plt.subplots(1, 1)
axes.imshow(image_01, interpolation='none')

# Display student in second axes and set window to the 
    

im = PIL.Image.new("RGB",(315,630),"white")

# Change each pixel

fig.show()
fig.savefig('figure_01.png')









# Open, resize, and display earth
#earth_file = os.path.join(directory, 'earth.png')
#earth_img = PIL.Image.open(earth_file)
#earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
#fig2, axes2 = plt.subplots(1, 2)
#axes2[0].imshow(earth_img)
#axes2[1].imshow(earth_small)
#fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
#student_img.paste(earth_small, (1162, 966), mask=earth_small) 
# Display
#fig3, axes3 = plt.subplots(1, 2)
#axes3[0].imshow(student_img, interpolation='none')
#axes3[1].imshow(student_img, interpolation='none')
#axes3[1].set_xlim(500, 1500)
#axes3[1].set_ylim(1130, 850)
#fig3.show()