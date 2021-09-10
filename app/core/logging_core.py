import logging
import ecs_logging

# StdlibFormatter helps creating logs in json format
# A custom class here, helps us with easy addition of more fields according to our use-case
# Feel free to use StdlibFormatter directly, incase you don't want to add more fields
class APMLogFormatter(ecs_logging.StdlibFormatter):
    def format(self, record):
        result = super().format(record=record)
        return result

def initialize():
    log = logging.getLogger('werkzeug')
    log.disabled = True     # disables default logging done by flask for each api call

    log_formatter = APMLogFormatter(
        exclude_fields=[
            "event", # this causes troubles with logging on apm service
        ]
    )
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(log_formatter) # you can skip this step if you don't want logs in json format

    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s]: %(process)s %(levelname)s %(message)s', # gets overridden if log_handler has a custom formatter set
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[log_handler])
