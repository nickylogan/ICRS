import dash_bootstrap_components as dbc
import dash_html_components as html


class Header:
    @staticmethod
    def render():
        element = [
            dbc.Row([
                dbc.Col([
                    html.H1("Informatics Concentration Recommender System (ICRS)"),
                    html.P("It is often hard to choose the concentration for your major. If you're an UPH Informatics major student, you're in luck!"),
                    html.P("Input your courses' scores below and we'll recommend the best suited concentration for you.")
                ], md=6),
            ],
                className="mt-5"
            )
        ]
        return html.Div(element)
