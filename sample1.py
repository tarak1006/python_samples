import itertools
testcases=int(input())
for t in range(testcases):
    count=0
    N = int(input())
    K=int(input())
    l = range(1, N + 1)
    list = itertools.permutations(l, 2)
    for i in list:
        if(sum(i)>K):
            count=count+1
    print(count/N*N-1)

