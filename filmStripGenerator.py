import os
from PIL import Image
import argparse

# Parse the image name and return the image number and channel
def parse_image_name(image_name):
  parts = image_name.split('_')
  if len(parts) < 2:
    return None, None
  
  image_number = parts[0]
  channel = parts[1].split('.')[0]

  return image_number, channel

def main(input_path, output_path):
  images_by_channel = {}

  for filename in os.listdir(input_path):
    if filename.endswith('.png'):
      image_number, channel = parse_image_name(filename)
      if channel:
        image_path = os.path.join(input_path, filename)
        image = Image.open(image_path)
        if channel not in images_by_channel:
          images_by_channel[channel] = []
        images_by_channel[channel].append((int(image_number), image))

  os.makedirs(output_path, exist_ok=True)

  # Create a film strip for each channel
  for channel, images in images_by_channel.items():
    images.sort(key=lambda x: x[0])

    total_width = sum(img.width for _, img in images)
    max_height = max(img.height for _, img in images)

    # Create a new blank image with the total width and max height
    new_image = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for _, img in images:
      new_image.paste(img, (x_offset, 0))
      x_offset += img.width

    output_image_path = os.path.join(output_path, f'{channel}_filmstrip.png')
    new_image.save(output_image_path)

  print('Filmstrip created and saved')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Combine images into horizontal strips by channel.')
  parser.add_argument('-i', '--input_path', type=str, required=True, help='Path topath containing the original images')
  parser.add_argument('-o', '--output_path', type=str, required=True, help='Path to the folder for storing the output images')
  args = parser.parse_args()
  main(args.input_path, args.output_path)
