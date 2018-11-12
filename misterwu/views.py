from django.shortcuts import render


# Create your views here.
from idna import unicode


def home(request):
    import requests
    import json
    api_requets = requests.get('https://api.github.com/users?since=0')
    api = json.loads(api_requets.content)
    return render(request, 'home.html', {'api': api})

def user(request):
    if request.method == 'POST':
        user = request.POST['user']
        import requests
        import json
        api_requets = requests.get('https://api.github.com/users/'+user)
        username = json.loads(api_requets.content)
        return render(request, 'user.html', {'user':user, 'username':username})
    else:
        notfound = '请在搜索框输入你要搜索的内容...'
        return render(request, 'user.html', {'notfound':notfound})