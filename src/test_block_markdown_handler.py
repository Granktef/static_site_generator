import unittest
import block_markdown_handler as bmh
from block_markdown_handler import BlockType

class TestBlockMarkdownHandler(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = bmh.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_heading(self):
        block1 = "# I am a heading yo!"
        block2 = "## I am a heading yo!"
        block3 = "### I am a heading yo!"
        block4 = "#### I am a heading yo!"
        block5 = "##### I am a heading yo!"
        block6 = "###### I am a heading yo!"

        block_type1 = bmh.block_to_block_type(block1)
        block_type2 = bmh.block_to_block_type(block2)
        block_type3 = bmh.block_to_block_type(block3)
        block_type4 = bmh.block_to_block_type(block4)
        block_type5 = bmh.block_to_block_type(block5)
        block_type6 = bmh.block_to_block_type(block6)

        self.assertEqual(block_type1, BlockType.HEADING)
        self.assertEqual(block_type2, BlockType.HEADING)
        self.assertEqual(block_type3, BlockType.HEADING)
        self.assertEqual(block_type4, BlockType.HEADING)
        self.assertEqual(block_type5, BlockType.HEADING)
        self.assertEqual(block_type6, BlockType.HEADING)

    def test_block_to_block_heading_fail(self):
        block = "####### I am not a heading yo!"
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_code(self):
        block = "``` Hello code block ```"
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_code_fail(self):
        block = "`` Hello code block ``"
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)    

    def test_block_to_block_quote(self):
        block = "> Welcome Quote block "
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)  

    def test_block_to_block_quote_multi(self):
        block = "> Welcome Quote block \n> Another block Quote \n> One more for three."
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE) 

    def test_block_to_block_quote_fail(self):
        block = "> Welcome Quote block \n< Woops, should fail"
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH) 
        
    def test_block_to_block_unordered_multi(self):
        block = "- No ORDER here bud \n- NONE !"
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)  
    
    def test_block_to_block_ordered_single(self):
        block = "1. Hey single ordered list block "
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST) 

    def test_block_to_block_ordered_multi(self):
        block = "1. Sup multi ordered list block \n2. Next one \n3. Gross number three "
        block_type = bmh.block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST) 



    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = bmh.markdown_to_html_node(md)
        print(f"node from call : {node}")

        html = node.to_html()
        print(f"html from call : {html}")
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )