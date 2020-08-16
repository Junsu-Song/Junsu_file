s = input("s:")
cnt1=0
cnt2=0
cnt3=0
cnt4=0
for i in range(0, len(s)):
    if  s[i] == "1":
        cnt1 += 1
    elif s[i] == "I":
        cnt2 += 1
    elif s[i] == "l":
        cnt3 += 1
    elif s[i] == "w":
        cnt4 += 1

print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
