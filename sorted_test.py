import sorting
import random

nums = [random.randint(1,100) for x in range(random.randint(1,100))]

def test_sorted():
  assert sorting.bubble(nums) == sorted(nums)
