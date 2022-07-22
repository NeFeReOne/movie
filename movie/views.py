from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth import login
from .forms import SignupForm

from .models import Check, Data, History
from .forms import TimeForm, FeelForm, HobbyForm, InterestForm


def index(request):
    params = {
        'title':'映画を検索しよう！',
        'msg':'時間ができたから映画を見たいけど、何があったかな？',
        'msg1':'いつもと違う映画に出会う・・・',
        'msg2':'今日の気分に合った映画を探してみましょう。',
        'msg3':'　　　　', 
        'goto':'time',
    }

    return render(request, 'movie/index.html', params)

def time(request):
    params = {
        'title':'time',
        'msg':'映画を見れる時間はどれぐらい？',
        'goto':'feel',
    }
    return render(request, 'movie/index.html', params)

def feel(request):
    params = {
        'title':'feel',
        'msg':'今日の気分を選んでね！',
        'goto':'hobby',
    }
    return render(request, 'movie/index.html', params)

def hobby(request):
    params = {
        'title':'hobby',
        'msg':'気になる趣味を選んでね',
        'goto':'interest',
    }
    return render(request, 'movie/index.html', params)

def interest(request):
    params = {
        'title':'interest',
        'msg':'気になる言葉を下からチェックしてね',
        'goto':'result',
    }
    return render(request, 'movie/index.html', params)

def result(request):
    params = {
        'title':'今日のあなたへのお勧め映画！',
        'msg':'映画タイトル',
        'goto':'index',
    }
    return render(request, 'movie/result.html', params)