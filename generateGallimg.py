import os
from PIL import Image  # Using Pillow to handle image dimensions

# Path to your image folder
image_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\assets\imgall"

# Path to the template HTML file
template_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\template.html"

# Output HTML file
output_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\layering-realities.html"

# Verify the paths
print("Image folder path:", os.path.abspath(image_folder))
print("Template file path:", os.path.abspath(template_file))

# Read the template file
try:
    with open(template_file, "r", encoding="utf-8") as file:
        template_html = file.read()
except Exception as e:
    print(f"Error reading template file: {e}")
    exit()

# Find the placeholder for images in the template
placeholder = "<!-- Images will be inserted here -->"

if placeholder not in template_html:
    print("Placeholder not found in template file. Please add '<!-- Images will be inserted here -->' to your template.")
    exit()

# Generate the image divs
image_divs = ""
for filename in sorted(os.listdir(image_folder)):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        file_path = os.path.join(image_folder, filename)

        # Open the image to get its dimensions
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                aspect_ratio = width / height

                # Determine if the image is landscape
                landscape_class = "landscape" if width > height else ""

                # Determine if the image is a highlight image
                highlight_class = "highlight" if "hero" in filename.lower() else ""

                # Combine classes
                combined_classes = f"{landscape_class} {highlight_class}".strip()

                # Create the image div
                image_divs += f'        <div data-aspect-ratio="{aspect_ratio:.2f}" class="{combined_classes}">\n'
                image_divs += f'            <img src="assets/imgall/{filename}" alt="{filename}" class="w-full h-auto object-cover rounded">\n'
                image_divs += f'        </div>\n'
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Replace the placeholder with the generated image divs
final_html = template_html.replace(placeholder, image_divs)

# Save the updated HTML to the output file
try:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)
    print(f"HTML gallery saved to {output_file}")
except Exception as e:
    print(f"Error saving HTML file: {e}")