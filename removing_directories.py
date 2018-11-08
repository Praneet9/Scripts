import os
import shutil
import string
import glob

total_images = 0
directories = string.ascii_uppercase
for i in directories:
    # shutil.rmtree(i)
    length = len(glob.glob('training_programs/data/test/'+i+'/*.jpg'))
    total_images += length
    print(str(i)+' : '+str(length))
print('Total Images in the directory is: ', total_images)