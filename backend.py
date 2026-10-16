"""Upper-layer interface only. No product implementation is distributed here."""
from typing import Protocol

class ReviewBackend(Protocol):
    def submit(self, asset_reference: str) -> str:
        """Submit an asset reference and return an opaque review identifier."""
        ...

class BackendNotIncluded(RuntimeError):
    """The separate product service is not connected to this scaffold."""

class UnconfiguredBackend:
    def submit(self, asset_reference: str) -> str:
        raise BackendNotIncluded('Product service not included.')
