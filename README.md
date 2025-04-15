# 📊 Student Marks Analyzer

A Python-based **Student Marks Analyzer** using `pandas`. It reads student scores from a CSV file, calculates the total and average marks, assigns grades based on average, and displays the class topper.

---

## 🚀 Features

- Read student data from a CSV file
- Calculate:
  - Total Marks (`Sum`)
  - Average Marks (`Avg`)
  - Grade:
    - A: 90 and above
    - B: 75 to 89
    - C: 50 to 74
    - D: Below 50
- Sort students by total marks in descending order
- Display the class topper

---

## 🐍 Requirements

- Python 3.x
- pandas

Install the required package using:

```bash
pip install pandas
📁 File Structure
project-root/
├── analyzer.py
└── data/
    └── student_scores.csv
✅ Ensure the CSV file (student_scores.csv) has this format:
Name   Math  Science   English
Alice   95    88     92
Bob     70    75     80
Charlie 50    40     60
🔧 How to Run
python analyzer.py

✅ Sample Output

       Name  Math  Science  English  Sum     Avg      Grade
0     Alice    95       88       92  275  91.666667     A
1       Bob    70       75       80  225  75.000000     B
2   Charlie    50       40       60  150  50.000000     C

Topper is Alice
Math           95
Science        88
English        92
Sum           275
Avg         91.666666
Grade           A
Name: 0, dtype: object
🤝 Contributing
Contributions are welcome!
Fork the repository, enhance it, and submit a pull request.
👨‍💻 Author
Soumyadeep Das
GitHub
