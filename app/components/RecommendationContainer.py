import dash_bootstrap_components as dbc
import dash_html_components as html
from .IIMCard import IIMCard
from .MICard import MICard
from .SECard import SECard

class RecommendationContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col(
                    html.H2("Recommended Concentration"),
                ),
                className="mt-4"
            ),
            dbc.CardDeck([IIMCard.render(), MICard.render(), SECard.render()], className="mt-3"),
        ]
        return html.Div(element)
