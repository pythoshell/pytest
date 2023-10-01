
import re

# Sample list of email addresses
email_list = [
    "user1@example.com",
    "user2@example.com",
    "user3@gmail.com",
    "user4@example.com",
    "user5@example.net"
]

# The regular expression pattern to match email addresses from "example.com"
#pattern = r'\b[A-Za-z0-9._%+-]+@example\.com\b'
pattern = r''
# Iterate through the email list and find matches
matches = []
for email in email_list:
    if re.search(pattern, email):
        matches.append(email)

# Print the matching email addresses
print("Email addresses from example.com:")
for match in matches:
    print(match)
