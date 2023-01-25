import pandas as pd

# Load the dataset from Kaggle into a DataFrame
df = pd.read_csv('Attendance_Sheet.csv')

# Remove non-numeric characters
df["Attendance"] = df["Attendance"].replace({r'[^0-9.]+': ''}, regex=True)

# Convert the Attendance column from object to numeric datatype
df['Attendance'] = pd.to_numeric(df['Attendance'], errors='coerce')

# Group by unique vales for Home country and aggregate of the number of attendees for each country
Home_attendance = df.groupby(['Home'])['Attendance'].sum().reset_index(name='Attendance')

# Rename columns of Home_attendance
Home_attendance.columns = ['Country', 'H_Attend']

# Group by unique vales for Away country and aggregate of the number of attendees for each country.
Away_attendance = df.groupby(['Away'])['Attendance'].sum().reset_index(name='Attendance')

# Rename columns of Away_attendance
Away_attendance.columns = ['Country', 'A_Attend']

merged_df = pd.merge(Home_attendance, Away_attendance, on='Country')
merged_df['Total_Attendance'] = merged_df['H_Attend'] + merged_df['A_Attend']

print(merged_df[['Country', 'Total_Attendance']])


