from enum import Enum

class FlightStatus(Enum):
    ON_TIME = "ON_TIME"
    DELAYED ="DELAYED"
    CANCELLED ="CANCELLED"
    