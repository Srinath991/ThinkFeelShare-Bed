from sqlmodel import SQLModel, Field
from typing import Optional
from uuid import UUID, uuid4

class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, description="Unique identifier for the user")
    username: str = Field(index=True, min_length=3, max_length=50, description="Username of the user")
    email: str = Field(index=True, description="Email address of the user")

    
class Chat(SQLModel,table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, description="Unique identifier for the chat")
    message: str = Field(description="Message content of the chat")
    timestamp: Optional[str] = Field(default=None, description="Timestamp of when the chat was created")
