import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_charts(df):
    os.makedirs("output/charts", exist_ok = True)

    #1. Grade Distribution
    plt.figure(figsize=(8,5))
    sns.countplot(x="Grade", data = df)

    plt.title("Student Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")

    plt.savefig("output/charts/grade_distribution.png")
    plt.show()
    plt.close()

    #2. Final Marks Distribution
    plt.figure(figsize=(8,5))
    sns.histplot(df["G3"], bins = 11, kde =True)

    plt.title("Distribution of Final Marks")
    plt.xlabel("Final Marks")
    plt.ylabel("Number of Students")

    plt.savefig("output/charts/final_marks_distribution.png")
    plt.show()
    plt.close()

    # 3. Study Time vs Final Marks
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="studytime", y="G3", data=df)

    plt.title("Study Time vs Final Marks")
    plt.xlabel("Study Time")
    plt.ylabel("Final Marks")

    plt.savefig("output/charts/studytime_vs_marks.png")
    plt.show()
    plt.close()

    # 4. Absences vs Final Marks
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="absences", y="G3", data=df)

    plt.title("Absences vs Final Marks")
    plt.xlabel("Number of Absences")
    plt.ylabel("Final Marks")

    plt.savefig("output/charts/absences_vs_marks.png")
    plt.show()
    plt.close()

    # 5. Gender-wise Average Final Marks
    plt.figure(figsize=(8, 5))
    sns.barplot(x="sex", y="G3", data=df)

    plt.title("Gender-wise Average Final Marks")
    plt.xlabel("Gender")
    plt.ylabel("Average Final Marks")

    plt.savefig("output/charts/gender_wise_performance.png")
    plt.show()
    plt.close()

    # 6. Correlation Heatmap
    plt.figure(figsize=(10, 8))

    numeric_df = df.select_dtypes(include="number")
    correlation = numeric_df.corr()

    sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

    plt.title("Correlation Between Numerical Variables")

    plt.savefig("output/charts/correlation_heatmap.png")
    plt.show()
    plt.close()

    # 7. Pass/Fail Distribution
    plt.figure(figsize=(7, 5))
    sns.countplot(x="Result", data=df)

    plt.title("Pass vs Fail Distribution")
    plt.xlabel("Result")
    plt.ylabel("Number of Students")

    plt.savefig("output/charts/pass_fail_distribution.png")
    plt.show()
    plt.close()