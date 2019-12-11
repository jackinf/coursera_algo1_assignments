from statistics import median
from typing import List, Tuple


class Solution:
    def run(self, array: List[int], version: int):
        comparisons = self.quick_sort(array, 0, len(array), version)
        return comparisons, array

    def quick_sort(self, array: List[int], left: int, right: int, version: int) -> int:
        if left < right:
            comparisons, i = self.partition(array, left, right, version)

            left_comparisons = self.quick_sort(array, left, i, version)
            right_comparisons = self.quick_sort(array, i + 1, right, version)

            return comparisons + left_comparisons + right_comparisons
        else:
            return 0

    def partition(self, array: List[int], start: int, end: int, version: int) -> Tuple[int, int]:
        p = self.choose_pivot(array, start, end, version)

        i = start + 1
        for j in range(start + 1, end):
            if array[j] < p:
                array[j], array[i] = array[i], array[j]
                i += 1

        array[start], array[i - 1] = array[i - 1], array[start]
        return end - start - 1, i - 1

    def choose_pivot(self, array: List[int], start: int, end: int, version: int) -> int:
        if version == 1:
            return self.choose_first_pivot(array, start)
        if version == 2:
            return self.choose_last_pivot(array, start, end)
        if version == 3:
            return self.choose_median_pivot(array, start, end)

    def choose_first_pivot(self, array: List[int], start: int) -> int:
        return array[start]

    def choose_last_pivot(self, array: List[int], start: int, end: int) -> int:
        array[end - 1], array[start] = array[start], array[end - 1]
        return array[start]

    def choose_median_pivot(self, array: List[int], start: int, end: int) -> int:
        first = array[start]
        last = array[end - 1]
        m2 = (end - 1 - start) // 2 + start

        med = median([first, last, array[m2]])
        i = m2 if med == array[m2] else start if med == first else end - 1
        array[i], array[start] = array[start], array[i]
        return array[start]


file = open('coursera-algo-task3.txt', 'r')
with file as f:
    nums = [int(x.strip()) for x in f.readlines()]

solution = Solution()
test_arr = [3, 8, 2, 5, 1, 4, 7, 6]
print(solution.run(test_arr[:], 1))
print(solution.run(test_arr[:], 2))
print(solution.run(test_arr[:], 3))

print(solution.run(nums[:], 1))
print(solution.run(nums[:], 2))
print(solution.run(nums[:], 3))

# first - mine is 162085, correct is 162085
# last - mine is 164123, correct is 164123
# middle - mine is 138382, correct is 138382
