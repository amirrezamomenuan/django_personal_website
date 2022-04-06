from django.shortcuts import render, HttpResponse

def home_page_view(request):
    if not request.user.is_authenticated:
        # this part should redirect user to authntication page (login , signup or ...) ------------------------------------------
        return HttpResponse("fuck you")
        
    return render(request, "home.html", {'username':request.user.first_name})