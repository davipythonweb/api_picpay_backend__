from django.shortcuts import render

import stripe
from django.conf import settings
import stripe.error
import stripe.webhook

from .models import Product, Order
from django.http import JsonResponse, HttpResponse

from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET_KEY



def home(request):
    product = Product.objects.get(id = 1)
    return render(request, 'home.html', {'product': product, 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})



def create_checkout_session(request, id):
    product = Product.objects.get(id = id)
    YOUR_DOMAIN = "http://127.0.0.1:8000/"
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'currency': 'BRL',
                    'unit_amount' : int(product.price),
                    'product_data': {
                        'name': product.name
                    }
                },
                'quantity': 1,
            },
        ],
        payment_method_types=[
            'card',
            'boleto',
        ],
        metadata={
            'id_product': product.id,
            'name': 'Eliote Alderson',
            'address': 'Rua Placa mae core i9'
        },
        mode='payment',
        success_url=YOUR_DOMAIN + 'sucesso',
        cancel_url=YOUR_DOMAIN + 'erro',
    )
    return JsonResponse({'id': checkout_session.id})


def sucesso(request):
    return HttpResponse('Sucesso!')


def erro(request):
    return HttpResponse('Erro!')


"""
comando para ouvir o webhook do stripe[roda no terminal dentro da pasta com arquivo stripe]
./stripe listen --forward-to localhost:8000/stripe_webhook
"""


# SEM segurança de verificação do token webhook 
# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body

#     # comment: For now, you only nedd print out the webhook payload so you can see
#     # comment: the structure.
#     print(payload)

#     return HttpResponse(status=200)



# com segurança de verificação do token webhook 
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # invalid signature
        return HttpResponse(status=400)
    
    # quando a compra está aprovada(pode ser feito varias coisas, como enviar um email de aprovação da compra.)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        print(session)

        # pegando os dados para salvar em banco
        order = Order(product_id=session['metadata']['id_product'],
                     email=session['customer_details']['email'],
                     name = session['metadata']['name'],
                     address = session['metadata']['address'],
                     status= event['type'],)
        order.save()
        
        print('Aprovada')

    return HttpResponse(status=200)

# sequencia das mensagens de aprovação do webhook stripe via terminal

"""
charge.updated
charged.succeeded
payment.intent.succeeded
payment.intent.created
checkout.session.completed

"""



"""
testando o webhook com request curl via terminal linux ( para firjar uma aprovação de pagamento.)

curl -X POST \
-H "Content-Type: application/json"\
--data '{type: "checkout.session.completed"}' \
-is http://localhost:8000/stripe_webhook

"""



# rota se fosse em produção
"""

def create_checkout_session(request, id):
    product = Product.objects.get(id = id)
    if settings.DEBUG:
        YOUR_DOMAIN = "http://127.0.0.1:8000/"
    else:
        NOVO_DOMAIN = 'http://seudominio.com.br'

    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                'price_data':{
                    'currency': 'BRL',
                    'unit_amount' : int(product.price),
                    'product_data': {
                        'name': product.name
                    }
                },
                'quantity': 1,
            },
        ],
        payment_method_types=[
            'card',
            'boleto',
        ],
        metadata={
            'id_product': product.id,
        },
        mode='payment',
        success_url=YOUR_DOMAIN + '/sucesso',
        cancel_url=YOUR_DOMAIN + '/erro',
    )
    return JsonResponse({'id': checkout_session.id})

    
"""