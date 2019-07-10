import dash_bootstrap_components as dbc
import dash_html_components as html


class MICard:
    @staticmethod
    def render():
        element = dbc.Card([
                dbc.CardBody([
                    html.H4("Medical Informatics", className="card-title"),
                    html.P("Predicted Performance: 66%", className="card-subtitle"),
                ])
            ],
            color="secondary",
            className="text-primary"
        )
        return element