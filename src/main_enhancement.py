# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:42:58 2016

@author: utkarsh
"""

import numpy as np
#import cv2
#import numpy as np;

import scipy.ndimage
import sys
import cv2

import skimage.morphology
import skimage

from getTerminationBifurcation import getTerminationBifurcation
from removeSpuriousMinutiae import removeSpuriousMinutiae
from image_enhance import image_enhance


if(len(sys.argv)<2):
    print('loading sample image');
    img_name = 'parmak izi 1.bmp'
    img = scipy.ndimage.imread('../images/'+img_name);
elif(len(sys.argv) >= 2):
    img_name = sys.argv[1];
    img = scipy.ndimage.imread(sys.argv[1]);
    
if(len(img.shape)>2):
    # img = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    img = np.dot(img[...,:3], [0.299, 0.587, 0.114]);

rows,cols = np.shape(img);
aspect_ratio = np.double(rows)/np.double(cols);

new_rows = 540;             # randomly selected number
new_cols = new_rows/aspect_ratio;

#img = cv2.resize(img,(new_rows,new_cols));
img = scipy.misc.imresize(img,(np.int(new_rows),np.int(new_cols)));

enhanced_img = image_enhance(img);    
"""
if(1):
    print('saving the image')
    scipy.misc.imsave('../enhanced/enhanced.bmp' ,enhanced_img);
else:
    plt.imshow(enhanced_img,cmap = 'Greys_r');
"""
# main.py dosyasından ekleme
if __name__ == "__main__":
    #img = cv2.imread('../enhanced/enhanced.bmp',0);
    #img = scipy.ndimage.imread('../images/'+img_name);
    #img = np.uint8(img>78);
    img =  enhanced_img

    skel = skimage.morphology.skeletonize(img)
    #skel = skimage.morphology.thin(img)
    skel = np.uint8(skel)*255;
    
    mask = img*255;
    (minutiaeTerm, minutiaeBif) = getTerminationBifurcation(skel, mask);
    
    minutiaeTerm = skimage.measure.label(minutiaeTerm, 8);
    RP = skimage.measure.regionprops(minutiaeTerm)
    minutiaeTerm = removeSpuriousMinutiae(RP, np.uint8(img), 23);
    
    BifLabel = skimage.measure.label(minutiaeBif, 8);
    TermLabel = skimage.measure.label(minutiaeTerm, 8);

    
    
    minutiaeBif = minutiaeBif * 0;
    minutiaeTerm = minutiaeTerm * 0;
    
    (rows, cols) = skel.shape
    DispImg = np.zeros((rows,cols,3), np.uint8)
    DispImg[:,:,0] = skel; DispImg[:,:,1] = skel; DispImg[:,:,2] = skel;
    
    
    RP = skimage.measure.regionprops(BifLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeBif[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (255,0,0));
    
    
    RP = skimage.measure.regionprops(TermLabel)
    for i in RP:
        (row, col) = np.int16(np.round(i['Centroid']))
        minutiaeTerm[row, col] = 1;
        (rr, cc) = skimage.draw.circle_perimeter(row, col, 3);
        skimage.draw.set_color(DispImg, (rr,cc), (0, 0, 255));
    
        (rows, cols) = img.shape;
    file1 = open("data.txt","a")
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            if(minutiaeTerm[i][j] == 1):
                file1.write("end\t"+str(i)+" "+str(j)+"\r\n")
            elif(minutiaeBif[i,j] == 1):
                file1.write("bif\t"+str(i)+" "+str(j)+"\r\n")
    file1.close()
    cv2.imshow('a',DispImg);
    scipy.misc.imsave('../enhanced/Minutiae.bmp' ,DispImg);
    cv2.waitKey(0)