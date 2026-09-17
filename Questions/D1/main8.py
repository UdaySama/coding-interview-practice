def remove_duplicates_str(s):
    seen = set()
    return "".join([c for c in s if not (c in seen or seen.add(c))])