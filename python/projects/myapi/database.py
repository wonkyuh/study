import contextlib

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

# 커넥션 풀 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터 접속에 필요한 클래스
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터 모델을 구성할 때 사용되는 클래스
Base = declarative_base()



# contextlib의 contextmanager 모듈을 사용하면
# with get_db() as db: 처럼 with문 활용이 가능하다.
# Depends을 사용하게 되면 중복 사용이 되기 때문에 주석처리함
# @contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()