import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from .models import Memento

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def index(request):
    mementos = Memento.objects.all()
    return render(
        request,
        'index.html',
        context={
            "mementos": mementos,
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )

def memento(request, id):
    memento_id = get_object_or_404(Memento, id=id)
    mementos = Memento.objects.all()

    context = {
        'memento_id': memento_id,
        'mementos': mementos
    }

    return render(request, 'mementos.html', context)

def addMemento(request):
    return render(request, 'add-memento.html')

def profile(request):
    return render(request, 'profile.html')

