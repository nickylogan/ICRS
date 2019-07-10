import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


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
            value=0
        )
        return element
