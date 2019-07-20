from dash.dependencies import Output, Input, State
from predictor import predict
import json

"""
register_callbacks registers callbacks for a dash app
"""
def register_callbacks(app):
    @app.callback(
        Output("concentration-data", "children"),
        [Input("submit-button", "n_clicks")],
        [State("input-INF0131", "value"),
         State("input-INF0221", "value"),
         State("input-INF0381", "value"),
         State("input-INF0011", "value"),
         State("input-INF0141", "value"),
         State("input-INF0621", "value"),
         State("input-INF0301", "value"),
         State("input-INF0531", "value"),
         State("input-INF0601", "value"),
         State("input-INF0031", "value"),
         State("input-INF0271", "value"),
         State("input-INF0521", "value"),
         State("input-INF0021", "value"),
         State("input-INF0291", "value")]
    )
    def process_data(n_clicks,
                     INF0131,
                     INF0221,
                     INF0381,
                     INF0011,
                     INF0141,
                     INF0621,
                     INF0301,
                     INF0531,
                     INF0601,
                     INF0031,
                     INF0271,
                     INF0521,
                     INF0021,
                     INF0291):
        scores = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0]
        data = {
            "INF0131": [scores[INF0131]],
            "INF0221": [scores[INF0221]],
            "INF0381": [scores[INF0381]],
            "INF0011": [scores[INF0011]],
            "INF0141": [scores[INF0141]],
            "INF0621": [scores[INF0621]],
            "INF0301": [scores[INF0301]],
            "INF0531": [scores[INF0531]],
            "INF0601": [scores[INF0601]],
            "INF0031": [scores[INF0031]],
            "INF0271": [scores[INF0271]],
            "INF0521": [scores[INF0521]],
            "INF0021": [scores[INF0021]],
            "INF0291": [scores[INF0291]],
        }
        result = predict(data)
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
    def render_iim_title(data):
        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "iim"
        recommended_str = "Recommended" if recommended else ""
        performance = data["iim"]
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
    def render_mi_title(data):
        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "mi"
        recommended_str = "Recommended" if recommended else ""
        performance = data["mi"]
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
    def render_se_title(data):
        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "se"
        recommended_str = "Recommended" if recommended else ""
        performance = data["se"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor
