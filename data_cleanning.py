import pandas as pd

# Path to your Excel file
file_path = 'school_data.xlsx'

# Read Excel file into a Pandas DataFrame
df_school_data = pd.read_excel(file_path, sheet_name='School Data')
df_teachers = pd.read_csv('teachers.csv')

df_teachers_sorted = df_teachers.sort_values(by='Location')
output_file = 'sorted_teachers.csv'
df_teachers_sorted.to_csv(output_file, index=False)

school_columns = df_school_data.iloc[4].values
print(school_columns)
df_school_data = df_school_data.iloc[5:]
df_school_data.columns = school_columns
df_school_data = df_school_data[['Federal School ID','Entity Type','Street Address','Year Round Yes/No', 'Public Yes/No','Administrator Name', 'Administrator Phone',
 'Administrator Phone Ext.', 'Administrator Email','Virtual Instruction Type', 'School', 'Street City']]

output_file = 'sorted_school.csv'
df_school_data.to_csv("school_data_subset.csv", index=False)