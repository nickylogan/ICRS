import dash_bootstrap_components as dbc
import dash_html_components as html
from typing import List, Tuple
from .CourseInput import CourseInput

CourseList = List[Tuple[str, str]]

class TermCard:
    @staticmethod
    def render(title, courses: CourseList):
        element = dbc.Card([
            dbc.CardBody([
                html.H4(title, className="card-title text-white mb-0"),
            ]),
            dbc.ListGroup([CourseInput.render(course[0], course[1]) for course in courses], flush=True)
        ], color="primary text-primary")
        return element
