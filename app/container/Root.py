import dash_bootstrap_components as dbc
import dash_html_components as html
from components import Header, CardContainer

class Root:
    @staticmethod
    def render():
        element = dbc.Container([
            Header.render(),
            html.Hr(),
            CardContainer.render(),
        ], className="pb-5 mb-5")
        return element
