def calculate_ranking(df):

    df = df.copy()

    df["Rank"] = (
        df["G3"]
        .rank(method="min", ascending=False)
        .astype(int)
    )

    return df