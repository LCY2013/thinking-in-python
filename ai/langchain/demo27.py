from langchain.output_parsers.enum import EnumOutputParser
from enum import Enum


class Colors(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


parser = EnumOutputParser(enum=Colors)
