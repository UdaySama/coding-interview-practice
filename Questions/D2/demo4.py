user_Input = "10, 20, 30, 40"

nums = [int(num) for num in user_Input.split(",")]

total_sum = sum(nums)
print(total_sum)


# input containing numbers separated by commas, convert them into a list of integers, and print their sum