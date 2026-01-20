def find_modified_max_argmax(L, f):
    L = [f(i) for i in L if type(i) == int]
    if not len(L):
        return tuple()
    return (max(L), L.index(max(L)))