from ninja import Router
from .schemas import UserSchema
from .models import User
from django.contrib.auth.hashers import make_password

users_router = Router()

@users_router.post('/', response={200: dict})
def create_user(request, user: UserSchema):
    user = User(**user.dict())
    user.password = make_password(user.password)
    user.save()

    return {'ok': 'ok'}

# trabalhando com schemas no django-ninja, ou seja, padrão de dados que vamos receber na nossa requisiçao

# type_user é a variavel que armazena todos os dados enviados na requisição
 

#  tempo do video 30:26