"""
Main module
"""
import logging
from os import environ as env
from app.app import app
import datetime
import pytz
import coloredlogs

logging.getLogger('werkzeug').disabled = True
logging.getLogger('urllib3').setLevel(logging.WARNING)
my_timezone = pytz.timezone('America/Sao_Paulo')

logger = logging.getLogger()


def customTime(*args):
    utc_dt = datetime.datetime.now(pytz.utc)
    my_tz = utc_dt.astimezone(my_timezone)
    return my_tz.timetuple()


logging.Formatter.converter = customTime

coloredlogs.install(level='DEBUG', logger=logger)
logger.handlers = []

console_handler = logging.StreamHandler()
formatter = coloredlogs.ColoredFormatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)


def main():
    """Main function"""
    port = int(env.get('PORT', 443))
    app.run(host='0.0.0.0', port=port, debug=False, load_dotenv=True,
            ssl_context=('./cert/certificate.cer', './cert/key.key'))


if __name__ == '__main__':
    main()
