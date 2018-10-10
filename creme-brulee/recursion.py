def get_permutations(s):
    chars = set(s)
    permutations = []
    def permute(s, chars):
        if not chars:
            permutations.append(s)
        for c in chars:
            new_s = s + c
            new_chars = chars.copy()
            new_chars.remove(c)
            permute(new_s, new_chars)

    permute("", chars)
    return permutations
