#how to use
copy your file into images and change it name as "parmak izi.bmp"

run the main_enhancement.py file
You will see output images in enhance file
The coordinates of minutiaes are in src/data.txt

please dont forget to delete data.txt file. I didnt add code for clean it.
# Fingerprint-Enhancement-Python

Uses oriented gabor filter bank to enhance the fingerprint image. The orientation of the gabor filters is decided by the orientation of ridges in the input image. 

## Results
![temp](https://cloud.githubusercontent.com/assets/13918778/25770604/637b3f38-31ee-11e7-818f-1f8359c96e07.jpg)
## Running the tests

1) go into the src folder

2) run the following command:
  
  python main_enhancement.py
  
3) The sample images are stored in the "images" folder

4) The enhanced image will be stored in the "enhanced" folder

## Theory
- We use oriented gabor filters to enhance a fingerprint image. The orientation of the gabor filters are based on the orientation of the ridges. the shape of the gabor filter is based on the frequency and wavelength of the ridges.

## License
- This project is licensed under the BSD 2 License - see the LICENSE.md file for details

## Acknowledgements
- This program is based on the paper: Hong, L., Wan, Y., and Jain, A. K. 'Fingerprint image enhancement: Algorithm and performance evaluation'. IEEE Transactions on Pattern Analysis and Machine Intelligence 20, 8 (1998), pp 777-789.

- The author would like to thank Dr. Peter Kovesi (This code is a python implementation of his work)

# FingerprintFeatureExtraction
The important fingerprint minutiae features are the ridge endpoints (a.k.a. Terminations) and Ridge Bifurcations.

![image](https://user-images.githubusercontent.com/13918778/35665327-9ddbd220-06da-11e8-8fa9-1f5444ee2036.png)

The feature set for the image consists of the location of Terminations and Bifurcations and their orientations

use the code https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python to enhance the fingerprint image.
This program takes in the enhanced fingerprint image and extracts the minutiae features.

Here are some of the outputs:


![1](https://user-images.githubusercontent.com/13918778/35665568-ae1fdb6c-06db-11e8-937b-33d7445c931d.jpg)   ![enhanced_feat1](https://user-images.githubusercontent.com/13918778/35665578-baddaf82-06db-11e8-8638-d24de65acd31.jpg)

