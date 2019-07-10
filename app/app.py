import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from container import Root

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, './assets/custom.css'])
app.layout = html.Div([Root.render()])
app.title = 'Playground | ICRS'

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
