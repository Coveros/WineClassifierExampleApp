from seleniumbase import BaseCase
from unittest.mock import patch

import pytest

from wine import app, model


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setitem(app.config, 'TESTING', True)
    with app.test_client() as test_client:
        yield test_client


class TestPredictionAPI:
    @pytest.mark.parametrize('class_id,wine_name', [
        (0, 'Barolo'),
        (1, 'Grignolino'),
        (2, 'Barbera'),
    ])
    def test_predict_returns_wine_name(self, client, class_id, wine_name):
        features = {
            'alcohol': '14', 'malic_acid': '1', 'ash': '10',
            'alcalinity_of_ash': '15', 'magnesium': '125',
            'total_phenols': '2', 'flavanoids': '2',
            'nonflavanoid_phenols': '0.5', 'proanthocyanins': '1',
            'color_intensity': '7', 'hue': '0.7',
            'od280_od315_of_diluted_wines': '2', 'proline': '1000',
        }
        with patch.object(model, 'predict', return_value=[class_id]) as predict:
            response = client.post('/predict', data=features)

        assert response.status_code == 200
        assert f'The predicted wine type is {wine_name}' in response.get_data(as_text=True)
        assert b'variety #' not in response.data
        predict.assert_called_once_with([list(features.values())])

class ClassifierTests(BaseCase):
    def login(self):
        # open login page
        self.open("http://127.0.0.1:5000/login")
        self.type("#username", "jefferyepayne")
        self.type("#password", "TestTest")
        self.click('button[type="submit"]')
        self.wait_for_text("Logged in successfully!")
        self.assert_text("Logged in successfully!")

    def logout(self):
        self.click_link("Logout")
        self.assert_element("#username")

    def test_predict_variety_0(self):

        self.login()

        # open classifier page
        self.open("http://127.0.0.1:5000/predict")
        
        # enter values into form
        self.type("#alcohol", "14")
        self.type("#malic_acid", "1")
        self.type("#ash", "10")
        self.type("#alcalinity_of_ash", "15")
        self.type("#magnesium", "125")
        self.type("#total_phenols", "2")
        self.type("#flavanoids", "2")
        self.type("#nonflavanoid_phenols", "0.5")
        self.type("#proanthocyanins", "1")
        self.type("#color_intensity", "7")
        self.type("#hue", "0.7")
        self.type("#od280_od315_of_diluted_wines", "2")
        self.type("#proline", "1000")

        # click predict button
        self.click("button[type=submit]")

        # assert prediction
        self.assert_text("The predicted wine type is Barolo")

        self.logout()