from datetime import datetime

import pytz
from aiohttp import web
from loguru import logger

moscow_tz = pytz.timezone("Europe/Moscow")


async def get_time(request: web.Request) -> web.Response:
    """Return current time in Moscow timezone."""
    t = datetime.now(moscow_tz).strftime("%H:%M:%S")
    logger.info("Time request")
    with open(request.app["config"].visits_file, "a") as f:
        f.write(f"get_time: {t}\n")
    return web.Response(text=f"Time in Moscow is {t}")


async def get_visits(request: web.Request) -> web.Response:
    """Return total visits and all visits."""
    logger.info("Visits request")
    with open(request.app["config"].visits_file, "r") as f:
        visits = f.read()
    line_count = len(visits.splitlines())
    return web.Response(text=f"Total visits: {line_count}\n\n{visits}")


async def get_health(_: web.Request) -> web.Response:
    """Return health status."""
    logger.info("Health request")
    return web.Response(text="Up")
