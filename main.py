import avl_tree as avl

avl_tree = avl.AvlTree()
root = avl_tree.insert(None, 1)
root = avl_tree.insert(root, 2)
root = avl_tree.insert(root, 3)
root = avl_tree.insert(root, 4)
root = avl_tree.insert(root, 5)
avl_tree.preorder(root)