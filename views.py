from django.shortcuts import render
from django.conf import settings


def project(request):
    context=  {
        
        "about_project": settings.DATA["ABOUT_PROJECT"],
        "projects": settings.DATA['PROJECTS']
    }
    return render(request,'main/project.html',context)

def languages(request):
    context=  {
        "lang": settings.DATA['Languages']
    }
    return render(request,'main/languages.html',context) 
def education(request):
    context=  {
        "edc": settings.DATA['EDUCATION']
    } 
    return render(request,'main/education.html',context)
def achievements(request):
    context=  {
        "ac": settings.DATA['ACHIEVEMENTS']
        
    }
    return render(request,'main/achievements.html',context)         
def index(request):
    context =  {
        "name": settings.DATA['NAME'],
        "about": settings.DATA['ABOUT_ME']
    }
    return render(request,'main/index.html',context)    