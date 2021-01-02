def get_target_copy(original, cloned, target):
    if not original:
        return None
    if original is target:
        return cloned
    return get_target_copy(original.left, cloned.left, target) or get_target_copy(original.right, cloned.right, target)
