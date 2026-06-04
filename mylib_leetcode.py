# this class is provided by leetcode.com
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_builder(nodes: list) -> TreeNode:
    """Warning: the first entry of the node list is ignored.
    This is necessary to ensure 2*i and  2*i+1 are valid indeces to access left and right nodes."""

    length = len(nodes)

    # append root node index to the list of nodes to process
    root = TreeNode(nodes[1])
    # append node index and node instance
    next_nodes = [(1, root)]

    while next_nodes:
        i, parent = next_nodes.pop()

        # left child
        index = 2 * i
        value = None

        if index < length:
            value = nodes[index]

        if value:
            node = TreeNode(value)
            parent.left = node
            next_nodes.append((index, node))

        # right child
        index = 2 * i + 1
        value = None

        if index < length:
            value = nodes[index]

        if value:
            node = TreeNode(value)
            parent.right = node
            next_nodes.append((index, node))

    return root

def print_tree(node: TreeNode, level: int=0) -> None:
    indent = "." * level
    print(indent + str(node.val))

    if node.left:
        print_tree(node.left, level + 1)

        if not node.right:
            indent = "." * (level + 1)
            print(indent + 'None')

    if node.right:
        if not node.left:
            indent = "." * (level + 1)
            print(indent + 'None')

        print_tree(node.right, level + 1)

if __name__ == '__main__':
    # test library

    datas = [
        # root, 2nd level
        [1, 2, 3],
        # root, 2nd level, 3rd level
        [1, 2, 3, 4, 5, 6, 7],
        # root, 2nd level, partial 3rd level
        [1, 2, 3, None, None, None, 7],
    ]

    for data in datas:
        # prepend zero at the begining of the list to ensure 2*i and
        # 2*i+1 are valid indeces to access left and right nodes
        tree = tree_builder([0] + data)
        print(f'{data=}')
        print_tree(tree)
        print()

