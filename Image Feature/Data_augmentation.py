# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:04:32 2020

@author: USER
"""



import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib

image = imageio.imread("car.jpg")
ia.imshow(image)

flip_hr=iaa.Fliplr(p=1.0)
flip_hr_image= flip_hr.augment_image(image)
ia.imshow(flip_hr_image)



rotate=iaa.Affine(rotate=(-50, 30))
rotated_image=rotate.augment_image(image)
ia.imshow(rotated_image)


shear = iaa.Affine(shear=(0,40))
shear_image=shear.augment_image(image)
ia.imshow(shear_image)


crop = iaa.Crop(percent=(0, 0.3)) # crop
corp_image=crop.augment_image(image)
ia.imshow(corp_image)

scale_im=iaa.Affine(scale={"x": (1.5, 1.0), "y": (1.5, 1.0)})
scale_image =scale_im.augment_image(image)
ia.imshow(scale_image)


contrast=iaa.GammaContrast(gamma=2.0)
contrast_image =contrast.augment_image(image)
ia.imshow(contrast_image)

