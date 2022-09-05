import dash
from dash import dcc, html

from django_plotly_dash import DjangoDash



years=["2013","2014","2015","2016","2017","2018","2019","2020"]
colors = {
    'background': '#363b56'
}

app = DjangoDash('SimpleExample')   # replaces dash.Dash

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.Div([
        html.Div([
            html.H1("Panorama économique de la région DAKHLA-OUAD DAHAB", style={'color': '#DE2342','textAlign':'center','font-weight': 'bold'}),
            ],style={'width': '90%', 'display': 'inline-block'}),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.Div([
            dcc.Slider(
                id="slider",
                min=0,
                max=8,
                value=0,
                marks={i:years[i] for i in range(8)},
                included=False,
                step=None)
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H1("                                                              ")
        ]),
        html.Div([
            html.H4("Population :",style={'color':'#90BFDC'})
        ]),
         html.Div([
            html.P(id='pop', style={
                       'textAlign': 'center',
                       'color': 'yellow',
                       'fontSize': 40,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.H4("L'éducation : primaire, collège et lycée :",style={'color':'#90BFDC'})
        ]),
        html.Div([
            html.P('Pourcentage des étudiants sous 18 ans', style={
                       'textAlign': 'center',
                       'color': '#F3D51A',
                       'fontSize': 15,
                       'margin-top': '-18px'}),
            html.P(id='etd', style={
                       'textAlign': 'center',
                       'color': '#F3D51A',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.P('pourcentge des étudiants du primaire', style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 15,
                       'margin-top': '-18px'}),
            html.P(id='prm', style={
                       'textAlign': 'center',
                       'color': '#dd1e35',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.P('pourcentge des étudiants du collége',style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 15,
                       'margin-top': '-18px'}), 
            html.P(id='col',style={
                       'textAlign': 'center',
                       'color': 'green',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.P('pourcentge des étudiants du lycée',style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 15,
                       'margin-top': '-18px'}), 
            html.P(id='lyc',style={
                       'textAlign': 'center',
                       'color': '#e55467',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
            html.H4("La relation entre le nombre des médecins et la population :",style={'color':'#90BFDC'})
        ]),
        html.Div([
            html.P('population pour un médecin',style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 15,
                       'margin-top': '-18px'}), 
            html.P(id='med',style={
                       'textAlign': 'center',
                       'color': 'orange',
                       'fontSize': 25,
                       'margin-top': '-18px'})
        ]),
        html.Div([
        html.Div([
            dcc.RadioItems(
                id="radio_1",
                options=[{'label':i, 'value':i} for i in ["Chomage","Activité"]],
                value="chomage",
                style={'color': 'white',
                       'fontSize': 23},
                labelStyle={"display":"inline-block"})
        ]),
        html.Div([dcc.Graph(id="chomage")])
    ]),
    html.Div([
        html.Div([
            dcc.RadioItems(
                id="radio_2",
                options=[{'label':i, 'value':i} for i in ["Nombre des nuitées touristiques","Nombre des lits touristiques"]],
                value="Nombre des nuitées touristiques",
                style={'color': 'white',
                       'fontSize': 23},
                labelStyle={"display":"inline-block"})
        ]),
        html.Div([dcc.Graph(id="tourisme")])
        ])
    ])
    ])
])

@app.callback(
    dash.dependencies.Output('output-color', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value')])
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value

@app.callback(
    dash.dependencies.Output('output-size', 'children'),
    [dash.dependencies.Input('dropdown-color', 'value'),
     dash.dependencies.Input('dropdown-size', 'value')])
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." %(dropdown_size, dropdown_color)