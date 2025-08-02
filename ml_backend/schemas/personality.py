from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated

class ModelInput(BaseModel):
    Time_spent_Alone: Annotated[int, Field(..., gt=0)]
    Stage_fear: bool
    Social_event_attendance: int
    Going_outside: Annotated[int, Field(..., gt=0)]
    Drained_after_socializing: bool
    Friends_circle_size: int
    Post_frequency: int

class Personality(str, Enum):
    INTROVERT = 'INTROVERT'
    EXTROVERT = 'EXTROVERT'

class ModelOutput(BaseModel):
    personality: Personality
    confidence: float
    probabilities: list[float]