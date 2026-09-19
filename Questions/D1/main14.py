def group_by_first_char(words):
    grouped = {}
    for w in words:
        if w:
            grouped.setdefault(w[0], []).append(w)
    return grouped