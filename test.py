# Import the necessary modules
import numpy as np
from PIL import Image

# Create a function to generate the image
def generate_image(grid):
  # Initialize an empty array to store the pixel values
  pixels = np.zeros((12, 12), dtype=np.uint8)
  
  # Loop over the grid
  for i in range(12):
    for j in range(12):
      # If the character is a "w", set the corresponding pixel value to 255 (white)
      if grid[i][j] == 'w':
        pixels[i][j] = 255
  
  # Create an image from the pixel values
  img = Image.fromarray(pixels)
  
  # Return the image
  return img

# Define the grid of characters
grid = [  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'b', 'b', 'b', 'b', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'b', 'w', 'w', 'w', 'w', 'b', 'w', 'w', 'w'],
  ['w', 'w', 'b', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'w', 'w'],
  ['w', 'b', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'w'],
  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
  ['b', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b'],
  ['w', 'b', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'w'],
  ['w', 'w', 'b', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'w', 'w'],
  ['w', 'w', 'w', 'b', 'w', 'w', 'w', 'w', 'b', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'b', 'b', 'b', 'b', 'w', 'w', 'w', 'w'],
  ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
]
# Generate the image
img = generate_image(grid)

# Show the image
img.show()

img.save('test.png')