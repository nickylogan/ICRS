import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from layout import Root
from callbacks import register_callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, './assets/custom.css'])
app.layout = html.Div(Root())
app.title = 'Playground | ICRS'
app.config['suppress_callback_exceptions'] = True

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
