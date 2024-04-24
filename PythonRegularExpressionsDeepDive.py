import re
excluded_domain = "exclude.com"
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
valid_emails = [email for email in emails if not email.lower().endswith(excluded_domain.lower())]
print(valid_emails)