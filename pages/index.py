import dash
from dash import Dash, html, dcc,Input, Output,State,callback
import dash_bootstrap_components as dbc
import logging
dash.register_page(__name__, path_template='/')

#  html.Div([html.Img(src ="assets/images/corelogic.png")],className= 'nav-bar')
layout = html.Div([
                html.H1("Welcom To ABC Insurance"),
                dbc.Card([
                    dbc.CardBody(
                        dbc.Form([
                                dbc.Row([
                                        dbc.Label("Email", html_for="example-email-row", width=2),
                                        dbc.Col(
                                            dbc.Input(
                                                type="text", id="login_email", placeholder="Enter Email"
                                                    ),width=10,
                                                )],className="mb-3",
                                            ),
                                        dbc.Row([
                                                dbc.Label("Password", html_for="example-password-row", width=2),
                                                dbc.Col(
                                                    dbc.Input(
                                                        type="password",
                                                        id="login_password",
                                                        placeholder="Enter password",
                                                            ),width=10,
                                                )], className="mb-3"
                                            ),
                                        dbc.Button("Submit", color="primary",id = 'login-button',href='')                   
                                ])                        
                    )]
                    ),],
                  id = 'index-main-div',className = 'index-main-div')

@callback(
        Output("login-button", "href"),
        Input('login_email', 'value'),
        Input('login_password', 'value'),   
        [Input('login-button', 'n_clicks')]
            )
def login_page(login_email,login_password,n_clicks):
    # print("--------------------124567")
    email_id ='admin'   
    password ='admin'
    print(login_email,login_password)
    # return None
    if (login_email ==email_id) and (login_password==password) and (n_clicks!=None):
        # print('\n',n_clicks)
        return "/user_info"


