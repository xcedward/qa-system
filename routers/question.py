import configparser
from datetime import time
from fastapi import APIRouter, Depends, Request,status
from sqlmodel import Session
import schemas
from sql.database import get_session
from sql.models import Question, Score

router = APIRouter()

@router.post("/publish_questions", response_model=schemas.QuestionResponse,
             status_code=status.HTTP_201_CREATED,
             responses={400:{"description":"Invalid request."}},
             summary="发布题目",
             description="""发布题目，发布时当前题目将自动变为往期""")
def publish_questions(request: Request, session: Session = Depends(get_session)):
    data = request.json()
    new_issue_number = data.get('issue_number')
    questions = data.get('questions')

    try:
        current_questions = session.exec(Question).all()
        for question in current_questions:
            question.issue_number = "past_" + question.issue_number
            session.add(question)

        for question_data in questions:
            new_question = Question(
                question_id=question_data.get('question_id'),
                issue_number=new_issue_number,
                question_content=question_data.get('question_content'),
                option_a=question_data.get('option_a'),
                option_b=question_data.get('option_b'),
                option_c=question_data.get('option_c'),
                option_d=question_data.get('option_d'),
                correct_answer=question_data.get('correct_answer')
            )
            session.add(new_question)

        session.commit()
        return {"status": "success", "message": "题目发布成功"}
    except Exception as e:
        return {"status": "error", "message": f"题目发布失败: {str(e)}"}

def get_current_issue_number():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config.get('issue', 'current_issue_number', fallback="202401")
   
    
@router.get("/get_questions", response_model=schemas.QuestionResponse,
             status_code=status.HTTP_200_OK,
             responses={406: {"description": "Not Acceptable."}},
             summary="获取题目",
             description="""获取当期或往期题目""")
def get_questions(is_current: bool = True, session: Session = Depends(get_session)):
    try:
        current_issue = get_current_issue_number()
        if is_current:
            questions = session.exec(Question).filter(Question.issue_number == current_issue).all()
        else:
            questions = session.exec(Question).filter(Question.issue_number != current_issue).all()

        question_list = []
        for question in questions:
            question_dict = {
                '题目ID': question.question_id,
                '题目内容': question.question_content,
                '选项A': question.option_a,
                '选项B': question.option_b,
                '选项C': question.option_c,
                '选项D': question.option_d,
                '正确答案': question.correct_answer
            }
            question_list.append(question_dict)
        return {"status": "success", "questions": question_list}
    except Exception as e:
        return {"status": "error", "message": f"获取题目失败: {str(e)}"}
    
    
@router.post("/answer_questions", response_model=schemas.AnswerResponse,
             status_code=status.HTTP_201_CREATED,
             responses={400: {"description": "Invalid request."}},
             summary="答题接口",
             description="""支持作答当期题目和补答往期题目""")
def answer_questions(request: Request, session: Session = Depends(get_session)):
    data = request.json()
    user_id = data.get('user_id')
    issue_number = data.get('issue_number')
    answers = data.get('answers')
    start_time = data.get('start_time')
    end_time = time.time()
    total_time = end_time - start_time

    correct_count = 0
    try:
        for answer in answers:
            question_id = answer['question_id']
            user_answer = answer['user_answer']
            question = session.get(Question, question_id)
            if question and user_answer == question.correct_answer:
                correct_count += 1

            answer_record = answer(
                user_id=user_id,
                question_id=question_id,
                user_answer=user_answer,
                issue_number=issue_number
            )
            session.add(answer_record)

        score = Score(user_id=user_id, issue_number=issue_number, score=correct_count, time_used=total_time)
        session.add(score)
        session.commit()
        session.refresh(score)
        return {"status": "success", "message": "答题提交成功", "成绩": correct_count, "用时": total_time}
    except Exception as e:
        return {"status": "error", "message": f"答题提交失败: {str(e)}"}

    
@router.post("/submit_answer", response_model=schemas.SubmitResponse,
             status_code=status.HTTP_201_CREATED,
             responses={400:{"description":"Invalid request."}},
             summary="答题提交",
             description="""答题提交""")
def submit_answer(request: Request, session: Session = Depends(get_session)):
    data = request.json()
    user_id = data.get('user_id')
    issue_number = data.get('issue_number')
    answers = data.get('answers')
    start_time = data.get('start_time')
    end_time = time.time()
    total_time = end_time - start_time
        
    correct_count = 0
    try:
        for answer in answers:
            question_id = answer['question_id']
            user_answer = answer['user_answer']
            question = session.get(Question, question_id)
            if question and user_answer == question.correct_answer:
                correct_count += 1

        score = Score(user_id=user_id, issue_number=issue_number, score=correct_count, time_used=total_time)
        session.add(score)
        session.commit()
        session.refresh(score)
        return {"status": "success", "message": "答题提交成功", "成绩": correct_count, "用时": total_time}
    except Exception as e:
        return {"status": "error", "message": f"答题提交失败: {str(e)}"}
