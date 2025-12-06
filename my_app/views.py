from django.shortcuts import render

def portfolio(request):
    data = {
        "partners": [
            {
                "name": "HI! I'M MARK GABRIELLE ZOSIMO",
                "skills": ["Python", "Django", "HTML", "CSS"]
            },
            {
                "name": "HI! I'M JOHN DERICK QUERUBIN",
                "skills": ["JavaScript", "PLAYING POG", "HIKING"]
            }
        ]
    }
    return render(request, "portfolio.html", data)