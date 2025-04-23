import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(str(node1), str(node2))
        #self.assertEqual(2, 2) #works


    def test_text_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(str(node1), str(node2))
    
    def test_text_type_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(str(node1), str(node2))
    
    def test_url_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://test.com/games")
        self.assertNotEqual(str(node1), str(node2))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        #html_node = node.text_node_to_html_node(node)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_text_italic(self):
        node = TextNode("This is a italic text node", TextType.ITALIC)
        #html_node = node.text_node_to_html_node(node)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic text node")
    
    def test_text_code(self):
        node = TextNode("This is a code text node", TextType.CODE)
        #html_node = node.text_node_to_html_node(node)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_text_link(self):
        node = TextNode("This is a link text node", TextType.LINK, "http://this-is-a-link.com")
        #html_node = node.text_node_to_html_node(node)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props["href"], "http://this-is-a-link.com")

    def test_text_image(self):
        node = TextNode("This is an image alt text node", TextType.IMAGE, "image.png")
        #html_node = node.text_node_to_html_node(node)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["alt"], "This is an image alt text node")
        self.assertEqual(html_node.props["src"], "image.png")

    # def test_text_invalid_node(self):
    #     node = TextNode("candy node", None)
    #     html_node = node.text_node_to_html_node(node)
    #     self.assertRaises(Exception("Not a valid TextType"))
    

if __name__ == "__main__":
    unittest.main()

