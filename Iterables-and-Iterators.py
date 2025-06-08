#Iterables and Iterators

from itertools import combinations
n = int(input())
List= input().split()
k = int(input())

#Generate all possible combinations
Combinations = list(combinations(List,k))

#Filter combinations to keep only those that contain character 'a'
Filter = filter(lambda x: 'a' in x, Combinations)

print(f"{len(list(Filter))/len(Combinations):.3f}")
