class NodeTree(object):
    """
       Abstract data type that provides the baseline to build a Tree Crawler.
    """
    def __init__(self, url=None):
        self.left = None
        self.right = None
        self.url = url
        self.content = None
        self.hash = None
        self.number_node = 0
