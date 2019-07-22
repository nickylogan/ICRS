# The Web App

The web application is build using [dash](https://dash.plot.ly), a Python framework based on [Flask](http://flask.pocoo.org/), [plotly](https://plot.ly/), and [ReactJS](https://reactjs.org/). The Dash framework provides an abstraction towards HTML components and supercharges it with other functionalities. Dash also provides other components useful for data visualization and since the Python language is used, it is very much suitable for data science-related tasks.

An additional library is used on top of the existing dash components, called [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components). That way, it is easier to style elements using the [Bootstrap](https://getbootstrap.com/) framework.

## Codebase structure

The entry point of the web application is on `main.py`. Other components live inside the `app` directory, containing four main python files:

| File            | Description                                |
| --------------- | ------------------------------------------ |
| `layout.py`     | Contains the main layout for the whole app |
| `components.py` | UI components                              |
| `callbacks.py`  | Dash callbacks                             |
| `routes.py`     | Flask routes                               |

### `main.py`

As you may already know, the web application's entry point is from `main.py`. Let's examine it a bit more.

The code snippet below shows import statements in the beginning of the script. The first three allows us to use `dash` and `dash-bootstrap-components`. The last three are from our own scripts&mdash;we'll explain them later.

```python
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

from app.layout import Root
from app.callbacks import register_callbacks
from app.routes import register_routes
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
register_callbacks(app)
```

Additional Flask routes are also registered. Similar to `register_callbacks`, `register_routes()` is a function made to register routes for the app. Further explanation can be read [later](#routespy).

```python
register_routes(app)
```

Finally, the app's main entry point is contained in the following code snippet.

```python
# This is the main entry point of the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_hot_reload=True)
```

### `layout.py`

The `Root()` function returns main layout of the web app. Here is a snippet of the whole file.

```python
import dash_bootstrap_components as dbc
import dash_html_components as html
from .components import Header, Tabs, InputContainer, RecommendationContainer

# The main layout of the app
def Root():
    element = dbc.Container([
        Header.render(),
        Tabs.render(),
        InputContainer.render(),
        html.Hr(),
        RecommendationContainer.render(),
    ], className="pb-5 mb-5")
    return element
```

As you can see, the app's layout simply uses already made components declared in another file, which we will discuss in the next section.

### `components.py`

Having a separate file for dash components is great, as it separates the view component from the internal logic. There are *nine* components in total, each following the same structure:

```python
class Component:
  @staticmethod
  def render():
    element = # some html component
    return element
```

If you want to use the component, you can just simply call `Component.render()`.

There are a total of 15 components, each rendering a different part of the app layout.

### `callbacks.py`

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

Below is an illustration of the full callback graph:

![callback](/img/diagrams/callback.svg)

### `routes.py`

This part contains Flask routes for file download. To ease explanation, below is the full copy of the file

```python
from flask import send_file


def register_routes(app):
    @app.server.route('/static/sample.csv')
    def download_sample():
        return send_file('app/static/sample.csv', mimetype='text/csv', attachment_filename='sample.csv', as_attachment=True)
```

A function called `register_routes` is declared, taking an `app` as an argument. It works in a similar way to `register_callbacks`. The `app` parameter is used as a function decorator for `download_sample`. The decorator `@app.server.route('/static/sample.csv')` part tells the Flask server behind the web app, that the succeeding function is the handle for route `/static/sample.csv`.

Inside the `download_sample` function, we see a `send_file` invocation. Since we want to provide a way for the user to download a template file, the server should respond with a pre-existing file for the request to the specified route.

## File upload and download

We added a feature for batch processing, that is, a user can upload a `.csv` file rather than inputting the scores one by one. The results are then shown in a table and can be downloaded into a `.csv` file. Luckily, dash has components supporting file upload along with some hacks to allow dynamic download.

### Uploading

Out of the box, dash provides a component called `Upload` to allow file upload. Below is a snippet of its usage in our app:

```python
dcc.Upload(
    id='upload-data',
    children=...,   # Truncated for conciseness
    style=...,      # Truncated for conciseness
    className="py-5 text-center",
    className_active="bg-secondary",
    className_reject="bg-danger text-white",
    accept='.csv',
    max_size=2000000,
)
```

It has parameters `accept` and `max_size`. We want `.csv` files to be uploaded. Hence, the `accept` parameter should be set as `.csv`. Next, since we don't want the file to be too large, we limit the size to 2MB by setting `max_size` to `2000000`. This element also has `id` `upload-data`, which can be passed into a callback to be further processed. Other than that, the rest of the parameters are for stylistic purposes.

### Downloading

Dynamic file download uses a hack explained [here](https://community.plot.ly/t/download-raw-data/4700/8). Basically, it uses an `<a>` element, with its `href` pointing to a data url. By clicking on it, the browser will automatically download the file encoded to the `href`. Here's an example of the rendered element:

```html
<a
    download="results.csv"
    href="data:text/csv;charset=utf-8,..."
    target="_blank"
    class="btn btn-primary text-white mt-3"
>
    Download results
</a>
```
