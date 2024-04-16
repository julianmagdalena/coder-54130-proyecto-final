from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>hola!!! esta es mi vista<h1/>")

def list_view(request):
    contexto_dic = {
        'games': [
            "final_fantasy - rpg",
            "god_of_war - action",
            "fifa24 - sport"
        ]
    }

return render(request, "list.html", contecto_dict)