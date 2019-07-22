# The Web App

The web application is build using [dash](https://dash.plot.ly), a Python framework based on [Flask](http://flask.pocoo.org/), [plotly](https://plot.ly/), and [ReactJS](https://reactjs.org/). The Dash framework provides an abstraction towards HTML components and supercharges it with other functionalities. Dash also provides other components useful for data visualization and since the Python language is used, it is very much suitable for data science-related tasks.

An additional library is used on top of the existing dash components, called [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components). That way, it is easier to style elements using the [Bootstrap](https://getbootstrap.com/) framework.

## Codebase structure

The entry point of the web application is on `main.py`. Other components live inside the `app` directory, containing three main python files:

| File            | Description                                |
| --------------- | ------------------------------------------ |
| `layout.py`     | Contains the main layout for the whole app |
| `components.py` | UI components                              |
| `callbacks.py`  | Dash callbacks                             |

## `main.py`

As you may already know, the web application's entry point is from `main.py`. Let's examine it a bit more.

The code snippet below shows import statements in the beginning of the script. The first three allows us to use `dash` and `dash-bootstrap-components`. The last two are from our own scripts&mdash;we'll explain them later.

```python
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from layout import Root
from callbacks import register_callbacks
```

Next is the app configuration, shown in the code snippet below. The app is created using the `dash.Dash()` function, along with two custom stylesheets. The first one uses the preexisting theme for `dash-bootstrap-components` and the other is our own custom styles. Using a bootstrap theme is extremely time-saving, as it avoids the need to exhaustively create our own style.

```python
# Initial app configuration
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX, './assets/custom.css'])
app.layout = html.Div(Root()) # <-- Root
app.title = 'Playground | ICRS'
app.config['suppress_callback_exceptions'] = True
```

As you can see above, we called the `Root()` function. In short, it returns the main layout of the app's look. This way, we can avoid cluttering the script file with HTML components.

Once the app is configured, data callbacks are registered. `register_callbacks()` is a custom-made function, so that callback registration can be separated into another file. We'll explain [later](#callbackspy) why it takes the `app` as an argument.

```python
# register_calbacks registers app callbacks, which are necessary
# for data flow between components
register_callbacks(app)
```

Finally, the app's main entry point is contained in the following code snippet.

```python
# This is the main entry point of the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
```

## `layout.py`

The `Root()` function returns main layout of the web app. Here is a snippet of the whole file.

```python
import dash_bootstrap_components as dbc
import dash_html_components as html
from components import Header, TermCardContainer, RecommendationContainer

# The main layout of the app
def Root():
    element = dbc.Container([
        Header.render(),
        html.Hr(),
        TermCardContainer.render(),
        html.Hr(),
        RecommendationContainer.render(),
    ], className="pb-5 mb-5")
    return element
```

The idea is to make the app's layout will look something like this:

```txt
+-------------------------+
| Header                  |
| ----------------------- |
| TermCardContainer       |
| ----------------------- |
| RecommendationContainer |
+-------------------------+
```

As you can see, the app's layout simply uses already made components declared in another file, which we will discuss in the next section.

## `components.py`

Having a separate file for dash components is great, as it separates the view component from the internal logic. There are *nine* components in total, each following the same structure:

```python
class Component:
  @staticmethod
  def render():
    element = # some html component
    return element
```

If you want to use the component, you can just simply call `Component.render()`.

## `callbacks.py`

This file contains all of the data flow logic for the web app. Dash callback functions are prepended with the `@app.callback` decorator. The `app` here must refer to the same `app` that was started in the main file. Hence, that's why the `register_callback` needs the `app` as a parameter.

We declare four callbacks, one for form submission and the other three for intermediate callbacks. We'll only how a dash callback works in general.

```python
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
def process_data(
    n_clicks: int,
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
```

The `@app.callback` decorator can take two or three arguments. The first one is the `Output` argument, specifying where the return value should be displayed. The second argument is the `Input` object, marking which elements should be listened for changes. The last and optional argument is the `State` object for keeping state. This is useful to simulate common form submission.
