import dash
from dash import Dash, html, dcc,Input, Output,State,callback
import dash_bootstrap_components as dbc
import logging

# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
app = Dash(__name__, use_pages=True,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dash.page_container
])

    
if __name__ == '__main__':  
    app.run(debug=True,port=5000) 