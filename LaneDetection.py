import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines, color=(0, 255, 0), thickness=3):
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

cap = cv2.VideoCapture('your_video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur and Canny edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Define the region of interest (ROI) vertices
    height, width = frame.shape[:2]
    vertices = np.array([[(0, height), (width/2, height/2 + 50), (width, height)]], dtype=np.int32)

    # Apply the ROI mask
    masked_edges = region_of_interest(edges, vertices)

    # Use the Hough Transform to detect lines
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, 15, minLineLength=40, maxLineGap=20)

    # Create a blank image to draw lines on
    line_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Draw the lines on the blank image
    draw_lines(line_image, lines)

    # Overlay the lane lines on the original frame
    result = cv2.addWeighted(frame, 0.8, line_image, 1, 0)

    # Display the result
    cv2.imshow('Lane Detection', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()