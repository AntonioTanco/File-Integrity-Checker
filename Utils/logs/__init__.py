import logging

logging.basicConfig(
    format="[F.I.M] - {asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO
)
logging.getLogger('apscheduler').setLevel(logging.DEBUG)