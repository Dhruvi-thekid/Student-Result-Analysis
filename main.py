from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.result_calculator import calculate_results
from src.ranking import calculate_ranking
from src.analysis import perform_analysis
from src.visualization import create_charts



DATA_FILE = "data/student-por.csv"

df = load_data(DATA_FILE)
#print(df.head())

#print("Data shape:", df.shape)
#print("Column Names:", df.columns.tolist())
#print("Data Types:", df.dtypes)
#print("Missing values:", df.isnull().sum())

df = clean_data(df)

#print("-----Final Dataset shape------")
#print(df.shape)

df = calculate_results(df)
print("------Student Results------")
print(df[["G1", "G2", "G3", "Percentage", "Grade", "Result"]].head(10))

df = calculate_ranking(df)
print("-----Top 10 Students-------")

top_students = df.sort_values("Rank").head(10)
print(
    top_students[
        ["Rank", "G1","G2","G3","Percentage", "Grade", "Result"]
        ]
    )

df = calculate_ranking(df)
perform_analysis(df)

print("---------Top 10 Students--------")
top_students= df.sort_values("Rank").head(10)

print(
    top_students[
        ["Rank", "G1", "G2", "G3", "Percentage", "Grade", "Result"]
    ]
)

perform_analysis(df)
create_charts(df)


df.to_csv("output/student_results.csv", index=False)

print("\nProcessed student results saved successfully.")




student_id = input("\nEnter student number to search: ")

student = df[df["Student_ID"] == int(student_id)]

if not student.empty:
    print("\nStudent Result:")

    student_data = student.iloc[0]

    print("\n===== STUDENT RESULT =====")
    print("Student ID:", student_data["Student_ID"])
    print("School:", student_data["school"])
    print("Gender:", student_data["sex"])
    print("Age:", student_data["age"])
    print("G1 Marks:", student_data["G1"])
    print("G2 Marks:", student_data["G2"])
    print("Final Marks:", student_data["G3"])
    print("Percentage:", round(student_data["Percentage"], 2), "%")
    print("Grade:", student_data["Grade"])
    print("Result:", student_data["Result"])
    print("Rank:", student_data["Rank"])
    print("==========================")

else:
    print("Student not found.")