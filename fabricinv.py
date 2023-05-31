from dash import Dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('fabrics.csv')

app.layout = html.Div([  
        html.Div([
            dcc.Dropdown(id='fabric-dropdown',            
                 options=[{'label': i, 'value': i}
                          for i in df['fabricname'].unique()],
                 value= 'Cotton'),  
	dcc.Graph(id='fabric-graph') 
             
           ]),

        html.Div([
            dcc.Dropdown(id='subcat-dropdown',
		 options=[{'label': j, 'value': j}
                          for j in df['fab_category'].unique()],
                 value= 'Egyptian cotton'),
	dcc.Graph(id='subcat-graph') 
            
    	]),
    ])
	
# Set up the callback function
@app.callback(
    Output(component_id='fabric-graph', component_property='figure'),
    [Input(component_id='fabric-dropdown', component_property='value')]
)

def update_graph(fabric):
    filtered_fabric = df[df['fabricname'] == fabric]
    bar_fig = px.bar(filtered_fabric,
                       x= 'fab_category', y='small',
			color='fabricname',
			height=600,width=400,	
                       title=f'Quantity of {fabric}')
    return bar_fig	


@app.callback(
     Output(component_id='subcat-graph', component_property='figure'),
    [Input(component_id='subcat-dropdown', component_property='value')]	
)


def update_graph1(subcat):
    filtered_subcat = df[df['fab_category'] == subcat]
    bar_fig2 = px.bar(filtered_subcat,
                       x= 'fab_category', y='small',
			color='fab_category',
			height=600,width=400,	
                      title=f'Quantity of {subcat}')


    return bar_fig2
  
    
	
   
	

# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)
    



