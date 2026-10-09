def areAnagrams(str,str1):
    cleanS1= str.replace(" " , " ").lower()
    cleanS2= str1.replace(" " , " ").lower()
    return sorted(cleanS1) == sorted(cleanS2)


print(areAnagrams("listen", "silent"))