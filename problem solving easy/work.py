num = 84719
num = str(num)
length = len(num)
start = int(num[0])
end = int(num[-1])

if length%2==0:
    mid1 = int(num[length//2])
    mid2 = int(num[length//2-1])
    if (mid1 < start and mid1 < end) and (mid2 < start and mid2 < end):
        print(True)
    else:
        print(False)
else:
    mid = int(num[length//2])
    if mid < start and mid < end:
        print(True)
    else:
        print(False)