from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from database import get_db
from domain.answer import answer_schema, answer_crud
from domain.question import question_crud

from sqlalchemy.orm import Session

router = APIRouter(
    prefix = '/api/answer'
)

@router.post('/create/{question_id}', status_code = status.HTTP_204_NO_CONTENT)
def create_answer(question_id : int, 
                  _answer_create: answer_schema.AnswerCreate,
                  db : Session = Depends(get_db)) :
    
    question = question_crud.get_question(db, question_id = question_id)
    if not question :
        raise HTTPException(status_code = 404, detail = 'Question not found')

    answer_crud.create_answer(db = db,
                              question = question,
                              answer_create = _answer_create
                              )
    
