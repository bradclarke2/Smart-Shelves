DATA = [
    ('Jones', 'Jane', 58),
    ('Smith', 'Anne', 30),
    ('Jones', 'Fred', 30),
    ('Smith', 'John', 60),
    ('Smith', 'Fred', 30),
    ('Jones', 'Anne', 30),
    ('Smith', 'Jane', 58),
    ('Smith', 'Twin2', 3),
    ('Jones', 'John', 60),
    ('Smith', 'Twin1', 3),
    ('Jones', 'Twin1', 3),
    ('Jones', 'Twin2', 3)
]

# Sort by Surname, Age DESCENDING, Firstname
print("Initial data in random order")
for d in DATA:
    print("{:10s} {:10s} {}".format(*d))

print('''
First we sort by first name, after this pass all
Twin1 come before Twin2 and Anne comes before Fred''')
DATA.sort(key=lambda row: row[1])

for d in DATA:
    print("{:10s} {:10s} {}".format(*d))

print('''
Second pass: sort by age in descending order.
Note that after this pass rows are sorted by age but
Twin1/Twin2 and Anne/Fred pairs are still in correct
firstname order.''')
DATA.sort(key=lambda row: row[2], reverse=True)
for d in DATA:
    print("{:10s} {:10s} {}".format(*d))

print('''
Final pass sorts the Jones from the Smiths.
Within each family members are sorted by age but equal
age members are sorted by first name.
''')
DATA.sort(key=lambda row: row[0])
for d in DATA:
    print("{:10s} {:10s} {}".format(*d))