## Import all the required libraries
import cv2
import os


def get_ouput_image(original_image_path: str, fully_annotated_image_path: str, partially_annotated_image_path: str):
    
    cv2.imwrite(partially_annotated_image_path,partially_annotated_image)