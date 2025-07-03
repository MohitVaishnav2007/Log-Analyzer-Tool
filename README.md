## 🔍 Log Analyzer Tool (Python)

This is a simple yet powerful Python-based Log Analyzer Tool designed to:

Read and analyze log files

Count total lines, words, and characters

Search for specific keywords like error, warning

Generate a clean report file summarizing the findings


Perfect for beginners, cybersecurity learners, and anyone who wants to automate basic log analysis.


---

## 📂 Features

Read any .txt log file

Automatically counts:

Total lines

Total words

Total characters


Detects and counts specific keywords (customizable)

Generates a report (log_report.txt)

Easy to customize & expand



---

## 🚀 How to Use

1. Clone this repository or download the files.


2. Place your log file in the same directory (sample file included: sample_log.txt).


3. In the script, update the file path and keywords as needed:



log_file_path = 'sample_log.txt'
search_keywords = ['error', 'warning']

4. Run the script:



python log_analyzer.py

5. ✅ You will get:

Detailed analysis on your terminal.

Report saved as log_report.txt.





---

## 📄 Sample Output:

Total Lines: 152
Total Words: 1803
Total Characters: 10439
'error' Occurrences: 15
'warning' Occurrences: 5

✅ Report saved as 'log_report.txt'


---

## 🛠 Files Included:

```File	Description

log_analyzer.py	Python script for log analysis (main tool)
sample_log.txt	Sample log file for testing (optional)
```


---

## 🔥 Future Enhancements (Ideas):

Multi-file log analysis

Regex-based advanced keyword search

Auto-alerting via Email/Discord/Slack

Integration with cybersecurity tools



---

## 💖 Author:

Mohit Vaishnav
Cybersecurity & Python Enthusiast


---

## ⚠ Disclaimer:

This is an educational project meant for learning purposes only.


---