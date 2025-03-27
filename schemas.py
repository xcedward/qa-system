from pydantic import BaseModel, Field


class PartyChange(BaseModel):
    
    user_id: str=Field(description="学号")
    name: str=Field(description="姓名")
    party_branch: str=Field(description="党支部")
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "user_id":"202200110001",
                "name":"张三",
                "party_branch":"x班党支部",
                }
        }
    }
    
class ChangeResponse(BaseModel):
    
    user_id: str=Field(description="学号")
    name: str=Field(description="姓名")
    party_branch: str=Field(description="党支部")
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "user_id":"202200110001",
                "name":"张三",
                "party_branch":"x班党支部",
                }
        }
    }

class ScroeInquiry(BaseModel):
    
    id: int=Field
    user_id: str=Field(description="学号")
    issue_number: str=Field(description="期数")
    score: int=Field(description="分数")
    time_used: float
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "id":"1",
                "user_id":"202200110001",
                "issue_number":"202503",
                "score":"97",
                "time_used":"90"
                }
        }
    }
    
class InquiryResponse(BaseModel):
    
    id: int=Field
    user_id: str=Field(description="学号")
    issue_number: str=Field(description="期数")
    score: int=Field(description="分数")
    time_used: float
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "id":"1",
                "user_id":"202200110001",
                "issue_number":"202503",
                "score":"97",
                "time_used":"90"
                }
        }
    }
    
class QuestionGet(BaseModel):
    
    question_id: str=Field(description="题号")
    issue_number: str=Field(description="期数")
    question_content: str=Field(description="题目")
    option_a: str=Field(description="选项a")
    option_b: str=Field(description="选项b")
    option_c: str=Field(description="选项c")
    option_d: str=Field(description="选项d")
    correct_answer: str=Field(description="正确答案")
    
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "question_id":"1",
                "issue_number":"202503",
                "question_content":"共产党成立于哪一年？",
                "option_a":"1920",
                "option_b":"1921",
                "option_b":"1923",
                "option_b":"1925",
                "correct_answer":"b"
                }
        }
    }
 
class QuestionResponse(BaseModel):
    
    question_id: str=Field(description="题号")
    issue_number: str=Field(description="期数")
    question_content: str=Field(description="题目")
    option_a: str=Field(description="选项a")
    option_b: str=Field(description="选项b")
    option_c: str=Field(description="选项c")
    option_d: str=Field(description="选项d")
    correct_answer: str=Field(description="正确答案")
    
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "question_id":"1",
                "issue_number":"202503",
                "question_content":"共产党成立于哪一年？",
                "option_a":"1920",
                "option_b":"1921",
                "option_b":"1923",
                "option_b":"1925",
                "correct_answer":"b"
                }
        }
    }

class AnswerQuestions(BaseModel):
    
    user_id: str=Field(description="学号")
    issue_number: str=Field(description="期数")
    question_id: str=Field(description="题号")
    user_answer:str=Field(description="用户答案")
    correct_answer:str=Field(description="正确答案")

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "user_id":"202200110001",
                "issue_number":"202503",
                "question_id":"7",
                "user_answer":"a",
                "correct_answer":"b"
                }
        }
    }    
    
class AnswerResponse(BaseModel):
    
    user_id: str=Field(description="学号")
    issue_number: str=Field(description="期数")
    question_id: str=Field(description="题号")
    user_answer:str=Field(description="用户答案")
    correct_answer:str=Field(description="正确答案")

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "user_id":"202200110001",
                "issue_number":"202503",
                "question_id":"7",
                "user_answer":"a",
                "correct_answer":"b"
                }
        }
    }    

class AnswerSubmit(BaseModel):
    
    user_id: str=Field(description="学号")
    issue_number: str=Field(description="期数")
    score: int=Field(description="分数")
    time_used: float

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "user_id":"202200110001",
                "issue_number":"202503",
                "score":"97",
                "time_used":"90"
                }
        }
    }    
    
class SubmitResponse(BaseModel):
    
    user_id: str=Field(description="学号")
    issue_number: str=Field(description="期数")
    score: int=Field(description="分数")
    time_used: float

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "user_id":"202200110001",
                "issue_number":"202503",
                "score":"97",
                "time_used":"90"
                }
        }
    }    


class CurrentRank(BaseModel):
    
    name: str=Field(description="姓名")
    party_branch: str=Field(description="党支部")
    score: int=Field(description="分数")
    time_used: float

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "name":"李四",
                "party_branch":"x班党支部",
                "score":"97",
                "time_used":"90"
                }
        }
    }    
    
class CurrentResponse(BaseModel):
    
    name: str=Field(description="姓名")
    party_branch: str=Field(description="党支部")
    score: int=Field(description="分数")
    time_used: float

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "name":"李四",
                "party_branch":"x班党支部",
                "score":"97",
                "time_used":"90"
                }
        }
    }    
    
class OverallRank(BaseModel):
    
    name: str=Field(description="姓名")
    party_branch: str=Field(description="党支部")
    total_score: int=Field(description="总分数")
    average_time: float

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "name":"李四",
                "party_branch":"x班党支部",
                "total_score":"180",
                "average_time":"90"
                }
        }
    }    

class RankResponse(BaseModel):
    
    name: str=Field(description="姓名")
    party_branch: str=Field(description="党支部")
    total_score: int=Field(description="总分数")
    average_time: float

    
    model_config = {
        "json_schema_extra":{
            "example":{
                "name":"李四",
                "party_branch":"x班党支部",
                "total_score":"180",
                "average_time":"90"
                }
        }
    }    