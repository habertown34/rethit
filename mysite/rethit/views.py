from django.shortcuts import render
from . import eth
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        if request.POST['content'] != '':
            eth.create_post(request.POST['content'])
    account, contract = eth.get_basic()
    balance = eth.get_balance()
    all_posts = eth.get_all_posts()
    num_posts = eth.get_number_of_posts()
    context = {
        'account': account,
        'contract': contract,
        'all': all_posts,
        'balance': balance,
        'num': num_posts
    }
    return render(request, 'rethit/index.html', context)

def upvote(request):
    post_id = int(request.GET['id'])
    votes = eth.upvote(post_id)
    return HttpResponse(votes)

def downvote(request):
    post_id = int(request.GET['id'])
    votes = eth.downvote(post_id)
    return HttpResponse(votes)