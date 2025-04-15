import pandas as pd
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'D'
df = pd.read_csv('python/data/student_scores.csv')
# print(df)
df["Sum"]=df[["Math","Science","English"]].sum(axis=1)
# print(df)
df["Avg"]=df[["Math","Science","English"]].mean(axis=1)
df["Grade"]=df["Avg"].apply(get_grade)
df1=df.sort_values(by="Sum",ascending=False)
print(df1)
df1 = df1.reset_index(drop=True)
print(f"Topper is {df1.loc[0]}")
