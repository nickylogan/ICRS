import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from app.layout import Root
from app.callbacks import register_callbacks
from app.routes import register_routes

# Initial app configuration
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, './assets/custom.css'])
app.layout = html.Div(Root())
app.title = 'Playground | ICRS'
app.config['suppress_callback_exceptions'] = True

register_callbacks(app)

register_routes(app)

# This is the main entry point of the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
