import os
import sys 
def combine_captions(blip_dir, wd14_dir, output_dir):
  """
  SakuraJensen - https://github.com/SakuraJensen
  Combines BLIP and WD14 captions for all images in the directories.

  Args:
    blip_dir: Directory containing BLIP caption files.
    wd14_dir: Directory containing WD14 caption files.
    output_dir: Directory to store combined caption files.
  """
  # Create output directory if it doesn't exist
  os.makedirs(output_dir, exist_ok=True)

  # Get lists of filenames from both directories
  blip_files = [f for f in os.listdir(blip_dir) if os.path.isfile(os.path.join(blip_dir, f))]
  wd14_files = [f for f in os.listdir(wd14_dir) if os.path.isfile(os.path.join(wd14_dir, f))]

  # Loop through filenames
  for filename in blip_files:
    # Extract image name (assuming consistent naming)
    image_name, _ = os.path.splitext(filename)

    # Check if corresponding WD14 caption file exists
    wd14_file = os.path.join(wd14_dir, f"{image_name}.txt")
    if not os.path.isfile(wd14_file):
      print(f"Warning: WD14 caption not found for image {image_name}")
      continue

    # Read captions from files
    with open(os.path.join(blip_dir, filename), 'r') as f:
      blip_caption = f.read().strip()
    with open(wd14_file, 'r') as f:
      wd14_caption = f.read().strip()

    # Combine captions
    combined_caption = f"{blip_caption}\nWD14: {wd14_caption}"

    # Write combined caption to output file
    output_file = os.path.join(output_dir, f"{image_name}.txt")
    with open(output_file, 'w') as f:
      f.write(combined_caption)

  print(f"Combined captions saved to {output_dir}")

# Check if there are enough arguments provided
if len(sys.argv) != 4:
  print("Usage: python combine_captions.py <blip_dir> <wd14_dir> <output_dir>")
  sys.exit(1)

# Get directory paths from command line arguments
blip_dir = sys.argv[1]
wd14_dir = sys.argv[2]
output_dir = sys.argv[3]

# Call the function with arguments
combine_captions(blip_dir, wd14_dir, output_dir)