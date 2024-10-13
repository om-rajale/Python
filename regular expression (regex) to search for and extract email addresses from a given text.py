import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails

text = "Please contact us at support@example.com or sales@domain.org for more information."
emails = find_emails(text)
print("Extracted Email Addresses:", emails)
