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
