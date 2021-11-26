from django.http import HttpResponse


def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://img2.baidu.com/it/u=1984058067,3319783488&fm=26&fmt=auto" />'
    return HttpResponse(line1 + line2)
