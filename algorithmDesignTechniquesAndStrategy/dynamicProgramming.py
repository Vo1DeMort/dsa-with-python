#NOTE: based on divide and conquer technique
# unlike divide and conquer ,dynamic programming solves
# each sub-sub problems only once and do not recompute the
# solution to an already-encounterd sub-problem
# it uses a remembering technique to avoid re-computation

#NOTE: two important characteristics
# optimal substructure
# overlapping sub-problem

#NOTE: storing the result of each sub-problem
# top-down with memoization
# - memoization ( storing teh sub-problem in an array or hash table)
# bottom-up approach

# fibonacci with dynamic programming
def dynamicFib(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    if lookup[n] is not None:
        return lookup[n]

    lookup[n] = dynamicFib(n-1) + dynamicFib(n-2)
    return lookup[n]

lookup = [None] * (1000)

for i in range(6):
    print((dynamicFib(i)))
