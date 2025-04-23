from block_markdown_handler import markdown_to_html_node
from htmlnode import HTMLNode
import os
import shutil

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            #print(f"Found title : {line.lstrip("# ").strip()}")
            return line.lstrip("# ").strip()
        
    raise Exception("Markdown missing title.")



def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    #read file in from_path, store in variable(markdown file)
    with open(from_path, 'r') as file_mark:
        markdown_file = file_mark.read()

    #read file from dest_path and store in variable(template file)
    with open(template_path, 'r') as file_temp:
        template_file = file_temp.read()

    #use markdown_to_html_node() and to_html() to convert markdown file to html string
    html_string = markdown_to_html_node(markdown_file).to_html()    
    #print(f"html_string : {html_string}")

    #use extract_title method above to get title
    title = extract_title(markdown_file)

    #print(f"title : {title}")

    #print(f"tempalte : {template_file}")

    #replace  {{title}} and {{content}} placeholders with html and the title we grabbed
    replaced_template = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace('href="/', "{basepath}").replace('src="/', "{basepath}")    
    
    #create full html file in dest_path and create needed dirs
    dir_name = os.path.dirname(dest_path)
    #print(f"dir name : {dir_name}")
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    

    with open(dest_path, 'w') as copy_file:
        copy_file.write(replaced_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    print(os.listdir(dir_path_content))
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
       
    dir_contents = os.listdir(dir_path_content)
    print(f"gen page dir_contents : {dir_contents} of path {dir_path_content}")
    
    for content in dir_contents:

        cur_path = os.path.join(dir_path_content, content)
        dest_path = os.path.join(dest_dir_path, content)
        
        print(f"cur_path : {cur_path}")
        print(f"dest path : {dest_path}")

        if os.path.isdir(cur_path):            
            print(f"{content} : is dir")            
            generate_pages_recursive(cur_path, template_path, dest_path, basepath)        

        elif os.path.isfile(cur_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(cur_path, template_path, dest_path, basepath)
            print(f"{content} : is file")            
    

    
    

