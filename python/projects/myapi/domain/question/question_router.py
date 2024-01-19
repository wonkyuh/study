from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)

# 의존성 주입 전
# 함수 실행 시 명시적으로 세션을 열고 닫고 있는 걸 볼 수 있다.
# 하지만 이런 식으로 만들어두게 되면 조회 시 오류가 났을 경우
# 세션이 정상적으로 닫히질 않아 메모리 누수가 발생할 가능성이 크다.
# @router.get("/list")
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     db.close()
#     return _question_list

# with문을 활용한 의존성 주입
# @router.get("/list")
# def question_list():
#     with get_db() as db:
#         _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
#     return _question_list

# Depends, Session 모듈을 통해 의존성 주입을 한 케이스
# 의존성 투입하기 제일 간단한 방법
# with문이 아닌 Depends 모듈을 사용하게 되면
# contextmanager가 2중으로 중복되기 때문에 database.py에 있는 부분을 주석처리 함.
@router.get("/list", response_model=question_schema.QuestionList)
def question_list(db: Session = Depends(get_db),
                  page: int = 0, size: int = 10):
    total, _question_list = question_crud.get_question_list(
        db, skip=page*size, limit=size)
    return {
        'total': total,
        'question_list': _question_list
    }

@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question

@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)