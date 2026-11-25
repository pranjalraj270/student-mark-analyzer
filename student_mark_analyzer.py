"""
Student Mark Analyzer
Run: python student_mark_analyzer.py
Input CSV columns: Student_ID, Student_Name, and subject marks.
"""
import pandas as pd
import matplotlib.pyplot as plt

FILE = "student_marks.csv"
PASS_MARK = 35

def load_data(file_name):
    df = pd.read_csv(file_name)
    required = {"Student_ID", "Student_Name"}
    if not required.issubset(df.columns):
        raise ValueError("CSV must contain Student_ID and Student_Name columns.")
    subject_cols = [c for c in df.columns if c not in required]
    if not subject_cols:
        raise ValueError("Add at least one subject column.")
    df[subject_cols] = df[subject_cols].apply(pd.to_numeric, errors="raise")
    if ((df[subject_cols] < 0) | (df[subject_cols] > 100)).any().any():
        raise ValueError("Marks must be between 0 and 100.")
    return df, subject_cols

def analyze(df, subjects):
    df["Total"] = df[subjects].sum(axis=1)
    df["Percentage"] = (df["Total"] / (len(subjects) * 100) * 100).round(2)
    df["Result"] = df[subjects].ge(PASS_MARK).all(axis=1).map(
        {True: "PASS", False: "NEEDS IMPROVEMENT"}
    )
    df["Grade"] = pd.cut(
        df["Percentage"],
        bins=[-1, 39.99, 49.99, 59.99, 69.99, 79.99, 100],
        labels=["F", "D", "C", "B", "A", "A+"]
    )
    return df

def main():
    df, subjects = load_data(FILE)
    result = analyze(df, subjects)
    print("\\n===== STUDENT MARK ANALYSIS =====")
    print(result[["Student_ID", "Student_Name", "Total", "Percentage", "Grade", "Result"]].to_string(index=False))
    print("\\nClass average: {:.2f}%".format(result["Percentage"].mean()))
    topper = result.loc[result["Percentage"].idxmax()]
    print("Topper: {} ({:.2f}%)".format(topper["Student_Name"], topper["Percentage"]))
    print("\\nSubject-wise averages:")
    print(result[subjects].mean().round(2).to_string())

    result.to_csv("student_analysis_output.csv", index=False)

    plt.figure(figsize=(9, 5))
    plt.bar(result["Student_Name"], result["Percentage"])
    plt.title("Student-wise Percentage")
    plt.xlabel("Student")
    plt.ylabel("Percentage")
    plt.ylim(0, 100)
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("student_performance.png", dpi=150)
    print("\\nSaved: student_analysis_output.csv and student_performance.png")

if __name__ == "__main__":
    main()
