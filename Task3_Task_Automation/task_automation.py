import re

# Read the text file
with open("sample.txt", "r") as file:
    text = file.read()

# Find email addresses
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)

# Save extracted emails to a new file
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Email addresses extracted successfully!")
print("Found emails:")

for email in emails:
    print(email)

print("Saved to extracted_emails.txt")