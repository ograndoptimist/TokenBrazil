"""
    The goal: to build the biggest token dictionary in Brazilian Portuguese, and the most important,
    garanting quality.
"""
from node_tree import NodeTree


class CrawlerTree(NodeTree):
    """
        We aim to build a beautiful Tree of text's documents from the internet.
        So, expect each node to be a document containing portuguese text.
        CrawlerTree is a Binary Search Tree (BST) data structure.
    """
    def __init__(self):
        super().__init__()
        self.root = NodeTree()

    def number_nodes(self) -> int:
        return self.number_node

    def __set_root_node(self, url: str) -> None:
        assert self.root.url is None

        if self.root.url is None:
            self.root.url = url
            self.number_node += 1

    def _create_node(self, url: str) -> bool:
        node = NodeTree(url)
        parent = self._search_node(self.root, url)

        if parent.url > node.url:
            parent.left = node
        elif parent.url < node.url:
            parent.right = node

        self.number_node += 1
        return True
        
    def insert_url(self, url: str) -> bool:
        if self.root.url is None:
            self.__set_root_node(url)
        elif not self.search_url(url):
            return self._create_node(url)
        else:
            return False

    def _search_node(self, node: NodeTree, url: str) -> NodeTree:
        if node.url == url:
            return node
        elif node.left is not None and node.url > url:
            return self._search_node(node.left, url)
        elif node.right is not None and node.url < url:
            return self._search_node(node.right, url)

        return node

    def search_url(self, url: str) -> bool:
        if self._search_node(self.root, url).url == url:
            return True
        else:
            return False
