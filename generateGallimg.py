import os

# Path to your image folder
image_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\assets\imgall"

# Output HTML file
output_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\gallery.html"

# Verify the image folder path
print("Image folder path:", os.path.abspath(image_folder))

# Start the HTML output
html_output = """
<section class="gallery">
    <h2 class="text-xl font-bold mb-4">Gallery</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
"""

# Loop through all files in the image folder
for filename in sorted(os.listdir(image_folder)):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        html_output += f'        <img src="assets/imgall/{filename}" alt="{filename}" class="w-full h-auto object-cover rounded">\n'

# Close the HTML
html_output += """
    </div>
</section>
"""

# Write the HTML to a file
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_output)

print(f"HTML gallery saved to {output_file}")