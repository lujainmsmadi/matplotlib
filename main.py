import pandas as pd
import numpy as np
#? Load the data into a Pandas DataFrame.
file_path='C:\\Users\\MSI GF63\\Desktop\\vs-projectspython\\matplotTask\\Employee Sample Data - Copy.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')
#?explore the data
print(df.head())
print (df.info())
#? cleaning the data 
###! drop the null values from the data except for the Exit date 
columns_to_check = [col for col in df.columns if col != 'Exit Date']
df= df.dropna(subset=columns_to_check)



#?Change the first 5 rows 
new = {
    'EEID': [101, 102, 103, 104, 105],
    'Full Name': ['Ali', 'Sara', 'Mazen', 'Ayah', 'Leen'],
    'Job Title': ['Manager', 'Sales Representative', 'Marketing Manager', 'Software Engineer', 'HR Manager'],
    'Department': ['Engineering', 'Sales', 'Marketing', 'IT', 'HR'],
    'Business Unit':['Manufacturing','Manufacturing','Manufacturing','Manufacturing','Manufacturing'],
    'Gender':['Male','Female','Male','Female','Female'],
    'Ethnicity':['Arabian','Arabian','Arabian','Arabian','Arabian'],
    'Age': [29,25 , 31, 23, 24],
    'Hire Date': [pd.Timestamp('2018-05-01'), pd.Timestamp('2019-09-15'), pd.Timestamp('2015-08-10'), pd.Timestamp('2019-08-10'),pd.Timestamp('2017-08-10')],
    'Annual Salary':[113527,100000,55000,66000,77000],
    'Bonus %':[20,10,15,5,8],
    'Country':['China','China','China','China','China'],
    'City':['Shijingshang','Shanghai','Shenzhen','Guangzhou','Shenzhen'],
    'Exit Date': ['until now', pd.Timestamp('2024-01-15'), 'until now', pd.Timestamp('2024-02-10'), 'until now']
}

df.iloc[:5] = pd.DataFrame(new)

print(df.head(10))


#?Print the row with the largest salary.

max_salary_row = df.loc[df['Annual Salary'].idxmax()]
print('The employee with the largest salary\n',max_salary_row)

#?Group by department, and get the average age as well as average salary

department_group = df.groupby('Department').agg({
    'Age': 'mean',
    'Annual Salary': 'mean'
})

department_group = department_group.rename(columns={'Age': 'Average Age', 'Annual Salary': 'Average Salary'})
print("Average age and average salary by department:")
print(department_group)

#? Group by 'Department' and 'Ethnicity' and calculate max age, min age, and median salary
dept_eth_group = df.groupby(['Department', 'Ethnicity']).agg({
    'Age': ['max', 'min'],
    'Annual Salary': 'median'
})
print(df.info())

dept_eth_group.columns = ['Max Age', 'Min Age', 'Median Salary']

print("\nMax age, min age, and median salary by department and ethnicity:")
print(dept_eth_group)

# Create a new Excel writer object
with pd.ExcelWriter('cleanedEmployeeSampleData.xlsx') as writer:
    # Save each DataFrame to a different sheet
    df.to_excel(writer, sheet_name='Cleaned Data')
    max_salary_row.to_excel(writer, sheet_name='Max Salary Employee')
    department_group.to_excel(writer, sheet_name='Avg Age and Salary by Dept')
    dept_eth_group.to_excel(writer, sheet_name='Age and Salary by Dept+Ethn')
    
print("Data has been saved to 'cleanedEmployeeSampleData.xlsx'")

import matplotlib.pyplot as plt

# Create a histogram of the 'Age' column

df['Age'].hist(bins=15, figsize=(10, 6))
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('age_distribution.png') 

plt.show()



gender_counts = df['Gender'].value_counts()

# Extract the counts and labels
values = gender_counts.values   
labels = gender_counts.index     

# Plot the pie chart
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Gender ')
plt.savefig('gender.png') 

plt.show()

df = df.sort_values(by='Annual Salary')

# Create a horizontal bar chart
plt.barh(df['Job Title'], df['Annual Salary'], color='red')

# Add labels and title
plt.xlabel('Annual Salary (USD)')
plt.ylabel('Job Title')
plt.title('Annual Salary by Job Title')
plt.savefig('salarywithjob.png') 


plt.show()

x = df['Ethnicity']
y = df['Country']
colors = np.random.randint(980, size=(980))
sizes = 10 * np.random.randint(980, size=(980))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

plt.colorbar()
plt.savefig('country.png') 

plt.show()