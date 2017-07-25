import re

# text = open("test-file.txt")
# print(text.read())

# with open("test-file.txt", "r") as text:
# 	policy = re.search(r'Policy Number:\s+[0-9]+', text.read())
# 	print(policy.group())
# text.close()

# with open("test-file.txt", "r") as text:
# 	claim = re.search(r'Claim Number:\s+[a-zA-Z]+[-]+[0-9]+', text.read())
# 	print(claim.group())
# text.close()

with open("test-file.txt", "r") as text:
	pin = re.sub('Pin:\s([0-9]+)','Pin: 9932', text.read())
text.close()
print(pin)