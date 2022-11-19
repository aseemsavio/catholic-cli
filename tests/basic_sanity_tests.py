import os

print("Test starting...")

commands = [
    "catholic",
    "catholic --version",
    "catholic --help",
    "catholic catechism --paragraph 101",
    "catholic catechism --paragraph 101,102",
    "catholic catechism --paragraph 101-103",
    "catholic catechism --paragraph 1,2,4-5",
    "catholic c --p 101",
    "catholic c --p 101,102",
    "catholic c --p 101-103",
    "catholic c --p 1,2,4-5",
    'catholic catechism --search "The Eucharist is our daily bread"',
    'catholic c --s "The Eucharist is our daily bread"',
    'catholic catechism --s "aseem savio"'
]

for num, command in enumerate(commands):
    print("\n-----------------------------------------------------------------\n")
    print(f"\n\n{num}. COMMAND: {command}\n")

    os.system(command)

print("Test Ended")
