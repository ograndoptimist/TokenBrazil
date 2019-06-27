"""
    The goal: to build the biggest token dictionary in Brazilian Portuguese, and the most important,
    garanting quality.
"""
from node_tree import NodeTree


class CrawlerTree(NodeTree):
    """
        We aim to build a beautiful Tree of text's documents from the internet.
        So, expect each node to be a document containing portuguese text.
    """
    def __init__(self):
        super().__init__()
        self.root = NodeTree()

    def number_of_nodes(self) -> int:
        return self.number_node

    def __set_root_node(self, item):
        assert self.root.item is None

        if self.root.item is None:
            self.root.item = item
            self.number_node += 1

    def _create_node(self, item: int) -> bool:
        node = NodeTree(item)
        parent = self._search_node(self.root, item)

        if parent.item > node.item:
            parent.child_left = node
        elif parent.item < node.item:
            parent._child_right = node

        self.number_node += 1
        return True
        
    def insert_node(self, item: int) -> bool:
        if self.root.item is None:
            self.__set_root_node(item)
        elif not self.search_item(item):
            return self._create_node(item)
        else:
            return False

    def _search_node(self, node: NodeTree, item: int) -> NodeTree:
        if node.item == item:
            return node
        if node.child_left is not None and node.item > item:
            return self._search_node(node.child_left, item)
        elif node.child_right is not None and node.url < item:
            return self._search_node(node.child_right, item)

        return node

    def search_item(self, item: int) -> bool:
        if self._search_node(self.root, item).item == item:
            return True
        else:
            return False

    def _calc_hash(self, node):
        pass
