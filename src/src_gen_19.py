from typing import List

def sat199(odds: List[int], nums=[204, 109, 203, 17, 45, 11, 21, 99, 909, 16, -33, 3, 17]):
    assert all(o > 10 and odds.count(o) == nums.count(o) and int(str(o)[i]) % 2 for o in odds for i in [-1, 0])
    return all(n in odds or n <= 10 or int(str(n)[0]) % 2 == 0 or int(str(n)[-1]) % 2 == 0 for n in nums)
def sol199(nums=[204, 109, 203, 17, 45, 11, 21, 99, 909, 16, -33, 3, 17]):
    """Find the numbers that are greater than 10 and have odd first and last digits

    [73, 4, 72] => [73]
    """
    return [n for n in nums if n > 10 and (int(str(n)[0]) * int(str(n)[-1])) % 2]
# assert sat199(sol199())

