import dash_bootstrap_components as dbc
import dash_html_components as html
from .components import Header, TermCardContainer, RecommendationContainer

# The main layout of the app
def Root():
    element = dbc.Container([
        Header.render(),
        html.Hr(),
        TermCardContainer.render(),
        html.Hr(),
        RecommendationContainer.render(),
    ], className="pb-5 mb-5")
    return element