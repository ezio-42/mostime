import pytest

from app.config import default_config
from app.main import make_app

pytest_plugins = "aiohttp.pytest_plugin"


@pytest.fixture
async def api_client(aiohttp_client):
    """Create test client for aiohttp application."""
    config = default_config
    app = make_app(config)
    client = await aiohttp_client(app)
    try:
        yield client
    finally:
        await client.close()
