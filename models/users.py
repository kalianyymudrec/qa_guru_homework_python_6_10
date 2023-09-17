import datetime
from dataclasses import dataclass
from typing import Tuple, Optional


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    subjects: Tuple[Optional[str], ...]
    date_of_birth: datetime.date
    hobbies: Tuple[Optional[str], ...]
    picture: str
    current_address: str
    state: str
    city: str
