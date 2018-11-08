import cv2
import glob
from datetime import datetime

i=0
base_directory = './downloaded_images/'
total_files=len(glob.glob('./downloaded_images/*.jpg'))
print(total_files)
start_time = datetime.now()
for i in range(total_files):
    try:
        img = cv2.imread(base_directory+'image_'+str(i)+'.jpg')
    # cv2.imshow('Image',img)
        img = img[0:36, 74:388]
        cv2.imwrite('./cropped_images/img_'+str(i)+'.jpg', img)
    except:
        print('Image {0} is not present in the Downloaded Images'.format(i))
        continue
end_time = datetime.now()
total_time = end_time-start_time
print('Cropped {0} images in {1} seconds'.format(total_files, total_time))