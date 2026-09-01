jobs = [
    {"company": "Google", "status": "Applied"},
    {"company": "Microsoft", "status": "Interview"},
    {"company": "Amazon", "status": "Rejected"},
    {"company": "Meta", "status": "Interview"},
]

# def compWithInternV(jb):
for job in jobs:
    if job["status"]=='Interview':
        print(job["company"])
    