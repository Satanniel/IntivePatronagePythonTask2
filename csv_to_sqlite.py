import pandas as pd
import sqlite3

task_database = sqlite3.connect('db.sqlite3')
salary_csv = pd.read_csv('salary.csv', skipinitialspace=True)
salary_csv.columns = ['worked_years', 'salary_brutto']
print(salary_csv)
salary_csv.to_sql('salaries_employee', task_database, index_label='id', if_exists='replace')
