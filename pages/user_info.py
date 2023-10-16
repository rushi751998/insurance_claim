import dash
from dash import Dash, html, dcc,Input, Output,State,callback
import dash_bootstrap_components as dbc
import logging
dash.register_page(__name__, path_template='/user_info')


layout = html.Div([
                html.Div([
                        dbc.Card(
                                dbc.CardBody(
                                        [
                                        html.H4("Title", className="card-title"),
                                        html.H6("Card subtitle", className="card-subtitle"),
                                        html.P(
                                                "Some quick example text to build on the card title and make "
                                                "up the bulk of the card's content.",
                                                className="card-text",
                                        ),
                                        dbc.CardLink("Card link", href="#"),
                                        dbc.CardLink("External link", href="https://google.com"),
                                        ]
                                        ),
                                        style={"width": "18rem"},
                                ),
                        dbc.Card(
                                html.Div([
                                        dbc.CardBody(
                                        html.Div([
                                        dbc.Button(
                                        "Current Policy",
                                        id="collapse-button-current-policy",
                                        className="mb-3",
                                        color="primary",
                                        n_clicks=0,
                                        ),
                                
                                        dbc.Collapse(
                                                dbc.Card(
                                                        html.Div([dbc.CardHeader(
                                                                dbc.Row([
                                                                        dbc.Col(html.Div("Policy Category"), width=5, lg=3),
                                                                        dbc.Col(html.Div("Policy Number"), width=3, lg=3),
                                                                        dbc.Col(html.Div("Action"), width=4, lg=3),
                                                                        
                                                                        ])
                                                                ),
                                                        dbc.CardBody(
                                                                dbc.Row([
                                                                        dbc.Col(html.Div("car"), width=5, lg=3),
                                                                        dbc.Col(html.Div("1234"), width=3, lg=3),
                                                                        dbc.Col(html.Div([dbc.Button("Claim", color="light", className="me-1",id = 'submit-claim'),
                                                                                dbc.Button("Policy", color="light", className="me-1",id = 'see-policy')]), width=3, lg=3),
                                                                        ])
                                                                )])
                                                                ),
                                                id="collapse-current-policy",
                                                is_open=False,
                                                )
                                        ])),
                                dbc.CardBody(
                                        html.Div([
                                        dbc.Button(
                                        "Expird Policy",
                                        id="collapse-button-expired-policy",
                                        className="mb-3",
                                        color="primary",
                                        n_clicks=0,
                                        ),
                                
                                        dbc.Collapse(
                                                dbc.Card(
                                                        html.Div([dbc.CardHeader(
                                                                dbc.Row([
                                                                        dbc.Col(html.Div("Policy Category"), width=5, lg=3),
                                                                        dbc.Col(html.Div("Policy Number"), width=3, lg=3),
                                                                        dbc.Col(html.Div("Action"), width=4, lg=3),
                                                                        
                                                                        ])
                                                                ),
                                                        dbc.CardBody(
                                                                dbc.Row([
                                                                        dbc.Col(html.Div("car"), width=5, lg=3),
                                                                        dbc.Col(html.Div("1234"), width=3, lg=3),
                                                                        dbc.Col(html.Div([
                                                                                        # dbc.Button("Claim", color="light", className="me-1",id = 'submit-claim'),
                                                                                        dbc.Button("Policy", color="light", className="me-1",id = 'see-policy')]), width=3, lg=3),
                                                                        ])
                                                                )])
                                                                ),
                                                id="collapse-expired-policy",
                                                is_open=False,
                                                )
                                        ]))]),
                                 ),
                        html.Div(id = 'see-claim-output')
                        
                                        
                
                        ],className= 'container')
                        
                ],className = 'userInfo-main-div')


@callback(
    Output("collapse-current-policy", "is_open"),
    [Input("collapse-button-current-policy", "n_clicks")],
    [State("collapse-current-policy", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse-expired-policy", "is_open"),
    [Input("collapse-button-expired-policy", "n_clicks")],
    [State("collapse-expired-policy", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
        Output("submit-claim", "href"),  
        [Input('submit-claim', 'n_clicks')]
            )
def claim(n_clicks):
    # return None
    if (n_clicks!=None):
        # print('\n',n_clicks)
        return "/claim"