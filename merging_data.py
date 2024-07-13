import pandas as pd

df_teachers = pd.read_csv('sorted_teachers.csv')
df_school_data = pd.read_csv('school_data_subset.csv')
df_school_data = df_school_data[["Federal School ID","Entity Type","Street Address", "Virtual Instruction Type", "Street City", "School"]]


merged_df = df_teachers.merge(df_school_data, how="cross")
merged_df["check"] = merged_df.apply(lambda row: str(row["Location"]) in str(row["School"]), axis=1)

merged_df = merged_df[merged_df["check"] == True]
merged_df = merged_df.drop(columns=["check", "Location"])

merged_df = merged_df[['School','Name', 'Title', 'Email', 'Street City','Federal School ID','Entity Type', 'Street Address', 'Virtual Instruction Type']]

merged_df.to_csv("final_data.csv", index=False)
