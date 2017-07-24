import re

# file_text = open("test-file.txt")
# print(file_text.read())

with open("test-file.txt", "r") as text:
	policy = re.search(r'Policy Number:\s+[0-9]+', text.read())
	print(policy.group())
text.close()

with open("test-file.txt", "r") as text:
	claim = re.search(r'Claim Number:\s+[a-zA-Z]+[-]+[0-9]+', text.read())
	print(claim.group())
text.close()