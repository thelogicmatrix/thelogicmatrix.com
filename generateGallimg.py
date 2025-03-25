import os
from PIL import Image  # Using Pillow to handle image dimensions

# Paths
image_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\assets\imgall"
template_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\template.html"
output_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\layering-realities.html"

# Read the template file
try:
    with open(template_file, "r", encoding="utf-8") as file:
        template_html = file.read()
except Exception as e:
    print(f"Error reading template file: {e}")
    exit()

# Image placeholder
image_placeholder = "<!-- Images will be inserted here -->"

# Verify image placeholder in the template
if image_placeholder not in template_html:
    print("Image placeholder not found in template file. Please add '<!-- Images will be inserted here -->' to your template.")
    exit()

# Generate image divs
image_divs = ""
for filename in sorted(os.listdir(image_folder)):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        file_path = os.path.join(image_folder, filename)

        # Open the image to get its dimensions
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                aspect_ratio = width / height

                # Determine if the image is landscape or highlight
                landscape_class = "landscape" if width > height else ""
                highlight_class = "highlight" if "hero" in filename.lower() else ""
                combined_classes = f"{landscape_class} {highlight_class}".strip()

                # Create the image div
                image_divs += f'        <div data-aspect-ratio="{aspect_ratio:.2f}" class="{combined_classes}">\n'
                image_divs += f'            <img src="assets/imgall/{filename}" alt="{filename}" class="w-full h-auto object-cover rounded">\n'
                image_divs += f'        </div>\n'
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Replace image placeholder in the template with generated content
final_html = template_html.replace(image_placeholder, image_divs)

# Save the updated HTML to the output file
try:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)
    print(f"Updated HTML file saved to {output_file}")
except Exception as e:
    print(f"Error saving updated HTML file: {e}")
