job1 = {"Python", "SQL", "Git", "FastAPI"}
job2 = {"Python", "SQL", "Git", "Docker"}

# print(python.intersection(backend))
# result = python.union(backend)
# print(python.difference(backend))
print("Job 1:- ",job1)
print("Job 2:- ",job2)
print("===================================")
print(job1.union(job2))
print(job1.intersection(job2))
print(job1.difference(job2))
print(job2.difference(job1))


