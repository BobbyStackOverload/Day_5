import collections
freq =input("Type a sentence: ")
uency = freq.split()
# counts frequency
answer =collections.Counter(uency)
print(answer)