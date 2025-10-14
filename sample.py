import logging
from pydantic import BaseModel, Field
from typing import Optional

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

class NewsTranscript(BaseModel):
    title: str
    id:int = Field(g=0)
    content: str = Field(..., description="The main content of the news transcript")

print(add(2, 3))
news = NewsTranscript(id=1, title="Sample News", content="This is a sample news content.")
print(news)