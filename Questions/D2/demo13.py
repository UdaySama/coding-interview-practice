def sort_array_by_parity(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] % 2 > nums[right] % 2:
            nums[left], nums[right] = nums[right], nums[left]

        if nums[left] % 2 == 0:
            left += 1
        if nums[right] % 2 != 0:
            right -= 1

    return nums

print(sort_array_by_parity([3, 1, 2, 4])) 