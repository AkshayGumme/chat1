import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.Div(
            id='sidebar',
            style={
                'width': '250px',
                'backgroundColor': '#075e54',
                'color': 'white',
                'padding': '20px',
            },
            children=[
                # Sidebar content goes here
                html.H2('Sidebar'),
            ]
        ),
        html.Div(
            id='chat',
            style={'flex': 1, 'padding': '20px', 'overflowY': 'scroll', 'flexDirection': 'column'},
            children=[
                # Chat messages go here
                html.Div('Sender: Hello!'),
                html.Div('Receiver: Hi there!'),
                html.Div('Sender: How are you?'),
            ]
        ),
        html.Div(
            id='input-container',
            style={
                'display': 'flex',
                'flex-direction':"column",
                'justifyContent': 'space-between',
                'padding': '20px',
                'backgroundColor': 'white',
                'boxShadow': '0px -5px 5px -5px #000000',
            },
            children=[
                dcc.Input(
                    id='input',
                    type='text',
                    placeholder='Type a message...',
                    style={'flex': 1, 'padding': '10px', 'border': 'none', 'borderRadius': '5px'}
                ),
                html.Button(
                    id='send-button',
                    children='Send',
                    n_clicks=0,
                    style={
                        'backgroundColor': '#128c7e',
                        'color': 'white',
                        'padding': '10px 20px',
                        'border': 'none',
                        'borderRadius': '5px',
                        'cursor': 'pointer',
                    }
                ),
            ]
        ),
    ],
    style={'display': 'flex','flex-direction':"column",}
)

if __name__ == '__main__':
    app.run_server(debug=True)
