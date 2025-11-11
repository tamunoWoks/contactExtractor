import pyperclip, re

# Create phone number regex
phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?           # Area code (optional)
    (\s|-|\.)?                   # Separator (space, dash, or dot)
    (\d{3})                      # First three digits
    (\s|-|\.)                    # Separator
    (\d{4})                      # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # Extension (optional)
)''', re.VERBOSE)

# Create email regex
email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # Domain name
    (\.[a-zA-Z]{2,4})       # Dot-something
)''', re.VERBOSE)

# Read text from clipboard
text = str(pyperclip.paste())

matches = []

# Extract phone numbers
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)
