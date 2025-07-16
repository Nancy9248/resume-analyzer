import re

# Define keywords to check
KEYWORDS = ["python", "data analysis", "machine learning", "teamwork", "communication", "project management"]

# Load resume text
def load_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().lower()

# Check for keywords
def check_keywords(text):
    found = []
    for keyword in KEYWORDS:
        if keyword in text:
            found.append(keyword)
    return found

# Count words
def count_words(text):
    return len(text.split())

# Check for email
def has_email(text):
    pattern = r"[a-zA-Z0-9+._%-]+@[a-zA-Z0-9._%-]+\.[a-zA-Z]{2,6}"
    match = re.search(pattern, text)
    return match.group() if match else None

# Main function
def analyze_resume(file_path):
    text = load_resume(file_path)
    keywords_found = check_keywords(text)
    word_count = count_words(text)
    email = has_email(text)

    print("Resume Analysis Report")
    print("----------------------")
    print(f"Total Words: {word_count}")
    print(f"Keywords Found: {', '.join(keywords_found) if keywords_found else 'None'}")
    print(f"Email Address: {email if email else 'Not found'}")

# Example usage
if __name__ == "__main__":
    # Replace 'sample_resume.txt' with your resume file name
    analyze_resume("sample_resume.txt")
