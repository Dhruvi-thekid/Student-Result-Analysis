# Student Result Analysis System

A Python-based data analysis project that analyzes student academic performance using the Student Performance dataset.

The project performs data cleaning, result calculation, statistical analysis, student ranking, visualization, and individual student result search.


## Features

- Load student data from CSV
- Clean and validate the dataset
- Calculate student percentage and grades
- Determine pass/fail results
- Rank students based on final marks
- Perform statistical analysis
- Analyze subject-wise performance
- Search for individual student results
- Generate student performance charts
- Generate a processed results CSV file


## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- CSV
- VS Code


## Dataset

The project uses the Student Performance dataset containing academic and personal information about students.

The dataset used in this project is the Portuguese subject dataset (`student-por.csv`).

It contains:

- 649 student records
- 33 columns
- Academic grades such as G1, G2, and G3
- Study time, absences, school, gender, age, and other student-related attributes

The final grade (`G3`) is used as the main measure of final academic performance.


## Project Structure

```text
Student-Result-Analysis/
│
├── data/
│   └── student-por.csv
│
├── output/
│   ├── charts/
│   └── student_results.csv
│
├── src/
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── result_calculator.py
│   ├── ranking.py
│   ├── analysis.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Dhruvi-thekid/Student-Result-Analysis
cd Student-Result-Analysis
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py



## Analysis Performed

The project performs the following analysis:

- Average, highest, and lowest final marks
- Median and standard deviation
- Overall pass percentage
- Comparison of G1, G2, and G3 marks
- Pass/fail distribution
- Top 10 students based on final marks
- Study time vs final marks
- Absences vs final marks
- Gender-wise average performance
- Correlation between numerical variables


## Output

The project generates:

- Student performance charts in `output/charts/`
- A processed student results file in `output/student_results.csv`
- Individual student result information through the student search feature


## Future Improvements

- Add a graphical user interface
- Add database support
- Generate PDF reports
- Add interactive dashboards
- Add more advanced student performance analysis
- Deploy the application as a web-based system