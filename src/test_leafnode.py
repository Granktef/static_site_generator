import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_eq(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_not_eq(self):
        node = LeafNode("p", "Hello, world!")
        self.assertNotEqual(node.to_html(), "<p>Goodbye, world!</p>")
    
    def test_multichar_tag_eq(self):
        node = LeafNode("h1", "Big Ol Title")
        self.assertEqual(node.to_html(), "<h1>Big Ol Title</h1>")

    def test_no_tag_eq(self):
        node = LeafNode(None, "no tag here")
        self.assertEqual(node.to_html(), "no tag here")
    
    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError)
    

