class NodeTree(object):
    """
       Abstract data type that provides the baseline to build a Tree Crawler.
    """
    def __init__(self, item=None):
        self.child_left = None
        self.child_right = None
        self.item = item
        self.content = None
        self.hash = None
        self.number_node = 0