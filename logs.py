import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.ERROR,
    format=
    "%(asctime)s - %(levelname)s - %(message)s [%(filename)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("logs.txt", maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Create a separate logger for downloaded links
download_logger = logging.getLogger("downloads")
download_handler = logging.FileHandler("downloaded_links.txt")
download_handler.setLevel(logging.INFO)
download_logger.addHandler(download_handler)

logging = logging.getLogger()
