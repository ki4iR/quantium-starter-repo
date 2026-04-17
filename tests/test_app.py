# from contextvars import copy_context
# from dash._callback_context import context_value
# from dash._utils import AttributeDict
#
# # Import the names of callback functions you want to test
# from app import display, update
#
# def test_update_callback():
#     output = update(1, 0)
#     assert output == 'button 1: 1 & button 2: 0'
#
# def test_display_callback():
#     def run_callback():
#         context_value.set(AttributeDict(**{"triggered_inputs": [{"prop_id": "btn-1-ctx-example.n_clicks"}]}))
#         return display(1, 0, 0)
#
#     ctx = copy_context()
#     output = ctx.run(run_callback)
#     assert output == f'You last clicked button with ID btn-1-ctx-example'


from app import dash_app
from dash import html, dcc


def test_header_present():
    layout = dash_app.layout
    # Find the H1 header
    headers = [c for c in layout.children if isinstance(c, html.H1)]
    assert len(headers) == 1
    assert headers[0].children == "Pink Morsel Visualizer"


def test_visualisation_present():
    layout = dash_app.layout
    graphs = [c for c in layout.children if isinstance(c, dcc.Graph)]
    assert len(graphs) == 1
    assert graphs[0].id == "visualization"


def test_region_picker_present():
    layout = dash_app.layout
    radios = [c for c in layout.children if isinstance(c, dcc.RadioItems)]
    assert len(radios) == 1
    assert radios[0].id == "radio-btns"
    assert radios[0].options == ['South', 'West', 'East', 'North', 'All']