""" This script contains different functions for the new exercise in epr """

__author__ = "7093700, Schenk"


def test_for_tree(graphing):
    """ This function checks if the provided graph is tree.

    """
    # SET TREE FIRSTLY TO TRUE
    tree = True
    # TEST IF CIRCLE EXISTS IN THE GRAPH
    for e in graphing:
        # ITERATE THRU EVERY NODE FIRST
        start_node = e[0]
        end_node = e[1]
        # ITERATE THRU EVERY OTHER NODE
        for new_e in graphing:
            start_node_copy = new_e[0]
            if start_node_copy != start_node:
                # IF THE FIRST START_NODE IS ANYWHERE THE END_NODE SET TREE TO FALSE
                end_node_copy = new_e[1]
                if end_node_copy == start_node:
                    print(start_node, end_node, start_node_copy, end_node_copy)
                    tree = False
                    break
    return tree


def get_leaves(graphing):
    """ This function looks for the leaves in the tree.

    """
    start_nodes = [n[0] for n in graphing]
    end_nodes = [n[1] for n in graphing]
    # CHECK IF ONE END_NODE HAS NO OUTGOING EDGE
    leaves = [n for n in end_nodes if n not in start_nodes]
    return leaves


def get_root(graphing):
    """ This function looks for the root in the tree

    """
    start_nodes = [n[0] for n in graphing]
    end_nodes = [n[1] for n in graphing]
    # CHECK IF ONE START_NODE HAS NO INGOING EDGE
    root = [n for n in start_nodes if n not in end_nodes]
    return root
