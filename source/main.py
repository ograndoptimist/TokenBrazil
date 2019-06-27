from tree_crawler import CrawlerTree
import random


def main():
    global documentsTree
    documentsTree = CrawlerTree()

    items = []
    for k in range(50000):
        items.append(random.randint(0, 500))

    for item in items:
        print("item a se adicionar: ", item)
        documentsTree.insert_item(item)

    print("Nós inseridos: {0}".format(documentsTree.number_nodes()))

    for item in items:
        print(documentsTree.search_item(item))

    

if __name__ == '__main__':
    main()
