import dash_html_components as html
import dash_bootstrap_components as dbc
from .ScoreInput import ScoreInput

class CourseInput:
    @staticmethod
    def render(id, name):
        element = dbc.ListGroupItem([
            name,
            ScoreInput.render(id),
        ], className="d-flex justify-content-between align-items-center")
        return element