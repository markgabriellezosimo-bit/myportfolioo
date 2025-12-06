from django.shortcuts import render

def portfolio(request):
    data = {
        "partners": [
            {
                "name": "MARK GABRIELLE ZOSIMO",
                "skills": ["Python", "Django", "HTML", "CSS"],
                "experience": "1 year as Web Developer"
            },
            {
                "name": "I'M JOHN DERICK QUERUBIN",
                "skills": ["JavaScript", "PLAYING POG", "HIKING"],
                 "experience": "2 years as Frontend Developer"
            }
        ]
    }
    return render(request, "portfolio.html", data)