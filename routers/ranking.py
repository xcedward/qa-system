from fastapi import APIRouter,Depends, status
from sqlmodel import Session
from sql import models
from sql.database import get_session
import schemas
from sqlalchemy import desc, asc, func

router = APIRouter()

@router.get("/real_time_rank", response_model=schemas.CurrentResponse,
             status_code=status.HTTP_200_OK,
             responses={406:{"description":"Not Acceptable."}},
             summary="实时排名",
             description="""当前活跃期排行榜""")
def real_time_rank(issue_number: str,session: Session = Depends(get_session)):
    try:
        query = session.exec(models.User.user_id, models.User.name, models.User.party_branch, models.Score.score, models.Score.time_used).join(
            models.Score, models.User.user_id == models.Score.user_id).filter(models.Score.issue_number == issue_number).order_by(
            desc(models.Score.score), asc(models.Score.time_used))
        rank_list = query.all()
        result = []
        for rank in rank_list:
            rank_dict = {
                '姓名': rank[1],
                '支部': rank[2],
                '成绩': rank[3],
                '用时': rank[4]
            }
            result.append(rank_dict)
        return {"status": "success", "rank": result}
    except Exception as e:
        return {"status": "error", "message": f"获取实时排名失败: {str(e)}"}


@router.get("/historical_rank", response_model=schemas.RankResponse,
             status_code=status.HTTP_200_OK,
             responses={406:{"description":"Not Acceptable."}},
             summary="总排行榜",
             description="""历史排名查询""")
def historical_rank(session: Session = Depends(get_session)):
    try:
        query = session.exec(models.User.user_id, models.User.name, models.User.party_branch, func.sum(models.Score.score).label(
            "total_score"), func.avg(models.Score.time_used).label("average_time")).join(
            models.Score, models.User.user_id == models.Score.user_id).group_by(models.User.user_id).order_by(
            desc("total_score"), asc("average_time"))
        rank_list = query.all()
        result = []
        for rank in rank_list:
            rank_dict = {
                '姓名': rank[1],
                '支部': rank[2],
                '总正确数': rank[3],
                '平均用时': rank[4]
            }
            result.append(rank_dict)
        return {"status": "success", "rank": result}
    except Exception as e:
        return {"status": "error", "message": f"获取历史排名失败: {str(e)}"}
