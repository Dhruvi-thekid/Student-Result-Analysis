def perform_analysis(df):
    print("--------Statisctical Analysis-------")

    print("Total Students:", len(df))
    print("Average Final Marks:", round(df["G3"].mean(), 2))
    print("Highest Final Marks:", df["G3"] .max())
    print("Lowest Final Marks:", df ["G3"]. min())
    print("Medium Final Marks:", round(df["G3"].median(), 2))
    print("Stnadard Deviation", round(df["G3"].std(), 2))
    pass_percentage = (df["Result"]== "Pass").mean()*100
    print("Pass Percentage:", round(pass_percentage, 2),"%")

    print("\n--- Subject Performance ---")

    print("Average First Period Marks (G1):", round(df["G1"].mean(), 2))
    print("Average Second Period Marks (G2):", round(df["G2"].mean(), 2))
    print("Average Final Marks (G3):", round(df["G3"].mean(), 2))

    print("\n--- Result Summary ---")

    pass_count = (df["Result"] == "Pass").sum()
    fail_count = (df["Result"] == "Fail").sum()

    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)

    print("\n--- Top 10 Students ---")

    top_students = df.sort_values("G3", ascending=False).head(10)

    print(top_students[["school", "sex", "G1", "G2", "G3", "Percentage", "Grade", "Rank"]])