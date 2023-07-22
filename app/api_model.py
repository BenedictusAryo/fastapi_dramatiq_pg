""" 
API Request Model
"""
from pydantic import BaseModel, validator
import re

class SendEmail(BaseModel):
    """Request model for sending email"""
    email: str
    subject: str
    body: str

    # Validate email
    @validator('email')
    def email_must_be_valid(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError("Invalid email address")
        return v