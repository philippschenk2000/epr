""" This script is the start for the different functions for the new exercise """

__author__ = "7093700, Schenk"

import epr_graph


def main():

    # DEFINE GRAPH VIA INPUT
    graphing = [((1, 1), (3, 3)), ((1, 1), (4, 1)), ((7, 7), (4, 2)), ((7, 7), (1, 1))]
    graphing = [eval(input('Enter your edge nuber' + str(g) + ': ')) for g in range(int(input('Enter number of nodes in your graph: ')))]
    try:
        # TRY: TEST IF THE PROVIDED GRAPH REALLY IS IN CORRECT FORMAT
        tree_status = epr_graph.test_for_tree(graphing)
        print(tree_status)
        #tree_status = True
        # JUST IF TREE = TRUE: CALL THE LEAVES AND ROOT FUNCTIONS AND PRINT THEM
        if tree_status:
            leaves = epr_graph.get_leaves(graphing)
            print('The leaves are: ', list(set(leaves)))
            root = epr_graph.get_root(graphing)
            if len(root) > 0:
                print('The root is:', list(set(root)))
            else:
                print('In the tree there is no root available.')
        else:
            print('The provided graph is no tree')
    except ValueError:
        print('Please provide a correct graph in the format like this \n[((1, 1), (3, 3)), ((1, 1), (4, 1)), ((7, 7), (4, 2)): ')


main()
