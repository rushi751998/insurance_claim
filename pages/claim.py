import dash
from dash import Dash, html, dcc,Input, Output,State,callback
import dash_bootstrap_components as dbc
import logging
from dash import dcc
from datetime import datetime



dash.register_page(__name__, path_template='/claim')
layout = html.Div([
                    dbc.Card(
                            dbc.CardBody([
                                        dbc.Form([html.H2("Fill Claim Details"),
                                            dbc.Row([
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Label("Accident Date *", html_for="example-email-row", width=7,className = 'form-div'),
                                                                ])
                                                ),
                                                dbc.Col(
                                                        html.Div([
                                                                dcc.DatePickerSingle(
                                                                                clearable=True,
                                                                                with_portal=True,
                                                                                id = 'input-date',
                                                                                date=datetime.today().date(), 
                                                                               style = { 'width':'20%'}
                                                                                )
                                                                ])
                                                        ),
                                                ]),
                                            dbc.Row([
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Label("FIR Number *", html_for="example-email-row",className = 'form-div'),
                                                                ])
                                                ),
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Input(type="text", id="fir-number", placeholder="",className = 'form-div')
                                                                ])
                                                        ),
                                                ]),
                                            dbc.Row([
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Label("Number of peoples in car *", html_for="example-email-row", width=7,className = 'form-div'),
                                                                ])
                                                ),
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Input(type="text", id="num-peoples", placeholder="",className = 'form-div')
                                                                ])
                                                        ),
                                                ]),
                                            dbc.Row([
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Label("Policy Number *", html_for="example-email-row", width=7,className = 'form-div'),
                                                                ])
                                                ),
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Input(type="text", id="policy-num", placeholder="",className = 'form-div')
                                                                ])
                                                        ),
                                                ]),
                                            dbc.Row([
                                                dbc.Col(
                                                        html.Div([
                                                                dbc.Label("Description *", html_for="example-email-row", width=7,className = 'form-div'),
                                                                ])
                                                ),
                                                dbc.Col(
                                                        html.Div([
                                                                 dbc.Textarea(className="mb-3", id = 'description',placeholder="",style = {'height':'150px'} )
                                                                ])
                                                        ),
                                                ]),
                                            dbc.Button("Submit", color="primary",id = 'form-submit',href='')   
                                            ],className = 'claim-form')
                                    ]),className = 'form-card')
                    
                    ])



@callback(
        Output("form-submit", "href"),
        Input('input-date', 'date'),
        State('fir-number', 'value'),
        State('num-peoples', 'value'),   
        State('policy-num', 'value'),   
        State('description', 'value'),   
        Input('form-submit', 'n_clicks')
            )
def form(input_date,fir_number,num_peoples,policy_num,description,n_clicks):
    if ((fir_number)!=None) and ((num_peoples)!=None) and ((policy_num)!=None) and ((description)!=None) and (n_clicks!=None):
        print(input_date,fir_number,num_peoples,policy_num,description,n_clicks)
        return "/upload_images"
    else:
        return "/claim"

        





