def append_valid_batches(mast,batches):
    for batch in batches:
        if batch:
            mast.extend(batch)
    return mast



print(append_valid_batches([1], [[2, 3], [], [4]]))