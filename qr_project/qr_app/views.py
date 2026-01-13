from django.shortcuts import render, get_object_or_404
from .models import VisitingCard
import qrcode, base64, uuid
from io import BytesIO


def home(request):
    qr_code = None

    if request.method == "POST":
        uid = str(uuid.uuid4())[:8]   # unique ID

        card = VisitingCard.objects.create(
            uid=uid,
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            company=request.POST.get("company"),
            address=request.POST.get("address"),
        )

        dynamic_url = f"http://127.0.0.1:8000/card/{uid}/"

        qr = qrcode.make(dynamic_url)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        qr_code = base64.b64encode(buffer.getvalue()).decode()

    return render(request, "qr_app/home.html", {"qr_code": qr_code})


def view_card(request, uid):
    card = get_object_or_404(VisitingCard, uid=uid)
    return render(request, "qr_app/card.html", {"card": card})
