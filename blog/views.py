from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("""<html>
    <title>Сайт Алексея Куличевского</title>
    <h1>Алексей Куличевский</h1>
    </html>""")
