def remove_duplicate_values(d):
    seen_vals = set()
    res = {}
    for k, v in d.items():
        if v not in seen_vals:
            seen_vals.add(v)
            res[k] = v
    return res