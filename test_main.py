import unittest
from main import app
import json
import requests
from unittest.mock import patch

class TestMovieApp(unittest.TestCase):

    @patch('requests.get')
    def test_random_movie(self, mock_get):
        # Mock de la réponse de l'OMDb API
        mock_response = {
            'Title': 'Inception',
            'Plot': 'A mind-bending thriller about dream manipulation.',
            'Poster': 'https://via.placeholder.com/200x300'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Simuler la requête GET à /random_movie
        with app.test_client() as client:
            response = client.get('/random_movie')
            data = json.loads(response.data)
            
            # Vérification des données
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['title'], 'Inception')
            self.assertEqual(data['description'], 'A mind-bending thriller about dream manipulation.')
            self.assertEqual(data['image'], 'https://via.placeholder.com/200x300')

    @patch('requests.get')
    def test_random_image(self, mock_get):
        # Mock de la réponse de Picsum API pour l'image
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        with app.test_client() as client:
            response = client.get('/random_movie')
            data = json.loads(response.data)
            
            # Vérification de la présence d'une image valide
            self.assertIn('http', data['image'])
            self.assertTrue(data['image'].endswith('.jpg') or data['image'].endswith('.png'))
            

if __name__ == '__main__':
    unittest.main()
