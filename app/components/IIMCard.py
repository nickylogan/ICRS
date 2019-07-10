import dash_bootstrap_components as dbc
import dash_html_components as html


class IIMCard:
    @staticmethod
    def render():
        element = dbc.Card([
                dbc.CardBody([
                    html.H4("Interactive & Intelligent Media", className="card-title"),
                    html.P("Predicted Performance: 77%", className="card-subtitle"),
                    html.Small("Recommended", className="text-muted"),
                ])
            ],
            color="primary",
            className="text-white"
        )

        return element