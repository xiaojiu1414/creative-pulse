"""Observable HTTP behavior of the public entry scaffold; no product internals."""
import io
import json
import unittest

from app import MAX_REQUEST_BYTES, application

def request(method, path, body=b'', content_length=None):
    observed = {}
    def start_response(status, headers):
        observed['status'] = int(status.split()[0])
        observed['headers'] = dict(headers)
    response = b''.join(application({
        'REQUEST_METHOD': method, 'PATH_INFO': path,
        'CONTENT_LENGTH': str(len(body) if content_length is None else content_length),
        'wsgi.input': io.BytesIO(body),
    }, start_response))
    return observed['status'], json.loads(response)

class ScaffoldTests(unittest.TestCase):
    def test_health_explicitly_identifies_scaffold(self):
        status, body = request('GET', '/healthz')
        self.assertEqual(status, 200)
        self.assertEqual(body['scope'], 'scaffold_only')
    def test_unconfigured_backend_returns_no_analytical_result(self):
        status, body = request('POST', '/api/reviews',
                               json.dumps({'asset_reference': 'demo-asset'}).encode())
        self.assertEqual(status, 501)
        self.assertEqual(body['error'], 'backend_not_included')
        self.assertEqual(set(body), {'error', 'message'})
    def test_malformed_body_is_rejected(self):
        self.assertEqual(request('POST', '/api/reviews', b'{')[0], 400)
    def test_unknown_route(self):
        self.assertEqual(request('GET', '/unavailable')[0], 404)
    def test_oversized_request(self):
        self.assertEqual(request('POST', '/api/reviews',
                                 content_length=MAX_REQUEST_BYTES + 1)[0], 413)

if __name__ == '__main__':
    unittest.main()
