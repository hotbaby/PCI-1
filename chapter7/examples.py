# encoding: utf-8

import treepredict

fruits = [
    [4, 'red', 'apple'],
    [4, 'green', 'apple'],
    [1, 'red', 'cherry'],
    [1, 'green', 'grape'],
    [5, 'red', 'apple']
]

my_data = [['slashdot', 'USA', 'yes', 18, 'None'],
           ['google', 'France', 'yes', 23, 'Premium'],
           ['digg', 'USA', 'yes', 24, 'Basic'],
           ['kiwitobes', 'France', 'yes', 23, 'Basic'],
           ['google', 'UK', 'no', 21, 'Premium'],
           ['(direct)', 'New Zealand', 'no', 12, 'None'],
           ['(direct)', 'UK', 'no', 21, 'Basic'],
           ['google', 'USA', 'no', 24, 'Premium'],
           ['slashdot', 'France', 'yes', 19, 'None'],
           ['digg', 'USA', 'no', 18, 'None'],
           ['google', 'UK', 'no', 18, 'None'],
           ['kiwitobes', 'UK', 'no', 19, 'None'],
           ['digg', 'New Zealand', 'yes', 12, 'Basic'],
           ['slashdot', 'UK', 'no', 21, 'None'],
           ['google', 'UK', 'yes', 18, 'Basic'],
           ['kiwitobes', 'France', 'yes', 19, 'Basic']]


def main(rows):
    # fruits with their colors and size
    tree = treepredict.buildtree(rows)
    # print(treepredict.classify([2, 'red'], tree))
    # print(treepredict.classify([5, 'red'], tree))
    # print(treepredict.classify([1, 'green'], tree))

    # 决策树
    treepredict.printtree(tree)
    treepredict.drawtree(tree, jpeg='treeview.jpg')


if __name__ == '__main__':
    main(my_data)
