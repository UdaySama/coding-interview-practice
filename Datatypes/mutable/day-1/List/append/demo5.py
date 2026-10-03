def capitalize_words(wrds):
    res = []
    for wrd in wrds:
        res.append(wrd.capitalize())
    return res



print(capitalize_words(['python',"Java","sql"]))