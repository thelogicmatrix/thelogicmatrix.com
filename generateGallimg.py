import os
from bs4 import BeautifulSoup  # To parse blog posts
from PIL import Image  # Using Pillow to handle image dimensions

# Paths
blog_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\blog"  # Folder where blog posts are stored
gallery_folder = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\assets\imgall"  # Folder for gallery images
output_file = r"C:\Users\Nathan\Documents\GitHub\thelogicmatrix.com\layering-realities.html"  # Main HTML page

# Function to generate the blog list
def generate_blog_list():
    blog_links = ""
    # Get a list of all blog posts (HTML files)
    blog_files = [f for f in os.listdir(blog_folder) if f.endswith('.html')]

    for blog_file_name in blog_files:
        blog_file_path = os.path.join(blog_folder, blog_file_name)

        try:
            # Open and parse the blog post HTML
            with open(blog_file_path, "r", encoding="utf-8") as file:
                blog_html = file.read()
            
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(blog_html, "html.parser")
            
            # Extract title (h1) and description (first paragraph or summary)
            title = soup.find("h1").get_text() if soup.find("h1") else "No Title"
            description = soup.find("p").get_text() if soup.find("p") else "No description available."

            # Generate the blog post list item HTML
            blog_links += f'<ul>\n'
            blog_links += f'    <li class="blog-post">\n'
            blog_links += f'        <a href="blog/{blog_file_name}">\n'
            blog_links += f'            <div class="blog-info">\n'
            blog_links += f'                <h3>{title}</h3>\n'
            blog_links += f'                <p>{description}</p>\n'
            blog_links += f'            </div>\n'
            blog_links += f'        </a>\n'
            blog_links += f'    </li>\n'
            blog_links += f'</ul>\n'

        except Exception as e:
            print(f"Error processing blog post {blog_file_name}: {e}")
    
    return blog_links

# Function to generate the gallery
def generate_gallery():
    gallery_images = ""
    for filename in os.listdir(gallery_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            file_path = os.path.join(gallery_folder, filename)

            try:
                # Open the image to get its dimensions
                with Image.open(file_path) as img:
                    width, height = img.size
                    aspect_ratio = width / height

                    # Generate the gallery image div
                    gallery_images += f'        <div data-aspect-ratio="{aspect_ratio:.2f}" class="landscape">\n'
                    gallery_images += f'            <img src="assets/imgall/{filename}" alt="{filename}" class="w-full h-auto object-cover rounded">\n'
                    gallery_images += f'        </div>\n'
            
            except Exception as e:
                print(f"Error processing image {filename}: {e}")
    
    return gallery_images

# Main function to generate the final HTML page
def generate_main_page():
    try:
        # Read the main HTML template
        with open(output_file, "r", encoding="utf-8") as file:
            main_html = file.read()

        # Generate the blog list and gallery images
        blog_html = generate_blog_list()
        gallery_html = generate_gallery()

        # Replace placeholders in the main HTML with the generated content
        main_html = main_html.replace('<!-- Blog links and summaries will be inserted here -->', blog_html)
        main_html = main_html.replace('<!-- Images will be inserted here -->', gallery_html)

        # Save the final HTML page
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(main_html)
        print(f"Main page generated: {output_file}")
    
    except Exception as e:
        print(f"Error generating main page: {e}")

# Call the function to generate the main page
generate_main_page()
