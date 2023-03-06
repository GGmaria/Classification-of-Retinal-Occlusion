import os
import cv2
import numpy as np

# Define the input and output directories
input_dir = 'F:\Main Project\eye'
output_dir = 'F:\Main Project\eye_aug'

# Define the augmentations to apply
augmentations = [cv2.flip, cv2.rotate]

# Loop through each image in the input directory
for filename in os.listdir(input_dir):
    # Load the image
    img_path = os.path.join(input_dir, filename)
    img = cv2.imread(img_path)

    # Apply each augmentation to the image and save the resulting images to the output directory
    for i, aug in enumerate(augmentations):
        augmented_img = aug(img, 1)
        new_filename = f'{os.path.splitext(filename)[0]}_aug{i}{os.path.splitext(filename)[1]}'
        cv2.imwrite(os.path.join(output_dir, new_filename), augmented_img)
