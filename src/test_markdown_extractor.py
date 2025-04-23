import unittest
import nodes_handler as nd

class TestMarkdownExtractor(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = nd.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multi(self):
        matches = nd.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://i.imgur.com/AAAAAAA.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://i.imgur.com/AAAAAAA.png")], matches)

    def test_extract_markdown_links(self):
        matches = nd.extract_markdown_links(
            "This is text with an [to youtube](https://youtube.com/bears)"
        )
        self.assertListEqual([("to youtube", "https://youtube.com/bears")], matches)