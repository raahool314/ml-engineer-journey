"""
Claude:
Problem 1
user_input = "   machine LEARNING engineer   "
Using string methods, print it: stripped of whitespace, in title case, in all caps, and print how many characters it has (after stripping).
"""

user_input = "   machine LEARNING engineer   "
print(user_input.strip())
print(user_input.title())
print(user_input.upper())
print(len(user_input.strip()))

"""
Claude:
Problem 2
email = "rahul.sharma@company.com"
Without hardcoding anything, extract and print just the username (rahul.sharma) and just the domain (company.com). Hint: .split() can split on any character.
"""
email = "rahul.sharma@company.com"
username, domain = email.split("@")
print(f"username: {username}, domain: {domain}")

"""
Claude:
Problem 3
sentence = "the quick brown fox jumps over the lazy dog"
Print how many words are in it, how many times the letter "o" appears, and print it in title case with all spaces replaced by underscores.
"""
sentence = "the quick brown fox jumps over the lazy dog"
print(f"words in sentence: {len(sentence.split())}")
print(f"number of o's in sentence: {sentence.count("o")}")
print(sentence.title().replace(" ","_"))