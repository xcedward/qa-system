from sqlmodel import SQLModel,Field

class User(SQLModel, table=True):
    user_id: str = Field(default=None, primary_key=True)
    name: str
    party_branch: str

class Question(SQLModel, table=True):
    question_id: str = Field(default=None, primary_key=True)
    issue_number: str
    question_content: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: str
    uesr_answer:str

class Score(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user_id: str
    issue_number: str
    score: int
    time_used: float