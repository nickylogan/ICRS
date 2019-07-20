import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from typing import List, Tuple
from random import randint

CourseList = List[Tuple[str, str]]

# Store the curriculum in a dictionary for easy access
curriculum: CourseList = {
    "Term 1": [
        ("INF0131", "Calculus I"),
        ("INF0221", "Discrete Mathematics"),
        ("INF0381", "Introduction to Informatics"),
        ("INF0011", "Programming Logic"),
    ],
    "Term 2": [
        ("INF0141", "Calculus II"),
        ("INF0621", "Data Structure"),
        ("INF0301", "Java Programming"),
        ("INF0531", "Management Information System"),
        ("INF0601", "Statistics & Probability"),
    ],
    "Term 4": [
        ("INF0031", "Algorithm Analysis"),
        ("INF0271", "Computer Organization & Architecture"),
        ("INF0521", "Database Systems"),
        ("INF0021", "Matrices & Linear Algebra"),
        ("INF0291", "Object-Oriented Programming"),
    ]
}

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

class TermCardContainer:
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

class TermCard:
    @staticmethod
    def render(title, courses: CourseList):
        element = dbc.Card([
            dbc.CardBody([
                html.H4(title, className="card-title text-white mb-0"),
            ]),
            dbc.ListGroup([CourseInput.render(course[0], course[1]) for course in courses], flush=True)
        ], color="primary text-primary mt-3")
        return element

class CourseInput:
    @staticmethod
    def render(id, name):
        element = dbc.ListGroupItem([
            name,
            ScoreInput.render(id),
        ], className="d-flex justify-content-between align-items-center")
        return element

class ScoreInput:
    @staticmethod
    def render(id):
        element = dcc.Dropdown(
            options=[
                {'label': 'A', 'value':  0},
                {'label': 'A-', 'value': 1},
                {'label': 'B+', 'value': 2},
                {'label': 'B', 'value':  3},
                {'label': 'B-', 'value': 4},
                {'label': 'C+', 'value': 5},
                {'label': 'C', 'value':  6},
                {'label': 'C-', 'value': 7},
                {'label': 'D', 'value':  8},
                {'label': 'E', 'value':  9},
            ],
            id="input-" + id,
            className="dropdown-group",
            clearable=False,
            value=randint(0, 9)
        )
        return element

class RecommendationContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col([
                    html.H2("Recommended Concentration"),
                    html.Span(id="concentration-data", className="d-none")
                ]),
                className="mt-4"
            ),
            dbc.CardDeck([IIMHeader.render(), MIHeader.render(), SEHeader.render()], className="mt-3"),
        ]
        return html.Div(element)

class IIMHeader:
    @staticmethod
    def render():
        element = dbc.Card([
                dbc.CardBody([
                    html.H4("Interactive & Intelligent Media", className="card-title"),
                    html.Small("Recommended", id="iim-recommended", className="card-subtitle"),
                ]),
                dbc.CardFooter([
                    "Predicted Performance: ",
                    html.Span("77", id="iim-performance"),
                    "%",
                ], className="border-0"),
            ],
            id="iim-header",
            color="primary",
            className="text-white"
        )

        return element

class MIHeader:
    @staticmethod
    def render():
        element = dbc.Card([
                dbc.CardBody([
                    html.H4("Medical Informatics", className="card-title"),
                    html.Small("Recommended", id="mi-recommended", className="card-subtitle"),
                ]),
                dbc.CardFooter([
                    "Predicted Performance: ",
                    html.Span("65", id="mi-performance"),
                    "%"
                ], className="border-0")
            ],
            id="mi-header",
            color="secondary",
            className="text-primary"
        )
        return element

class SEHeader:
    @staticmethod
    def render():
        element = dbc.Card([
                dbc.CardBody([
                    html.H4("Software Engineering", className="card-title"),
                    html.Small("Recommended", id="se-recommended", className="card-subtitle"),
                ]),
                dbc.CardFooter([
                    "Predicted Performance: ",
                    html.Span("53", id="se-performance"),
                    "%"
                ], className="border-0")
            ],
            id="se-header",
            color="secondary",
            className="text-primary"
        )
        return element

