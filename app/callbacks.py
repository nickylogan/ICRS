from dash import Dash
from dash.dependencies import Output, Input, State
from model.predictor import Predictor
import json


def register_callbacks(app: Dash):
    '''Register callbacks for the given app argument'''

    predictor = Predictor()

    @app.callback(
        Output("concentration-data", "children"),
        [Input("submit-button", "n_clicks")],
        [State("input-calculus1", "value"),
         State("input-discrete_math", "value"),
         State("input-intro_to_it", "value"),
         State("input-prolog", "value"),
         State("input-calculus2", "value"),
         State("input-data_structure", "value"),
         State("input-java", "value"),
         State("input-mis", "value"),
         State("input-stats", "value"),
         State("input-algo_analysis", "value"),
         State("input-computer_arch", "value"),
         State("input-database", "value"),
         State("input-linear_algebra", "value"),
         State("input-oop", "value")]
    )
    def process_data(n_clicks: int,
                     calculus1: int, discrete_math: int, intro_to_it: int, prolog: int,
                     calculus2: int, data_structure: int, java: int, mis: int, stats: int,
                     algo_analysis: int, computer_arch: int, database: int, linear_algebra: int, oop: int,
                     ) -> str:
        '''Process the data from the provided arguments'''

        scores = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0]
        result = predictor.predict(
            calculus1=scores[calculus1],
            discrete_math=scores[discrete_math],
            intro_to_it=scores[intro_to_it],
            prolog=scores[prolog],
            calculus2=scores[calculus2],
            data_structure=scores[data_structure],
            java=scores[java],
            mis=scores[mis],
            stats=scores[stats],
            algo_analysis=scores[algo_analysis],
            computer_arch=scores[computer_arch],
            database=scores[database],
            linear_algebra=scores[linear_algebra],
            oop=scores[oop],
        )
        return json.dumps(result)

    """
    This callback is used for rendering the GUI element of the IIM concentration
    """
    @app.callback(
        [
            Output("iim-recommended", "children"),
            Output("iim-performance", "children"),
            Output("iim-header", "color"),
            Output("iim-header", "className"),
        ],
        [
            Input("concentration-data", "children")
        ]
    )
    def render_iim_title(data: str) -> (str, str, str, str):
        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "iim"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["iim"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor

    """
    This callback is used for rendering the GUI element of the MI concentration
    """
    @app.callback(
        [
            Output("mi-recommended", "children"),
            Output("mi-performance", "children"),
            Output("mi-header", "color"),
            Output("mi-header", "className"),
        ],
        [
            Input("concentration-data", "children")
        ]
    )
    def render_mi_title(data: str) -> (str, str, str, str):
        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "mi"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["mi"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor

    """
    This callback is used for rendering the GUI element of the SE concentration
    """
    @app.callback(
        [
            Output("se-recommended", "children"),
            Output("se-performance", "children"),
            Output("se-header", "color"),
            Output("se-header", "className"),
        ],
        [
            Input("concentration-data", "children")
        ]
    )
    def render_se_title(data: str) -> (str, str, str, str):
        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "se"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["se"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor
