import unittest
import nodes_handler as nd
from textnode import TextNode, TextType


class TestNodeSplitter(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = nd.split_nodes_image([node])        
        #print(f"NEW NODES : {new_nodes}")
        compare_nodes = [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")                                    
            ]
        #print(f"COMPARE NODES : {compare_nodes}")
        self.assertEqual(str(compare_nodes), str(new_nodes))
        #fails, even though both are lists and the below test test_two_lists works np, weird, annoyed, moving on
        #self.assertListEqual(compare_nodes, new_nodes_nodes)

    def test_split_images_image_first(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) This is text with an image first ![second image](https://i.imgur.com/3elNhQu.png) and another.",
            TextType.TEXT,
        )
        new_nodes = nd.split_nodes_image([node])                
        compare_nodes = [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" This is text with an image first ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and another.", TextType.TEXT),
                                                   
            ]        
        self.assertEqual(str(compare_nodes), str(new_nodes))
            
    def test_two_lists(self):
        list1 = ["Yo", "This", "Is", "A", "list"]
        list2 = ["Yo", "This", "Is", "A", "list"]
        self.assertListEqual(list1, list2)

    # def test_no_image(self):
    #     node = [TextNode("This is text node without an image", TextType.TEXT)]
                    
    #     new_nodes = nd.split_nodes_image(node)
    #     self.assertEqual(str(node), str(new_nodes))


    def test_split_links_link_first(self):
        node = TextNode(
            "[youtube link](https://youtube.com/partytime) This is text with a link first [youtube link 2](https://youtube.com/partytimeagain) and another.",
            TextType.TEXT,
        )
        new_nodes = nd.split_nodes_link([node])                
        compare_nodes = [
                TextNode("youtube link", TextType.LINK, "https://youtube.com/partytime"),
                TextNode(" This is text with a link first ", TextType.TEXT),
                TextNode("youtube link 2", TextType.LINK, "https://youtube.com/partytimeagain"),
                TextNode(" and another.", TextType.TEXT),                                                   
            ]        
        self.maxDiff = None
        self.assertEqual(str(compare_nodes), str(new_nodes))
        #self.assertListEqual(compare_nodes, new_nodes)
