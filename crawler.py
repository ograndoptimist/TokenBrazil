"""
    The goal: to build the biggest token dictionary in Brazilian Portuguese, and the most important,
    garanting quality.
"""
import typing


class NodeTree(object):
        def __init__(self, url=None):
            self._child_left = None
            self._child_right = None
            self._url = None
            self._content = None
            self._hash = None
            self._number_node = 0

            
class CrawlerTree(NodeTree):
    """
        We aim to build a beautiful Tree of text's documents from the internet.
        So, expect each node to be a document containing portuguese text.
    """
    def __init__(self):
        super().__init__()
        self._root = NodeTree()

    def number_of_nodes(self):
        return self._number_node
        
    def insert_node(self, url):
        if self._root == None:
            self._root = node
            self._url = url
            self._hash = -1212
            return self._url

        if(self.search_node(node, url) == None):
            node = NodeTree()
            self._number_node += 1
        else:
            raise Exception("URL already on the tree.")

    def search_node(self, node, url):
        if node == None:
            raise Exception("Parent is empty")

        if node._url == url:
            return node
        elif node._child_left is not None and node._url < node._child_left._url:
            self.search_node(node._child_left)
        elif node._child_right is not None and node._url < node._child_right._url:
            self.search_node(node._child_right)

    def _calc_hash(self, node):
        pass
