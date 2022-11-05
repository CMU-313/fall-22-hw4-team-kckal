from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the predict route it is great!'


def test_predict_route_success():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&activities=true&higher_edu=true&studytime=4&G1=20&G2=20'

    response = client.get(url)
    print(response.status_code)
    assert response.status_code == 200
    #assert response.json['message'] == 'Applicant is likely to succeed.'

def test_predict_route_success_unlikely():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=3&activities=false&higher_edu=false&studytime=1&G1=0&G2=0'

    response = client.get(url)
    assert response.status_code == 200
    # assert response.json['message'] == 'Applicant is not likely to succeed.'


def test_predict_route_no_parameters():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_missing_failures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?activities=0&higher_edu=0&studytime=1&G1=10&G2=10'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_missing_activities():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&higher_edu=0&studytime=1&G1=10&G2=10'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_missing_higher():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=4&activities=0&studytime=1&G1=10&G2=10'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_missing_studytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=4&activities=0&higher_edu=0&G1=10&G2=10'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_missing_G1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=4&activities=0&higher_edu=0&studytime=1&G2=10'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_missing_G2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=4&activities=0&higher_edu=0&studytime=1&G1=10'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'Missing one or more parameters required.'


def test_predict_route_invalid_failures():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=5&activities=1&higher_edu=1&studytime=&G1=20&G2=20'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'One or more invalid parameters.'


def test_predict_route_invalid_activities():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&activities=2&higher_edu=1&studytime=4&G1=20&G2=20'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'One or more invalid parameters.'


def test_predict_route_invalid_higher():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&activities=1&higher_edu=4&studytime=2&G1=20&G2=20'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'One or more invalid parameters.'

def test_predict_route_invalid_studytime():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&activities=1&higher_edu=0&studytime=27&G1=20&G2=20'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'One or more invalid parameters.'


def test_predict_route_invalid_G1():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&activities=1&higher_edu=0&studytime=1&G1=43&G2=20'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'One or more invalid parameters.'


def test_predict_route_invalid_G2():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/predict?failures=1&activities=1&higher_edu=0&studytime=1&G1=20&G2=26'

    response = client.get(url)
    assert response.status_code == 400
    assert response.json['message'] == 'One or more invalid parameters.'

