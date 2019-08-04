## Prerrequisites
Must have defined a custom environment. (You can see more about in generic scripting - virtualenv.txt).
Once inside the environment we need to install the python libraries listed in requirements.txt
To do this cd to the directory where requirements.txt is located and run from shell:

```shell
(venv) your:route/youruser$ pip install -r requirements.txt
```
Once installed you are ready to run app

## How to run this app

To run this app (flask_app.py) load the appropiate environment with workon and..
once activate the environmet (venv in this case) execute from shell:

```shell
(venv) your:route/youruser$ flask run
 * Serving Flask app "yourapp"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Then to access to the output app you must to charge in your browser the url 127.0.0.1:5000 or localhost:5000
