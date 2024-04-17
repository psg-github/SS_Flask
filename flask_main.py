import dash_bootstrap_components as dbc
import dash
import dash_html_components as html
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

server = flask.Flask(__name__)

@server.route("/")
def home():
    return "Hello, Flask!"
@server.route("/trxn_risk/")
def trxn_rr():
    return "7.2"

app = dash.Dash(server=server, routes_pathname_prefix="/dash/")

app.layout = html.Div("This is the Dash app.")

if __name__ == "__main__":
    app.run_server(debug=True)