from crawler import CrawlerTree


def main(url_beggining="https://pt.wikipedia.org/wiki/Brasilac",
         ):
    documentsTree = CrawlerTree()
    print(documentsTree.insert_node(url=url_beggining))
    




if __name__ == '__main__':
      main()
