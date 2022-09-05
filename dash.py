# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



data=pd.read_csv("excel_final.xls - Worksheet.csv")

data.rename(columns = {'Unnamed: 0':'Annee'}, inplace = True)
def switch(st):
    if "," in st:
        i=st.index(",")
        return float(st[:i]+"."+st[i+1:])
    return float(st)

for c in ["chomage","activite","nuitées_touristiques","nbr_eleve_lycee"]:
    data[c]=[switch(x) for x in data[c].values]

data["nbr_eleve_lycee"]=[int(x) for x in data["nbr_eleve_lycee"].values]
data["nuitées_touristiques"]=[int(x) for x in data["nuitées_touristiques"].values]

med_par_pop=[list(data["population"].values)[i]/list(data["nbr_medecin"].values)[i] for i in range(8)]
data["pop_pour_UN_med"]=med_par_pop


years=["2013","2014","2015","2016","2017","2018","2019","2020"]

c=["chomage","activite"]
t=["nuitées_touristiques","nbr_lits_touristiques"]

app = Dash(__name__)

colors = {
    'background': '#363b56'
}

fig = px.bar(data, x="Annee", y="chomage", barmode="group")

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
    Output('pop', 'children'),
    Input('slider', 'value'))
def pop(year):
    a=list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])[1]
    p=str(int(a))
    popul=p[:3]+"."+p[3:]
    return popul+ "  habitants"
@app.callback(
    Output('etd', 'children'),
    Input('slider', 'value'))
def etudiant(year):
    a=list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])[7]+list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])[8]+list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])[9]
    b=a/list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])[1]*100
    s=str(round(b,2))+"%"
    return s

@app.callback(
    Output('prm', 'children'),
    Input('slider', 'value'))
def prim(year):
    a_list=list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])
    a=a_list[7]+a_list[8]+a_list[9]
    b=(a_list[7]/a)*100
    s=str(round(b,2))+"%"
    return s

@app.callback(
    Output('col', 'children'),
    Input('slider', 'value'))
def col(year):
    a_list=list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])
    a=a_list[7]+a_list[8]+a_list[9]
    b=(a_list[8]/a)*100
    s=str(round(b,2))+"%"
    return s

@app.callback(
    Output('lyc', 'children'),
    Input('slider', 'value'))
def lyc(year):
    a_list=list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])
    a=a_list[7]+a_list[8]+a_list[9]
    b=(a_list[9]/a)*100
    s=str(round(b,2))+"%"
    return s


@app.callback(
    Output('med', 'children'),
    Input('slider', 'value'))
def med(year):
    a=list(list(data.loc[data["Annee"]==int(year)+2013].values)[0])[10]
    return int(a)

@app.callback(
    Output("chomage",'figure'),
    Input("radio_1","value")
)
def update_graph_chomage(input_value):
    if input_value=="Chomage":
        input_radio="chomage"
    else:
        input_radio="activite"
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Annee"], y=data[input_radio],
                    mode='lines+markers', line_color="orange",
                    name=input_value))
    fig.update_layout(
        title="Variation du pourcentage du "+input_value+" entre 2013 et 2020",
        plot_bgcolor='#363b56',
        font_color='#FFFFFF',
        paper_bgcolor='#464C68',
        legend=dict(
            bgcolor='#363b56',
            bordercolor='#363b56'
        ))
    return fig

@app.callback(
    Output("tourisme",'figure'),
    Input("radio_2","value")
)
def update_graph_touris(input_value):
    if input_value=="Nombre des nuitées touristiques":
        input_radio="nuitées_touristiques"
    else:
        input_radio="nbr_lits_touristiques"
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data["Annee"], y=data[input_radio],marker_color='yellow',name=input_value))
    fig.update_layout(
        title="Variation du pourcentage du "+input_value+" entre 2013 et 2020",
        plot_bgcolor='#363b56',
        font_color='#FFFFFF',
        paper_bgcolor='#464C68',
        legend=dict(
            bgcolor='#363b56',
            bordercolor='#363b56'
        ))
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)
