from ninja import Router

payments_router = Router()

@payments_router.post('/')
def transaction(request):
    return {1: 1}