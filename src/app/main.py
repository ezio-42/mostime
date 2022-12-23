import os

from aiohttp import web

from app.config import Config, default_config
from app.handlers import get_health, get_time, get_visits


def make_app(config: Config):
    """Create aiohttp application."""
    os.makedirs(os.path.split(config.visits_file)[0], exist_ok=True)
    app = web.Application()
    app["config"] = config
    app.add_routes([web.get("/", get_time)])
    app.add_routes([web.get("/visits", get_visits)])
    app.add_routes([web.get("/health", get_health)])
    return app


def main():
    """Run application."""
    config = default_config
    app = make_app(config)
    web.run_app(app, port=config.port)


if __name__ == "__main__":
    main()
