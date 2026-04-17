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
