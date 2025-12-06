from django.shortcuts import render

def portfolio(request):
    partners = [
        {
            "name": "Mark Gabrielle Zosimo",
            "description": "I am a web developer specializing in Django and front-end technologies.",
            "skills": ["Python", "Django", "HTML", "CSS"]
        },
        {
            "name": "John Derick Querubin",
            "description": "I focus on UI/UX design and front-end development using JavaScript and React.",
            "skills": ["JavaScript", "Hiking", "Playing Pog"]
        }
    ]
    
    objective = "Our objective is to create clean, user-friendly web applications and improve our coding skills through real-world projects."

    return render(request, "portfolio.html", {"partners": partners, "objective": objective})
