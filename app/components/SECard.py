import dash_bootstrap_components as dbc
import dash_html_components as html


class SECard:
    @staticmethod
    def render():
        element = dbc.Card([
                dbc.CardBody([
                    html.H4("Software Engineering", className="card-title"),
                    html.P("Predicted Performance: 53%", className="card-subtitle"),
                ])
            ],
            color="secondary",
            className="text-primary"
        )
        return element