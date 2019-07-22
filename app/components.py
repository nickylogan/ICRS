from random import randint
from typing import List, Tuple

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

CourseList = List[Tuple[str, str]]

# Store the curriculum in a dictionary for easy access
curriculum: CourseList = {
    "Term 1": [
        ("calculus1", "Calculus I"),
        ("discrete_math", "Discrete Mathematics"),
        ("intro_to_it", "Introduction to Informatics"),
        ("prolog", "Programming Logic"),
    ],
    "Term 2": [
        ("calculus2", "Calculus II"),
        ("data_structure", "Data Structure"),
        ("java", "Java Programming"),
        ("mis", "Management Information System"),
        ("stats", "Statistics & Probability"),
    ],
    "Term 4": [
        ("algo_analysis", "Algorithm Analysis"),
        ("computer_arch", "Computer Organization & Architecture"),
        ("database", "Database Systems"),
        ("linear_algebra", "Matrices & Linear Algebra"),
        ("oop", "Object-Oriented Programming"),
    ]
}


class Header:
    @staticmethod
    def render():
        element = [
            dbc.Row([
                dbc.Col([
                    html.H1("Informatics Concentration Recommender System (ICRS)"),
                    html.P(
                        "It is often hard to choose the concentration for your major. If you're an UPH Informatics major student, you're in luck!"),
                    html.P(
                        "Input your courses' scores below and we'll recommend the best suited concentration for you.")
                ], md=6),
            ],
                className="mt-5"
            )
        ]
        return html.Div(element)


class Tabs:
    @staticmethod
    def render():
        element = dbc.Tabs(
            [
                dbc.Tab(label="Playground", tab_id="playground",
                        tab_style={'cursor': 'pointer'}),
                dbc.Tab(label="Batch Processor", tab_id="batch",
                        tab_style={'cursor': 'pointer'}),
            ],
            id="tabs",
            active_tab="playground",
            className="mt-3 mb-5",
        )
        return element


class InputContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col(
                    html.H2("Score Input"),
                ),
                className="mt-4 mb-2"
            ),
            ManualInputContainer.render(),
            BatchInputContainer.render(),
        ]
        return html.Div(element)


class ManualInputContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row([
                dbc.Col(TermCard.render(title, courses), md=4) for title, courses in curriculum.items()
            ]),
            dbc.Row(
                dbc.Col(
                    dbc.Button("Pick a concentration for me!",
                               outline=True, color="primary", id="submit-button", className="ml-auto")
                ),
                className="mt-5 mb-5",
            )
        ]
        return html.Div(element, id="manual-input-container")


class BatchInputContainer:
    @staticmethod
    def render():
        element = [
            dbc.Button("Download template", color="link",
                       style={'textDecoration': 'underline'}),
            dbc.Col(
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        html.Span(
                            'DRAG AND DROP OR',
                            className="text-primary",
                            style={'fontSize': '0.765625rem'}
                        ),
                        html.Br(),
                        dbc.Button([
                            "Click to upload a ", html.Code(" .csv ")," file"
                        ], color="link", className="p-0"),
                        html.Br(),
                        html.Small(
                            'Maximum size: 2MB',
                            className="text-secondary",
                            style={'fontSize': '0.765625rem'}
                        ),
                    ]),
                    style={
                        'width': '100%',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                    },
                    className="py-5 text-center",
                    className_active="bg-secondary",
                    className_reject="bg-danger text-white",
                    accept='.csv',
                    max_size=2000000,
                )
            ),
            dbc.Col(html.H3("Data Preview"), className="mt-4"),
            dbc.Col(id="batch-preview"),
        ]
        return dbc.Row(element, id="batch-input-container")


class TermCard:
    @staticmethod
    def render(title, courses: CourseList):
        element = dbc.Card([
            dbc.CardBody([
                html.H4(title, className="card-title text-white mb-0"),
            ]),
            dbc.ListGroup([CourseInput.render(course[0], course[1])
                           for course in courses], flush=True)
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
                {'label': '-', 'value': -1},
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
            value=-1
        )
        return element


class RecommendationContainer:
    @staticmethod
    def render():
        element = [
            dbc.Row(
                dbc.Col([
                    html.H2("Recommended Concentration"),
                    html.Span(id="manual-output", className="d-none"),
                    html.Span(id="batch-output", className="d-none"),
                    html.Span(id="concentration-data", className="d-none"),
                ]),
                className="mt-4"
            ),
            ManualOutputContainer.render(),
            BatchOutputContainer.render(),
        ]
        return html.Div(element)


class ManualOutputContainer:
    @staticmethod
    def render():
        element = html.Div([
            html.P(
                "Fill up your scores and we'll try to choose the best concentration for you!",
                id="manual-welcome",
            ),
            dbc.Alert(
                id="manual-error",
                color="danger",
                className="d-none",
            ),
            html.Div(
                dbc.CardDeck(
                    [IMDDHeader.render(), MIHeader.render(), SEHeader.render()],
                    className="mt-3",
                ),
                id="manual-deck",
                className="d-none",
            ),
        ],
            id="manual-output-container"
        )
        return element


class IMDDHeader:
    @staticmethod
    def render():
        element = dbc.Card([
            dbc.CardBody([
                html.H4("Interactive & Intelligent Media",
                        className="card-title"),
                html.Small("Recommended", id="imdd-recommended",
                           className="card-subtitle"),
            ]),
            dbc.CardFooter([
                "Predicted Performance: ",
                html.Span("-", id="imdd-performance"),
            ], className="border-0"),
        ],
            id="imdd-header",
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
                html.Small("Recommended", id="mi-recommended",
                           className="card-subtitle"),
            ]),
            dbc.CardFooter([
                "Predicted Performance: ",
                html.Span("-", id="mi-performance"),
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
                html.Small("Recommended", id="se-recommended",
                           className="card-subtitle"),
            ]),
            dbc.CardFooter([
                "Predicted Performance: ",
                html.Span("-", id="se-performance"),
            ], className="border-0")
        ],
            id="se-header",
            color="secondary",
            className="text-primary"
        )
        return element


class BatchOutputContainer:
    @staticmethod
    def render():
        element = html.Div(
            dbc.Row(
                dbc.Col(
                    html.P("Predicted results for your data will appear here"),
                    id="batch-results-container"
                ),
            ),
            id="batch-output-container"
        )
        return element


class BatchTable:
    @staticmethod
    def render(df: pd.DataFrame):
        element = dbc.Table.from_dataframe(
            df=df,
            striped=True,
            float_format=".2f",
            id="batch-table",
            size="sm",
            responsive=True,
            hover=True,
            className="mt-3",
        )
        return element
