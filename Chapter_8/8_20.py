def level(root, node):
    if root is None:
        return None

    if root == node:
        return 1

    left_level = level(root.left, node)
    if left_level is not None:
        return left_level + 1

    right_level = level(root.right, node)
    if right_level is not None:
        return right_level + 1