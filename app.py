"""Local entry scaffold. Product analysis is implemented in a separate service."""
import json
from http import HTTPStatus
from wsgiref.simple_server import make_server

from backend import BackendNotIncluded, UnconfiguredBackend

backend = UnconfiguredBackend()
MAX_REQUEST_BYTES = 16 * 1024

def respond(start_response, status, payload):
    body = json.dumps(payload).encode('utf-8')
    start_response(f'{status.value} {status.phrase}', [
        ('Content-Type', 'application/json; charset=utf-8'),
        ('Content-Length', str(len(body))),
    ])
    return [body]

def application(environ, start_response):
    method = environ.get('REQUEST_METHOD', 'GET')
    path = environ.get('PATH_INFO', '/')
    if method == 'GET' and path == '/healthz':
        return respond(start_response, HTTPStatus.OK, {
            'service': 'Creative Pulse submission scaffold',
            'status': 'ok', 'scope': 'scaffold_only',
        })
    if method == 'POST' and path == '/api/reviews':
        try:
            length = int(environ.get('CONTENT_LENGTH') or 0)
            if not 0 <= length <= MAX_REQUEST_BYTES:
                return respond(start_response, HTTPStatus.REQUEST_ENTITY_TOO_LARGE,
                               {'error': 'request_too_large'})
            payload = json.loads(environ['wsgi.input'].read(length))
            asset = payload.get('asset_reference') if isinstance(payload, dict) else None
            if not isinstance(asset, str) or not asset.strip():
                raise ValueError('asset_reference is required')
        except (ValueError, UnicodeDecodeError, KeyError):
            return respond(start_response, HTTPStatus.BAD_REQUEST,
                           {'error': 'invalid_request'})
        try:
            review_id = backend.submit(asset.strip())
        except BackendNotIncluded:
            return respond(start_response, HTTPStatus.NOT_IMPLEMENTED, {
                'error': 'backend_not_included',
                'message': 'Use the deployed evaluation prototype for product functionality.',
            })
        return respond(start_response, HTTPStatus.ACCEPTED,
                       {'review_id': review_id, 'status': 'accepted'})
    return respond(start_response, HTTPStatus.NOT_FOUND, {'error': 'not_found'})

if __name__ == '__main__':
    print('Creative Pulse scaffold: http://127.0.0.1:8080/healthz')
    print('The product analysis service is not included or connected.')
    with make_server('127.0.0.1', 8080, application) as server:
        server.serve_forever()
