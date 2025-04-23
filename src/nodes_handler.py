import re
from textnode import TextNode, TextType

def text_to_textnodes(text):    
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_image(old_nodes):    
    new_nodes = []
    special_delimiter_full = "-||-"
    special_delimiter_half = "-|"
    for node in old_nodes:        
        images = extract_markdown_images(node.text)
        #print(f"images : {images}")
        #no images, just return node as is in a list
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        replaced = node.text
        for image in images:
            replaced = replaced.replace(f"![{image[0]}]({image[1]})", "-||-")
        #print(f"replaced : {replaced}")

        split_replaced = replaced.split("|-")
        #print(f"split_replaced : {split_replaced}")

        for piece in split_replaced:
            if piece[-2:] == special_delimiter_half and piece.replace(special_delimiter_half, "") == "":
                new_nodes.append(TextNode(f"{images[0][0]}", TextType.IMAGE, f"{images[0][1]}"))
            elif piece[-2:] == special_delimiter_half:
                new_nodes.append(TextNode(piece[:-2], TextType.TEXT))
                new_nodes.append(TextNode(f"{images[0][0]}", TextType.IMAGE, f"{images[0][1]}"))                
            elif piece.strip() != "":
                new_nodes.append(TextNode(piece, TextType.TEXT))
            
            images = images[1:]

        # for nod in new_nodes:
        #     print(f"new nod : {nod}")
    return new_nodes
            

#boot dev solution        
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        #print(f"links : {links}")

        if len(links) == 0:
            new_nodes.append(node)
            continue
        node_text = node.text
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            #print(f"sections : {sections}")
                            
            if sections[0].strip() != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(f"{link[0]}", TextType.LINK, f"{link[1]}"))
                       
            node_text = sections[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.TEXT))
    
    # for nod in new_nodes:
    #     print(f"new nod : {nod}")

    return new_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []

    # print(f"old nodes : {old_nodes}")
    for node in old_nodes:
        # print(f"oldy : {node}")
        # print(f"oldy text : {node.text}")
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        #if we have an odd number of delimiters we are missing part of the pair
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown, no matching delimiter found")
            #raise ValueError("invalid markdown, no matching delimiter found")
        #parse parts
        parts = node.text.split(delimiter)    
        #print(f"mah parts : {parts}")    
        for part in parts:
            #NOTE - misses repetitive edge cases like **a** and a
            if f"{delimiter}{part}{delimiter}" in node.text:
                #print("delimiter match")
                new_nodes.append(TextNode(part, text_type))
            else:
                #print("delimiter NOT match")
                new_nodes.append(TextNode(part, TextType.TEXT))

    #print(f"mah NEW nodes : {new_nodes}")

    return new_nodes





def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    #!\[([^\[\]]*)\]\(([^\(\)]*)\) # from boot.dev solution
    #!\[(\w+)\] #my soution for [image] part
    #\((.*?)\) #my solution for (image url) part
    #print(f"image matches = {matches}")
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    #print(f"link matches = {matches}")
    return matches
    

