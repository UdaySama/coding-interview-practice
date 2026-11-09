people = [{'name':'Amey', "age":25}, {'name':'Sanmathi', "age":24},{'name':'Sidharth', "age":26},]
oldest = max(people,key=lambda x:x['age'])
print(oldest)