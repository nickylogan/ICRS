import dash_bootstrap_components as dbc
import dash_html_components as html
from .TermCard import TermCard

curriculum = {
    "Term 1": [
        ("calculus-1", "Calculus I"),
        ("discrete-math", "Discrete Mathematics"),
        ("intro-inf", "Introduction to Informatics"),
        ("prolog", "Programming Logic"),
    ],
    "Term 2": [
        ("calculus-2", "Calculus II"),
        ("data-structure", "Data Structure"),
        ("java", "Java Programming"),
        ("mis", "Management Information System"),
        ("stats", "Statistics & Probability"),
    ],
    "Term 4": [
        ("algorithm-analysis", "Algorithm Analysis"),
        ("comp-arch", "Computer Organization & Architecture"),
        ("database", "Database Systems"),
        ("linear-algebra", "Matrices & Linear Algebra"),
        ("oop", "Object-Oriented Programming"),
    ]
}


class CardContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col(
                    html.H2("Score Input"),
                ),
                className="mt-4"
            ),
            dbc.Row([
                dbc.Col(TermCard.render(title, courses), md=4) for title, courses in curriculum.items()
            ], className="mt-3"),
            dbc.Row(
                dbc.Col(
                    dbc.Button("Pick a concentration for me!",
                               outline=True, color="primary", id="submit-button", className="ml-auto")
                ),
                className="mt-5 mb-5",
            )
        ]
        return html.Div(element)
