from source.tree_crawler import CrawlerTree
import random


def main(url_beggining="https://pt.wikipedia.org/wiki/Brasilac",
         ):
    global documentsTree
    documentsTree = CrawlerTree()

    items = []
    for k in range(5):
        items.append(random.randint(0, 500))

    for item in items:
        print("item a se adicionar: ", item)
        documentsTree.insert_node(url=item)

    print("Nós inseridos: {0}".format(documentsTree.number_of_nodes()))
    

if __name__ == '__main__':
    main()
