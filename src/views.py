from fastapi import APIRouter

from schemas import User

router = APIRouter()


@router.get('/{user_id}')
def get_user(user_id: int):
    return {
        'user': user_id,
    }


@router.post('/user')
def post_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email,
    }
