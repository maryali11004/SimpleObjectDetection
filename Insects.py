import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'ML-Intro/insect.jpeg'
image = cv2.imread(image_path)
print("Image shape:", image.shape)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Plot histogram of the grayscale image
plt.figure(figsize=(10, 4))
plt.hist(gray_image.ravel(), bins=256, color='gray', alpha=0.7)
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

lower_threshold = 195 
upper_threshold = 197  
# Create a mask where background pixels are set to 0 (black)
background_mask = (gray_image > lower_threshold) & (gray_image < upper_threshold)
background_mask = np.uint8(background_mask) * 255
# Invert the mask to get non-background (insects)
insect_mask = cv2.bitwise_not(background_mask)
# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=insect_mask)
# Convert to grayscale and apply thresholding
gray_segmented_image = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY)
_, thresholded_image = cv2.threshold(gray_segmented_image, 1, 255, cv2.THRESH_BINARY)
# Find contours in the thresholded image
contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Filter out small contours
min_contour_area = 500  
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]
# Count the number of contours (insects)
insect_count = len(contours)
print(f"Number of insects detected: {insect_count}")
# Draw contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title(f"Insects Detected: {insect_count}")
plt.axis('off')
plt.show()
