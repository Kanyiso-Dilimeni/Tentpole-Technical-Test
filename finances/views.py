from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .forms import CustomerForm
import pandas as pd
import plotly
import plotly.graph_objects as go

"""
    After submit button is clicked, the form input is saved to the database.
    The uploaded file is read using pandas (I used pandas mainly because it is way simpler that anything
    else I could find) and the values are plotted onto the graph using plotly.
"""


def index(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Saves the form input to the database
            file_name = str(request.FILES['income_expense_file'].name)  # Gets the file name of the uploaded file
            new_file_name = file_name.replace(' ', '_')     # Returns name where the whitespaces are replaced with
                                                            # underscores.
            print(new_file_name)
            form = CustomerForm()   # Create a blank form

            data_file = pd.read_excel(f"media/files/{new_file_name}")   # Gets the file from it's location

            # Creates the scatter graph using data from the excel files
            data = [go.Scatter(x=data_file['Month'], y=data_file['Income'], legendgroup='Income'),
                    go.Scatter(x=data_file['Month'], y=data_file['Expenses'], legendgroup='Expenses')]

            # Posts the scatter graph to the chart
            fig = go.Figure(data)
            # Shows the chart
            fig.show()

            return render(request, 'index.html')
    else:
        form = CustomerForm()

    # Renders the webpage created by the html file "index"
    return render(request, 'index.html', context={'form': form})
