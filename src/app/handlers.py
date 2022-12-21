from datetime import datetime

import pytz
from aiohttp import web
from loguru import logger

moscow_tz = pytz.timezone("Europe/Moscow")


async def log_visit(request: web.Request) -> web.Response:
    logger.info("Visits request")
    return web.Response(text="Visits")


async def get_time(request: web.Request) -> web.Response:
    t = datetime.now(moscow_tz).strftime("%H:%M:%S")
    logger.info("Time request")
    with open(request.app["config"].visits_file, "a") as f:
        f.write(f"get_time: {t}\n")
    return web.Response(text=f"Time in Moscow is {t}")


async def get_visits(request: web.Request) -> web.Response:
    logger.info("Visits request")
    with open(request.app["config"].visits_file, "r") as f:
        visits = f.read()
    line_count = len(visits.splitlines())
    return web.Response(text=f"Total visits: {line_count}\n\n{visits}")


async def health(_: web.Request) -> web.Response:
    logger.info("Health request")
    return web.Response(text="Up")
