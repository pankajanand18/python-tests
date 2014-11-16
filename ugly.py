__author__ = 'pankaj'

n = 15
bases = [2, 3, 5]

nums = [1] * n
candidates_indexes = [0 for _ in bases]
candidates = [base for base in bases]

for i in range(1, n):
    nextn = min(candidates)
    nums[i] = nextn

    for index, val in enumerate(candidates):
        if val == nextn:
            candidates_indexes[index] += 1
            candidates[index] = bases[index] * nums[candidates_indexes[index]]
            print nextn,candidates[index]

print(nums)

