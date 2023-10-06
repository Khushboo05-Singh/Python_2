s=input()
counter=0
for i in s:
    if i.isalnum():
        counter+=1
if counter>=1:
    print(True)
else:
    print(False)