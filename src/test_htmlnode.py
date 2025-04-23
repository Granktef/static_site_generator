import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        node1 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )
        node2 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )                

        self.assertEqual(str(node1), str(node2))

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )


    def test_props_to_html_eq(self):
        node1 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )
        node2 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )
        
        self.assertEqual(node1.props_to_html(), node2.props_to_html())


    #not equal props 
    def test_props_to_html_not_eq(self):
        node1 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev/spells/enchanter"}
            )
        node2 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev/spells/wizard"}
            )
        
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())


    #not equal tag
    def test_tag_not_eq(self):
        node1 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )
        node2 = HTMLNode(
            "div", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )                

        self.assertNotEqual(str(node1), str(node2))


    #not equal value
    def test_value_not_eq(self):
        node1 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )
        node2 = HTMLNode(
            "p", 
            "this is a different test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )                

        self.assertNotEqual(str(node1), str(node2))


    #not equal children
    def test__children_not_eq(self):

        child_node = HTMLNode(
            "p", 
            "candy corn is gross",
            None,
            {"href": "https://www.boot.dev/events"}
            )

        node1 = HTMLNode(
            "p", 
            "this is a test paragraph",
            child_node,
            {"href": "https://www.boot.dev"}
            )
        node2 = HTMLNode(
            "p", 
            "this is a test paragraph",
            None,
            {"href": "https://www.boot.dev"}
            )                

        self.assertNotEqual(str(node1), str(node2))    

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

if __name__ == "__main__":
    unittest.main()