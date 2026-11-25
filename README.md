# Student Mark Analyzer

A beginner-friendly Python project that analyzes student marks using Pandas and Matplotlib.

## Files
- `student_marks.csv` — sample student marks dataset
- `student_mark_analyzer.py` — main Python program
- `student_analysis_output.csv` — generated after running the program
- `student_performance.png` — generated performance chart
- `Student_Mark_Analyzer.ipynb` — Jupyter Notebook version
- `requirements.txt` — required Python libraries

## How to run
1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python student_mark_analyzer.py`

## Features
- Calculates total marks and percentage for every student.
- Assigns grades.
- Checks pass status (35 marks minimum in every subject).
- Finds class average and topper.
- Calculates subject-wise averages.
- Exports an analysis CSV and a bar chart.

## Grade scale
A+: 80–100 | A: 70–79.99 | B: 60–69.99 | C: 50–59.99 | D: 40–49.99 | F: below 40

You can replace the sample data in `student_marks.csv` with your own data, keeping the same column names and marks between 0 and 100.
