import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DecoratorLogger")
def loggerFn(func : callable) -> callable:
    def wrapper(*args, **kwargs):
        logger.info(f"{func.__name__} was called with args: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@loggerFn
def add(x, y):
    return x + y

print(add(2, 3))