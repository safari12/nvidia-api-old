import unittest
import unittest.mock as mock
import json

from app import create_app
from app.gpu import handlers
from app.gpu.exceptions import GPUError


class GPUListTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('development')
        self.client = self.app.test_client

    @mock.patch('app.gpu.handlers.commands')
    def test_handler(self, mock_commands):
        mock_commands.query.return_value = """
        39, Geforce GTX 1070, 103.38, 151.00, 1544, 8114, 100, 59
        """

        gpu_list = handlers.get_gpu_list()

        self.assertEqual(len(gpu_list), 1)
        self.assertDictEqual(gpu_list[0].serialize(), {
            'name': 'Geforce GTX 1070',
            'fan_speed': 39,
            'watt': {
                'usage': 103.38,
                'cap': 151.00
            },
            'memory': {
                'used': 1544,
                'max': 8114
            },
            'temperature': 59,
            'volatile': 100
        })

    @mock.patch('app.gpu.handlers.commands')
    def test_handler_error(self, mock_commands):
        try:
            mock_commands.query.return_value = "lkajsdflkjasdlk;jfl;kasdkf"
            handlers.get_gpu_list()
        except GPUError:
            pass

    @mock.patch('app.gpu.handlers.commands')
    def test_api_error(self, mock_commands):
        mock_commands.query.return_value = "lkajsdflkjasdlk;jfl;kasdkf"
        res = self.client().get('/gpu')

        self.assertEqual(res.status_code, 500)
        self.assertTrue(json.loads(res.data)['message'])

    @mock.patch('app.gpu.handlers.commands')
    def test_api(self, mock_commands):
        mock_commands.query.return_value = """
            39, Geforce GTX 1070, 103.38, 151.00, 1544, 8114, 100, 59
            """
        res = self.client().get('/gpu')

        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(json.loads(res.data)[0], {
            'name': 'Geforce GTX 1070',
            'fan_speed': 39,
            'watt': {
                'usage': 103.38,
                'cap': 151.00
            },
            'memory': {
                'used': 1544,
                'max': 8114
            },
            'temperature': 59,
            'volatile': 100
        })
