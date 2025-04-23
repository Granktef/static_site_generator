import unittest

import nodes_handler as ndh
from textnode import TextNode, TextType




class TestNodeHandler(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = ndh.split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(str(new_nodes[0]), "TextNode(This is text with a , text, None)")
        self.assertEqual(str(new_nodes[1]), "TextNode(code block, code, None)")
        self.assertEqual(str(new_nodes[2]), "TextNode( word, text, None)")


    #test bold **
    def test_eq_bold(self):
        node = TextNode("This is text with a **bold is gold** word", TextType.TEXT)
        new_nodes = ndh.split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(str(new_nodes[0]), "TextNode(This is text with a , text, None)")
        self.assertEqual(str(new_nodes[1]), "TextNode(bold is gold, bold, None)")
        self.assertEqual(str(new_nodes[2]), "TextNode( word, text, None)")

    #test italic _
    def test_eq_italic(self):
        node = TextNode("This is text with a _italic fun_ word", TextType.TEXT)
        new_nodes = ndh.split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(str(new_nodes[0]), "TextNode(This is text with a , text, None)")
        self.assertEqual(str(new_nodes[1]), "TextNode(italic fun, italic, None)")
        self.assertEqual(str(new_nodes[2]), "TextNode( word, text, None)")


    #test no matching delimiter in TextNode.text
    def test_eq_missing_matching_delimiter(self):
        node = TextNode("This is text with a _missing closing delimiter word", TextType.TEXT)
        
        with self.assertRaises(Exception) as context:
            new_nodes = ndh.split_nodes_delimiter([node], "_", TextType.ITALIC)        



    #test multiple delimited TextNode
    #I am the **fart** king **bow** to mah gas
    def test_eq_multi_delimited_sections(self):
        node = TextNode("I am the **fart** king **bow** to mah gas", TextType.TEXT)
        new_nodes = ndh.split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(str(new_nodes[0]), "TextNode(I am the , text, None)")
        self.assertEqual(str(new_nodes[1]), "TextNode(fart, bold, None)")
        self.assertEqual(str(new_nodes[2]), "TextNode( king , bold, None)")
        self.assertEqual(str(new_nodes[3]), "TextNode(bow, bold, None)")
        self.assertEqual(str(new_nodes[4]), "TextNode( to mah gas, text, None)")



    #test repetitive code edge case noted in split_nodes_delimiter()

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = ndh.text_to_textnodes(text)                
        compare_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]        
        self.maxDiff = None
        self.assertEqual(str(compare_nodes), str(new_nodes))



