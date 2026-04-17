# Using the prev given example
import pandas
from dash import Dash, html, dcc
from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./data/pink_morsel.csv"

# load in data (rewrite for part3)
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# create the visualization
line_chart = line(data, x="date", y="sales", color="region", title="Pink Morsel Sales")
visualization = dcc.Graph(
    id="visualization",
    figure=line_chart,
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

radio_btns = dcc.RadioItems(
    options=['South','West','East','North','All'],
    value='All',
    id='radio-btns',
    inline=True
)

# define the app layout
dash_app.layout = html.Div(
    [
        header,
        radio_btns,
        visualization
    ],
    # style={
    #     'backgroundColor': 'black',
    #     'color': 'white',
    #     'fontFamily': 'Inter, Arial, sans-serif',
    #     'fontWeight': '500',
    #     'minHeight': '100vh',
    #     'padding': '20px'
    # }
)

# Creating the callback
# Always before running the served beacuse it won't load it haha xd
from dash.dependencies import Input, Output

@dash_app.callback(
    Output("visualization", "figure"),
    Input("radio-btns", "value")
)
def update_graph(selected_region):
    # If "All" → show everything
    if selected_region == "All":
        filtered = data
    else:
        filtered = data[data["region"].str.lower() == selected_region.lower()]

    # Rebuild the line chart with filtered data
    fig = line(filtered, x="date", y="sales", color="region",
               title="Pink Morsel Sales")
    # Important
    fig.update_layout(
        plot_bgcolor="black",
        paper_bgcolor="black",
        font_color="white"
    )
    return fig

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run()



# from dash import Dash, callback, html, Input, Output, ctx, callback
#
# app = Dash()
#
# app.layout = html.Div([
#     html.Button('Button 1', id='btn-1'),
#     html.Button('Button 2', id='btn-2'),
#     html.Button('Button 3', id='btn-3'),
#     html.Div(id='container'),
#     html.Div(id='container-no-ctx')
# ])
#
# @callback(
#     Output('container-no-ctx', 'children'),
#     Input('btn-1', 'n_clicks'),
#     Input('btn-2', 'n_clicks'))
# def update(btn1, btn2):
#     return f'button 1: {btn1} & button 2: {btn2}'
#
#
# @callback(Output('container','children'),
#               Input('btn-1', 'n_clicks'),
#               Input('btn-2', 'n_clicks'),
#               Input('btn-3', 'n_clicks'))
# def display(btn1, btn2, btn3):
#     button_clicked = ctx.triggered_id
#     return f'You last clicked button with ID {button_clicked}'
#
# if __name__ == '__main__':
#     app.run(debug=True)