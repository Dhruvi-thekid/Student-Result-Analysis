def clean_data(df):
    print("--------Data Cleaning--------")

    duplicates = df.duplicated().sum()
    print("Number of duplicate rows:", duplicates)

    missing = df.isnull().sum().sum()
    print("Missing values:", missing)

    df = df.drop_duplicates()

    return df

