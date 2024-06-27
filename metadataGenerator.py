import os
import json
from PIL import Image
import argparse

# Parse the image name and return the metadata
def parse_image_name(image_name):
  return image_name

def get_image_dimensions(image_path):
  with Image.open(image_path) as img:
    return img.width, img.height
  

  