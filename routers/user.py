from fastapi import APIRouter, Depends, Request
from fastapi import  status
from sqlmodel import Session
from sql import models
from sql.database import get_session
import schemas

router = APIRouter()




@router.post("/change_party_branch", response_model=schemas.ChangeResponse,
             status_code=status.HTTP_201_CREATED,
             responses={400:{"description":"Invalid request."}},
             summary="更改党支部",
             description="""更改党支部""")
def change_party_branch(request: Request, session: Session = Depends(get_session)):
    data = request.json()
    user_id = data.get('user_id')
    new_branch = data.get('new_branch')
    try:
        user = session.get(models.User, user_id)
        if user:
            user.party_branch = new_branch
            session.commit()
            session.refresh(user)
            return {"status": "success", "message": "党支部更改成功"}
        else:
            return {"status": "error", "message": "用户不存在"}
    except Exception as e:
            return {"status": "error", "message": f"党支部更改失败: {str(e)}"}


@router.get("/query_personal_score", response_model=schemas.InquiryResponse,
             status_code=status.HTTP_200_OK,
             responses={406:{"description":"Not Acceptable."}},
             summary="查询个人成绩",
             description="""查询个人成绩""")
def query_personal_score(user_id: str, session: Session = Depends(get_session)):
    try:
        scores = session.exec(models.Score).filter(models.Score.user_id == user_id).all()
        score_list = []
        for score in scores:
            score_dict = {
                '期号': score.issue_number,
                '成绩': score.score,
                '用时': score.time_used
            }
            score_list.append(score_dict)
        return {"status": "success", "scores": score_list}
    except Exception as e:
        return {"status": "error", "message": f"查询个人成绩失败: {str(e)}"}