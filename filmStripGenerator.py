import os
from PIL import Image

# Parse the image name and return the image number and channel
def parse_image_name(image_name):
  parts = image_name.split('_')
  if len(parts) < 2:
    return None, None
  
  image_number = parts[0]
  channel = parts[1].split('.')[0]

  return image_number, channel

