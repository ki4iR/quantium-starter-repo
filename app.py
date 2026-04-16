# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import csv

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

months_list = []
montly_sales_list = []

with open('./data/pink_morsel.csv', newline='') as pink_morsel:
    reader = csv.reader(pink_morsel, delimiter=',', quotechar='|')
    # First checkout the set
    #for row in reader:
    #   print(', '.join(row))

    next(reader)  # skips the header otherwise the line count is +1
                  # and I get an error lol

    # I want more precise data, so extract for each month
    # first look at month extraction
    # month_count = 0
    # month_current = "02"
    # for row in reader:
    #     month_new = row[1].split("-")[1]
    #     if month_current != month_new:
    #         month_current = month_new
    #         month_count += 1
    #
    # print(month_count)

    # Now try to extract the average for each month
    month_current = "02"

    montly_sales = 0

    for row in reader:
        # collect for the new month
        month_new = row[1].split("-")[1]
        # print(", ".join(row))
        if month_current != month_new:
            montly_sales_list.append(montly_sales)
            montly_sales = 0
            month_current = month_new
            months_list.append(month_new)

        # accumulate the sales for the month
        montly_sales += float(row[0])

    print(len(montly_sales_list))

    # Check Sales results
    # for i in range(0,len(montly_sales_list)):
    #     print(i,montly_sales_list[i])


for i in range(0, len(months_list)):
    months_list[i] = str(2018 + int(i / 12)) + "-" + str(months_list[i])

print(len(montly_sales_list))
print(len(months_list))

# Graph
df = pd.DataFrame({
    "Sales": montly_sales_list,
    "Month": months_list
})

fig = px.bar(df, x="Month", y="Sales", barmode="group")
fig2 = px.scatter(df, x="Month", y="Sales",
                 size="Sales", hover_name="Month",
                 log_x=True)

app.layout = html.Div(children=[
     html.H1(children='Graph'),
     html.H2(children='''
         Pink Marsel Sales from 2018 to 2022.
     '''),
     dcc.Graph(
         id='Sales Bar Chart',
         figure=fig
     ),
     dcc.Graph(
         id='Sales Scatter Chart',
         figure=fig2
     )
])


if __name__ == '__main__':
     app.run(debug=True)

# In conclusion the graph shows that rising the price of the candy didnt harm its sales
# and that they have risen


# Copy from example
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })
#
# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
#
# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),
#
#     html.Div(children='''
#         Dash: A web application framework for your data.
#     '''),
#
#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])
#
# if __name__ == '__main__':
#     app.run(debug=True)