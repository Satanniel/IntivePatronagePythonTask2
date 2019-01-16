from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import pandas as pd
import numpy as np
from django_pandas.io import read_frame
from sklearn.linear_model import LinearRegression
from salaries.models import Employee


def salaries(request):
    # Load the database table into dataframe
    query_set = Employee.objects.all()
    base_table = read_frame(query_set)

    # Create a dataframe wihtout data to calculate
    base_table.drop(['id'], axis=1, inplace=True)
    base_table.reset_index(drop=True, inplace=True)
    filled_table = base_table.dropna()

    # Predict data using linear regression
    x = filled_table[["worked_years"]]
    y = filled_table[["salary_brutto"]]
    LinReg = LinearRegression()
    LinReg.fit(x, y)
    predict_data = base_table[["worked_years"]]
    predicted_salary = pd.DataFrame(LinReg.predict(predict_data))
    predicted_salary.columns = {"salary_brutto"}
    base_table.salary_brutto.fillna(predicted_salary.salary_brutto, inplace=True)

    plt.scatter(x, y,  color='black')
    plt.plot(predict_data, predicted_salary, color='blue', linewidth=3)

    plt.title("Comparison of existing data to predictions obtained by linear regression.")
    plt.xlabel("workedYears")
    plt.ylabel("salaryBrutto")

    # Transform the data into HTML format and render the HTML template
    base_table.columns = ['Worked years', 'Salary brutto']
    html_table = base_table.to_html(index=False)
    return render(request, 'salaries.html', {'html_table': html_table})
