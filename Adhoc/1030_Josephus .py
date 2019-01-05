
# n -> Noof People
# k -> Noof step

"""
Input
-----
3
5 2
6 3
1234 233

OutPut
-------

Case 1: 3
Case 2: 1
Case 3: 25

"""
def wining_position(n, k):
    if (n == 1):
        return 0
    
    return (wining_position(n-1,k)+ k) % n



# take testCase form user
test_case = int(input())

for test in range(1,test_case+1):
     n, k = map(int, input().split())

     live_postion = wining_position(n,k) + 1
     print("Case "+ str(test)+ ": "+ str(live_postion))




