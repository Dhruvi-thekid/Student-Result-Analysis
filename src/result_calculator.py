def calculate_results(df):
    df = df.copy()
    df["Student_ID"] = range(1, len(df) + 1)


    df["Percentage"] = (df["G3"] / 20) * 100

    df["Grade"] = df["Percentage"].apply(calculate_grade)

    df["Result"] = df["G3"].apply(lambda x: "Pass" if x >= 10 else "Fail")

    return df


def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

