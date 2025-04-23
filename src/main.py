from textnode import TextNode, TextType
import os
import shutil
from dir_copy import handle_dir_copy
from generate_page import generate_page, generate_pages_recursive


#./main.sh
#print("hello world")
dir_path_static = "./static"
dir_path_public = "./public/"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    #text_dummy = TextNode("This is a test", TextType.BOLD, "https://boot.dev")    
    #print(text_dummy)

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)    
    
    print(f"copying from {dir_path_static} to {dir_path_public}...")
    handle_dir_copy(dir_path_static, dir_path_public)

    #works
    #os.mkdir("./public/images")
    #shutil.copy("./static/images/tolkien.png", "./public/images/tolkien.png")
    
    #swapped for recursive
    # generate_page(
    #     os.path.join(dir_path_content, "index.md"), 
    #     template_path, 
    #     os.path.join(dir_path_public, "index.html")
    #     )

    print("Generating pages")
    generate_pages_recursive(
        dir_path_content, 
        template_path, 
        dir_path_public #os.path.join(, "content")
        )

main()
