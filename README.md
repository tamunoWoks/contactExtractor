# contactExtractor
**contactExtractor** is a simple yet powerful Python script that automatically extracts **phone numbers** and **email addresses** from any copied text (from your clipboard). It uses the `re` (Regular Expressions) module for pattern matching and `pyperclip` for clipboard access.

This tool is inspired by practical text processing problems. For example, scanning a web page, document, or message for contact information and can easily be adapted for automation scripts or data cleaning workflows.

### Code Overview:
The code for this mini-project can be found on [contactExtractor.py](https://github.com/tamunoWoks/contactExtractor/blob/main/contactExtractor.py)

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

## How It Works:
1. The script grabs text currently copied to your clipboard.
2. It uses **two regular expressions**:
   - One to identify **phone numbers**
   - One to identify **email addresses**
3. All detected matches are combined into a single list.
4. The matches are copied back to your clipboard and printed to the terminal.

## Example Usage
### Input (copied to clipboard):
```txt
Reach us at 415-863-9900 or 415.863.9950.
You can also email info@nostarch.com or sales@nostarch.com for details.
```
### Output (printed & copied):
```txt
Copied to clipboard:
415-863-9900
415-863-9950
info@nostarch.com
sales@nostarch.com
```
