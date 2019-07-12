from dash.dependencies import Output, Input, State
import json
import random


def register_callbacks(app):
    @app.callback(
        Output("concentration-data", "children"),
        [Input("submit-button", "n_clicks")]
    )
    def process_data(n_clicks):
        data = {
            "iim": random.randint(1, 100),
            "mi": random.randint(1, 100),
            "se": random.randint(1, 100),
        }
        return json.dumps(data)

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
