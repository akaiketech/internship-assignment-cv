## Import all the required libraries
import cv2
import os
import numpy as np


def get_ouput_image(original_image_path: str, fully_annotated_image_path: str, partially_annotated_image_path: str): import cv2
           gray_image = cv2.cvtColor(fully_annotated_image_path, cv2.COLOR_BGR2GRAY)
           edged = cv2.Canny(gray_image, 30, 120)
           contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
           largest_contour = None
           max_dimension = 0
           for contour in contours:
                 x, y, w, h = cv2.boundingRect(contour) # Calculate the maximum dimension of the bounding rectangle
                 dimension = max(w, h)
                 if dimension > max_dimension:
                         largest_contour = contour
                         max_dimension = dimension
           mask = np.zeros_like(gray_image)
           cv2.drawContours(mask, [largest_contour], -1, (255), thickness=cv2.FILLED)
           mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
           result_image = cv2.bitwise_and(fully_annotated_image, mask_color)
           plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
           plt.axis('off')
           plt.show()
get_output_image(original_image, fully_annotated_image, partially_annoted_image)
