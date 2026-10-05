def add_task(queue, new_task):
    queue.extend(new_task)
    return queue


print(add_task(["task1"], ["task2", "task3"]))