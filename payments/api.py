from ninja import Router

payments_router = Router()

@payments_router.post('/')
def transaction(request):
    return {1: 1}


#  tempo do video 59:14