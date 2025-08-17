import os
import re

# The regex pattern for the old absolute Mac path to archive.zip
pattern = re.compile(r'["\']/Users/.+?/archive\.zip["\']')

# Replacement string (relative path)
replacement = '"data/archive.zip"'

project_dir = "."  # Current folder
modified_files = []

for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith(".py"):  # Only process Python files
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Replace all matches
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                modified_files.append((file_path, count))

# Report
if modified_files:
    print("✅ Replaced hardcoded paths in:")
    for path, count in modified_files:
        print(f"  {path}  ({count} replacement(s))")
else:
    print("✅ No matching hardcoded archive.zip paths found.")
