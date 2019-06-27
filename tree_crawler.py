"""
    The goal: to build the biggest token dictionary in Brazilian Portuguese, and the most important,
    garanting quality.
"""
import typing
import requests


class NodeTree(object):
    def __init__(self, url=None):
        self.child_left = None
        self.child_right = None
        self.url = url
        self.content = None
        self.hash = None
        self.number_node = 0

            
class CrawlerTree(NodeTree):
    """
        We aim to build a beautiful Tree of text's documents from the internet.
        So, expect each node to be a document containing portuguese text.
    """
    def __init__(self):
        super().__init__()
        self.root = NodeTree()

    def number_of_nodes(self):
        return self.number_node
        
    def insert_node(self, url):
        if self.root.url is None:
            self.root.url = url
        elif self.search_node(self.root, url) is None:
            node = NodeTree(url)
            parent = CrawlerTree._search_node(self.root, url)
            if parent.url > node.url:
                parent.child_left = node
            elif parent.url < node.url:
                parent._child_right = node
            self.number_node += 1
        else:
            return None

    @staticmethod
    def _search_node(node, url):
        if node.child_left is not None and node.url > node.child_left.url:
            CrawlerTree._search_node(node.child_left, url)
        elif node.child_right is not None and node.url < node.child_right.url:
            CrawlerTree._search_node(node.child_right, url)
        return node

    def search_node(self, node, url):
        if node.url == url:
            return node
        elif node.child_left is not None and node.url < node.child_left.url:
            self.search_node(node.child_left, url)
        elif node.child_right is not None and node.url < node.child_right.url:
            self.search_node(node.child_right, url)
        else:
            return None

    def _calc_hash(self, node):
        pass
