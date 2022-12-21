import os
from aiohttp import web
from handlers import get_time, get_visits, health
from config import Config, default_config


def make_app(config: Config):
    os.makedirs(os.path.split(config.visits_file)[0], exist_ok=True)
    app = web.Application()
    app["config"] = config
    app.add_routes([web.get("/", get_time)])
    app.add_routes([web.get("/visits", get_visits)])
    app.add_routes([web.get("/health", health)])
    return app


def main():
    config = default_config
    app = make_app(config)
    web.run_app(app, port=config.port)


if __name__ == "__main__":
    main()
