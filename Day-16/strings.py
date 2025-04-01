T = 1
N = 8
K = 3

A = [1,2,3,4,5,6,7,8]
R = []

for i in range(N-K,N):
    R.append(A[i])
for j in range(0,N-K):
    R.append(A[j])
A = R

for i in A:
    print(i,end=' ')