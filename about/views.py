from django.shortcuts import render
from about.models import About, DailyMessage

# Create your views here.
def AboutPage(request):

    about_obj = About.objects.all().first()
    daily_message = DailyMessage.objects.order_by("?").first()

    return render(
        request,
        "about/index.html",
        context={"daily_message": daily_message, "about_obj": about_obj},
    )
