total_Second = 3665

hours = total_Second // 3600
minutes = (total_Second % 3600) // 60
seconds = total_Second % 60

print(f"{hours}hr | {minutes}min | {seconds}sec")