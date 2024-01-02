"""
Sample submission file
"""

import cv2


def submission(file_path):
    """
    Sample submission function

    :param file_path:
    :return:
    """
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    out = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, (3, 3), iterations=5)
    _, thresh = cv2.threshold(out, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    co_ords = []

    for contour in contours:
        moment = cv2.moments(contour)
        center_x = int(moment['m10'] / moment['m00'])
        center_y = int(moment['m01'] / moment['m00'])
        co_ords.append((center_x, 480 - center_y))

    co_ords = sorted(co_ords, key=lambda x: (x[0], x[1]))
    origin = co_ords[0]

    co_ords = [(x - origin[0], y - origin[1]) for (x, y) in co_ords]
    return co_ords[1:]
