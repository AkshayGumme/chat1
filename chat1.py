import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Layout of the form
app.layout = html.Div([
    html.H1("Simple Form Example"),
    
    # Text Input
    dcc.Input(
        id='input-username',
        type='text',
        placeholder='Enter your username',
        value=''
    ),
    
    # Dropdown
    dcc.Dropdown(
        id='dropdown-country',
        options=[
            {'label': 'United States', 'value': 'US'},
            {'label': 'Canada', 'value': 'CA'},
            {'label': 'United Kingdom', 'value': 'UK'}
        ],
        value='US',
        placeholder='Select a country'
    ),
    
    # Submit Button
    html.Button('Submit', id='button-submit', n_clicks=0),
    
    # Output Div
    html.Div(id='output-message')
])

# Callback to update the output message
@app.callback(
    Output('output-message', 'children'),
    [Input('button-submit', 'n_clicks')],
    [dash.dependencies.State('input-username', 'value'),
     dash.dependencies.State('dropdown-country', 'value')]
)
def update_output(n_clicks, username, country):
    if n_clicks > 0:
        return f"Submitted! Username: {username}, Country: {country}"

if __name__ == '__main__':
    app.run_server(debug=True)
