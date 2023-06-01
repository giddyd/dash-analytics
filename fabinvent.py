import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Label import Label
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(
    __name__,
    
)
server=app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

colors2 = {
 'background': '#444444',
    'text': '#7FDBFF'
}

colors3 = {
 'background': '#444444',
    'text': '#7FDBFF'
}

df = pd.read_csv(
    "fabrics.csv"
)

fig = px.bar(df, x='fab_category', y='small', color='fab_category', barmode='group')
fig2= px.bar(df, x='fab_category', y='large', color='fab_category', barmode='group')
fig3= px.bar(df, x='fab_category', y='medium', color='fab_category', barmode='group')

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig2.update_layout(
    plot_bgcolor=colors2['background'],
    paper_bgcolor=colors2['background'],
    font_color=colors2['text']
)

fig3.update_layout(
    plot_bgcolor=colors3['background'],
    paper_bgcolor=colors3['background'],
    font_color=colors['text']
)


app.layout = html.Div(children=[
   html.Div([	
         html.Div([	
    	    html.H1(children='Fabric Count for size: Small.'),

        html.Div(children='''
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
]),

#Another graph(another div)
html.Div(children=[
    html.H1(children='Fabric Count for size: Large.'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='graph2',
        figure=fig2
    	),
   ]),
]),

#Another graph(another div)
html.Div(children=[
    html.H1(children='Fabric Count for size: Medium.'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='graph3',
        figure=fig3
    	),
     ]),
  ])



if __name__ == '__main__':
    app.run_server(debug=True)
