a = "TTTAGAGCGGCCGCGCGCT"
b = {"A": "T", "C": "G", "G": "C", "T": "A"}
c = ""

for i in a:
    c += b[i]
print(a)
print(c[::-1])
