# ContactExtractor
**ContactExtractor** is a simple yet powerful Python script that automatically extracts **phone numbers** and **email addresses** from any copied text (from your clipboard). It uses the `re` (Regular Expressions) module for pattern matching and `pyperclip` for clipboard access.

This tool is inspired by practical text processing problems. For example, scanning a web page, document, or message for contact information and can easily be adapted for automation scripts or data cleaning workflows.

## Features:
- Detects **multiple phone number formats** such as:
  - `415-555-4242`
  - `(415) 555-4242`
  - `415.555.4242`
  - `415 555 4242`
- Handles **optional extensions**, e.g., `415-555-4242 ext 123` or `x1234`
- Finds **valid email addresses** like:
  - `info@nostarch.com`
  - `first.last123@company.org`
- Copies all matches directly to your clipboard for quick use.
