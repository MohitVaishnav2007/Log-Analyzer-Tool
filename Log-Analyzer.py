import os 

def analyze_log(file_path, keywords):
  try:
    with open(file_path, 'r') as file:
      content = file.read()

    lines = content.splitlines()
    total_lines = len(lines)
    total_words = len(content.split())
    total_characters = len(content)

    keywords_counts = {}
    for keyword in keywords:
      keywords_counts[keyword] = content.lower().count(keyword.lower())

    
    #Display result
    print(f"Total Lines: {total_lines}")
    print(f"Total Words: {total_words}")
    print(f"Total Characters: {total_characters}")
    for keyword, count in keywords_counts.items():
      print(f"'{keyword}' Occurrences: {count}")


    #Save report
    report = f"Log Analysis Report\n\n"
    report += f"Total Lines: {total_lines}\n"
    report += f"Total Words: {total_words}\n"
    report += f"Total Characters: {total_characters}\n"
    for keyword, count in keywords_counts.items():
      report += f"'{keywords}' Occurrences: {count}\n"

    with open('log_report.txt', 'w') as report_file:
      report_file.write(report)

    print("\n Report Saved as 'log_report.txt'")

  except FileNotFoundError:
    print("Error: The specified file does not exist.")
  except Exception as e:
    print(f"An error occurred: {e}")



# =====Customize below=====
log_file_path = 'sample_log.txt' #Your log file name at place of Sample_log.txt
search_keywords = ['error','warning','critical','failed'] #Add more keywords if needed


# ==== Run Analyzer ====
analyze_log(log_file_path, search_keywords)
