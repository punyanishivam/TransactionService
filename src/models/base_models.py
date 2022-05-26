from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Optional


# class TransactionStatus(str, Enum):
#     initiated = "initiated"
#     processing = "processing"
#     completed = "completed"
#     failed = "failed"


# class TransactionType(str, Enum):
#     upi = "upi"
#     card = "card"
#     cod = "cod"


class Transaction(BaseModel):
    type: str
    parent_id: Optional[int]
    amount: float
