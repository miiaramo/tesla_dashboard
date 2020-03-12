from flask import Flask, render_template
import pandas as pd
import plotly
import json
import plotly.graph_objs as go
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html

from waitress import serve

tesla = pd.read_csv("data/tesla.csv")
app = dash.Dash()

colors = {
    "background": "white",
    "text": "#7FDBFF"
}

navbar = {
    "font-family":"Arial, Helvetica, sans-serif",
    "display": "inline-block",
    "color": "white",
    "text-align": "center",
    "padding": "14px 16px",
    "text-decoration": "none",
    "background": "grey",
}

app.layout = html.Div(style={"backgroundColor": colors["background"]}, children=[
    html.Div(
        children=[
            html.A(
                "First",
                style=navbar
            ),
            html.A(
                "Second",
                style=navbar
            ),
        ],
        style={"background":"grey"}
    ),
    html.Div(
        dcc.Graph(
            id="daily",
            figure={
                "data": [
                    {
                        "x": pd.to_datetime(tesla["Date"]), 
                        "y": tesla["Volume"], "type": "line", 
                        "name": "Daily volume 2010-2017"
                    },
                ],
                "layout": {
                    "plot_bgcolor": "white",
                    "paper_bgcolor": colors["background"],
                    "font": {
                        "color": "black"
                    },
                    "title": "Tesla daily stock volume",
                    "xaxis": {"title":"bll"},
                    "yaxis": {"title":"bll"}
                }
            }
        )
    )
])


class Dashboard:

    @staticmethod
    def run():
        import os
        try:
            PORT = os.getenv["PORT"]
        except:
            PORT = 8000
        serve(app.server, host="0.0.0.0", port=PORT)
    
    @staticmethod
    def test():
        print("Hello world!")