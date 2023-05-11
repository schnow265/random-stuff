import sys

f = open("text.txt", "r")
print(f.read())

print("Close? [Y/N]")
action = input()
if action == "Y":
    f.close()
else:
    pass

# trying hard to check

try:
    f.read()

except IOError:
    print("none")
else:
    print("open")
