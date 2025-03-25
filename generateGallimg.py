import os
from PIL import Image  # Using Pillow to handle image dimensions
from bs4 import BeautifulSoup  # For parsing the HTML content of the blog posts

# Paths
image_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\assets\imgall"
blog_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\blog"
template_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\template.html"
output_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\layering-realities.html"

# Read the template file
try:
    with open(template_file, "r", encoding="utf-8") as file:
        template_html = file.read()
except Exception as e:
    print(f"Error reading template file: {e}")
    exit()

# Placeholders
image_placeholder = "<!-- Images will be inserted here -->"
blog_placeholder = "<!-- Blog links will be inserted here -->"
overview_placeholder = "<!-- Blog summaries will be inserted here -->"

# Verify placeholders in the template
if image_placeholder not in template_html or blog_placeholder not in template_html:
    print("Placeholders not found in template file. Please add them.")
    exit()

# Generate image divs for the gallery
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

# Generate blog links and summaries
blog_links = ""
blog_summaries = ""
for filename in sorted(os.listdir(blog_folder)):
    if filename.lower().endswith(".html"):
        blog_file_path = os.path.join(blog_folder, filename)

        # Open the blog post HTML and parse with BeautifulSoup
        try:
            with open(blog_file_path, "r", encoding="utf-8") as blog_file:
                blog_html = blog_file.read()
                soup = BeautifulSoup(blog_html, "html.parser")

                # Extract the title and first paragraph for the summary
                title = soup.title.string.strip() if soup.title else "Untitled"
                first_paragraph = soup.find("p").get_text().strip() if soup.find("p") else "No summary available."

                # Create a link and summary
                blog_links += f'<li><a href="blog/{filename}">{title}</a></li>\n'
                blog_summaries += f'<p><strong>{title}</strong>: {first_paragraph}</p>\n'

        except Exception as e:
            print(f"Error processing blog post {filename}: {e}")

# Replace placeholders in the template with generated content
final_html = template_html.replace(blog_placeholder, f"<ul>\n{blog_links}</ul>")
final_html = final_html.replace(overview_placeholder, blog_summaries)
final_html = final_html.replace(image_placeholder, image_divs)

# Save the updated HTML to the output file
try:
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(final_html)
    print(f"Updated HTML file saved to {output_file}")
except Exception as e:
    print(f"Error saving updated HTML file: {e}")
