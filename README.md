# UPH Informatics Concentration Recommender System

## Background

Most universities have what is named as an academic concentration, which is a branch of an academic major. This includes the Informatics Major in Universitas Pelita Harapan. Choosing the right academic concentration is very important, as it determines the main focus for students to learn on for more than half of their university lifetime.

Unfortunately, there is little information available to help students decide their concentration. Considering the fact that students also strive for academic success, this application tries to give an insight to help them choose the right concentration. Given a list of course scores for the first four semesters, the student will be given the predicted rate of success for each Informatics major concentration.

## Getting Started

To run this app, make sure you have the mentioned prerequisites and follow the installation steps below.

### Prerequisites

* [Python3](https://www.python.org/downloads/)
* [pip](https://pypi.org/project/pip/)

### Installing

Before installing any libraries, it is better to have a clean slate Python environment. To do so, we can make a Python virtual environment by running:

```sh
python3 -m venv myvenv
```

The command above will create a directory called `myvenv` in the project root. To activate the virtual environment, run the following command:

```sh
# For Windows users
$ .\myvenv\Scripts\activate.bat

# For UNIX or MacOS
$ source myvenv/bin/activate
```

Your terminal prompt will be prepended by the name of the virtual environment. For instance, activating `myvenv` would cause the terminal to look like this:

```sh
$ source myvenv/bin/activate
(myvenv) $ _
```

> **Make sure the virtual environment is already activated**

There are several libraries used for this project, all of them are listed in `requirements.txt`. To install all of them, simply run the following command from the project directory.

```sh
(myvenv) $ pip install -r requirements.txt
```

***IF***, however, you want to install the libraries manually, here are the links to the crucial ones:

* [dash](https://dash.plot.ly/)
* [dash-bootstrap-components](https://github.com/facultyai/dash-bootstrap-components)
* [pandas](https://pandas.pydata.org/)
* [numpy](https://www.numpy.org/)
* [scikit-learn](https://scikit-learn.org/)
* [Jupyter](https://jupyter.org/)

### Running the app

> **Make sure the virtual environment is still activated**

The app was built using [Dash](https://dash.plot.ly/). To run the app locally, run the following command from the `app` directory:

```sh
(myvenv) $ python app.py
Running on http://127.0.0.1:8050/
Debugger PIN: XXX-XXX-XXX
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
Running on http://127.0.0.1:8050/
Debugger PIN: XXX-XXX-XXX
...
```

You can open the app on the browser by accessing `http://127.0.0.1:8050/`.

## How does it work

![diagram](img/diagram.svg)

The diagram shows several major steps in the whole development process, each of which are going to be explained in the following subsections.

### Data acquisition

// TODO: add more

### Data cleansing

The raw data *needs* to be transformed, so it can be trained. The full process can be read [here](data/preprocess.ipynb).

### Model training + test

### Frontend development using Dash

The app lives inside the `app` directory. As you can see, there are four main python files:

* `app.py`: The entry point of the web application
* `callbacks.py`: Dash callbacks to register, so that data can flow between components
* `components.py`: UI components
* `layout.py`: Contains the main layout for the whole app

### Integration with Dash

### Visualize and predict data

## Authors

* **Laurentius Dominick Logan** - [nickylogan](https://github.com/nickylogan)
* **Nadya Felim Bachtiar** - [Ao-Re](https://github.com/ao-re)
* **Barjuan Davis Penthalion** - [cokpsz](https://github.com/cokpsz)
