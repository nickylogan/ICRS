import base64
import io
import json
import urllib

import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output, State

from model.predictor import Predictor

from .components import (
    BatchInputContainer, BatchTable, ManualInputContainer,
    ManualOutputContainer)


def register_callbacks(app: Dash):
    '''Register callbacks for the given app argument'''

    predictor = Predictor()

    @app.callback(
        Output("manual-output", "children"),
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
        values = [
            calculus1, discrete_math, intro_to_it, prolog,
            calculus2, data_structure, java, mis, stats,
            algo_analysis, computer_arch, database, linear_algebra, oop
        ]

        if not n_clicks:
            return json.dumps({})

        if any(x == -1 for x in values):
            result = {
                'error': 'All course scores must be non-empty'
            }
            return json.dumps(result)

        scores = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0]
        data = predictor.predict(
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
        return json.dumps({'data': data})

    @app.callback(
        [
            Output('concentration-data', 'children'),
            Output('manual-welcome', 'className'),
            Output('manual-error', 'className'),
            Output('manual-error', 'children'),
            Output('manual-deck', 'className'),
        ],
        [Input('manual-output', 'children')]
    )
    def render_output(data: str) -> (str, str, str, str, str):
        payload: dict = json.loads(data)
        error: str = payload.get('error', None)
        data: dict = payload.get('data', None)

        if error:
            return "", "d-none", "d-block", error, "d-none"

        if not data:
            return "", "d-block", "d-none", "", "d-none"

        return json.dumps(data), "d-none", "d-none", "", "d-block"

    @app.callback(
        [
            Output("imdd-recommended", "children"),
            Output("imdd-performance", "children"),
            Output("imdd-header", "color"),
            Output("imdd-header", "className"),
        ],
        [
            Input("concentration-data", "children")
        ]
    )
    def render_imdd_title(data: str) -> (str, str, str, str):
        """
        render_imdd_title is used for rendering the GUI element of the imdd concentration
        """
        if not data:
            return "", "", "", ""

        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "imdd"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["imdd"]
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
    def render_mi_title(data: str) -> (str, str, str, str):
        """
        render_mi_title is used for rendering the GUI element of the MI concentration
        """
        if not data:
            return "", "", "", ""

        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "mi"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["mi"]
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
    def render_se_title(data: str) -> (str, str, str, str):
        """
        render_se_title is used for rendering the GUI element of the SE concentration
        """
        if not data:
            return "", "", "", ""

        data = json.loads(data)
        recommended = sorted(data.items(), key=lambda x: x[1], reverse=True)[
            0][0] == "se"
        recommended_str = "Recommended" if recommended else ""
        performance = "%.2f %%" % data["se"]
        color = "primary" if recommended else "secondary"
        textColor = "text-white" if recommended else "text-primary"
        return recommended_str, performance, color, textColor

    @app.callback(
        [
            Output("manual-input-container", "className"),
            Output("manual-output-container", "className"),
            Output("batch-input-container", "className"),
            Output("batch-output-container", "className"),
        ],
        [Input("tabs", "active_tab")]
    )
    def render_tab_content(tab: str):
        if tab == "playground":
            return "d-block", "d-block", "d-none", "d-none"
        if tab == "batch":
            return "d-none", "d-none", "d-block", "d-block"

        return "d-none", "d-none", "d-none", "d-none"

    @app.callback(
        Output("batch-preview", "children"),
        [Input('upload-data', 'contents')],
        [State('upload-data', 'filename'),
         State('upload-data', 'last_modified')]
    )
    def preview_data(contents, filename, last_modified):
        if not filename:
            return html.P("The preview of your data will appear here")

        try:
            decoded = base64.b64decode(contents.split("base64,")[1])
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            df = df.head()
            return [
                html.Small("Only the first 5 rows are shown"),
                BatchTable.render(df),
                dbc.Button("Process data",
                            outline=True, color="primary", id="process-button", className="mt-3 mb-5")
            ]
        except Exception as e:
            return dbc.Alert("There is an error in uploading your data", color="danger")


    @app.callback(
        Output("batch-results-container", "children"),
        [Input("process-button", "n_clicks")],
        [State("upload-data", "contents")],
    )
    def process_batch(n_clicks, contents):
        if not n_clicks or n_clicks == 0:
            return html.P("Predicted results for your data will appear here")
        
        try:
            decoded = base64.b64decode(contents.split("base64,")[1])
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            result_df = predictor.predict_batch(df)
            csv_string = result_df.to_csv(index=False, encoding='utf-8')
            csv_string = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_string)
            return [
                html.A(
                    "Download results",
                    href=csv_string,
                    download="results.csv",
                    target="_blank",
                    className="btn btn-primary text-white mt-3",
                ),
                BatchTable.render(result_df),
            ]
        except Exception as e:
            return dbc.Alert("There is an error in processing your data: " + str(e), color="danger")
