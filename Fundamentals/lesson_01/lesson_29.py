# Task 3 — Real-world Job Data 🔥


job = {
    "company": "Google",
    "role": "Software Engineer",
    "status": "Applied",
    "location": "Bangalore"
}

# Print the company.
# Print the role.
# Change status from "Applied" to "Interview".
# Add:
# salary
# job_url

# with your own values.
# 5. Check whether "email" exists using in.
# 6. Print the final dictionary.
print(job)

print(job["company"])
print(job['role'])
job["status"]="Interview"
print(job)
job["salary"]=3000
job["job_url"]="https://chatgpt.com/c/6a96e990-3634-83e8-806d-7ebc1490f65e"
print(job)


if "email" in job:
    print("Exists")
else:
   print("Not exists") 


print(job)