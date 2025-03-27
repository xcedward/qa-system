from fastapi import FastAPI
from sql.database import create_db_and_tables
from routers import question, ranking,user
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name":"用户",
        "description":"统一认证登录、更改党支部、查询个人成绩"
            
    },
    {
        "name":"题目管理",
        "description":"获取题目、答题提交"
            
    },
    {
        "name":"排行榜",
        "description":"实时排名、历史排名查询"
    }
]

app = FastAPI(title="党建问答", version = "0.0.1",open_tags=tags_metadata)

app.include_router(ranking.router, tags=["排行榜"], prefix="/api")
app.include_router(question.router, tags=["题目管理"], prefix="/api")
app.include_router(user.router, tags=["用户管理"], prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




if __name__ == '__main__':
    create_db_and_tables()
    import uvicorn
    uvicorn.run('main:app', port = 8000, reload=True)