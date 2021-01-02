def can_form_array(arr, pieces):
    for piece in pieces:
        try:
            idx = arr.index(piece[0])
        except:
            return False
        if arr[idx:idx+len(piece)] != piece:
            return False
    return True
