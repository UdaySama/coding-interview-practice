jobs = [
    {"company": "Google", "status": "Applied"},
    {"company": "Microsoft", "status": "Interview"},
    {"company": "Amazon", "status": "Rejected"},
    {"company": "Meta", "status": "Interview"},
]

def compWithInternV(jbs):
    for job in jobs:
        if job["status"]=='Interview':
            print(job)

compWithInternV(jobs)



