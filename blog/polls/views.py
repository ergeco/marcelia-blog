from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from .models import Post, DonationPeople, HistoryNews


def index(request):

    # Сделать, чтоб история была только ласт, а дальше буду думать
    # как сделать по красоте

    # В общем истории еще продумать

    hist = HistoryNews.objects.all().order_by('-date')[:1]


    donations = DonationPeople.objects.all()
    posts = Post.objects.all()
    posts = Post.objects.order_by('-post_date')
    return render(request, 'polls/index.html', {'history': hist, 'donation_people': donations,
                  'some_posts': posts})


def create_post(request):
    return render(request, 'polls/create_post.html')

def creating(request):
    if request.method == "POST":

        post = Post()
        post.title  = request.POST.get("title")
        post.text = request.POST.get("text")
        post.theme = request.POST.get("theme")
        post.hash_tags = request.POST.get("hash_tags")

        post.save()


        return HttpResponseRedirect('/burkoff_blog')
    else:
        return HttpResponse('Error in posting. Just watch your code and do something!!!  \^-^/')

def delete_post(request, id):
    try:
        post_id = id
        post = Post.objects.filter(id=post_id)
        post.delete()
        return HttpResponseRedirect('/burkoff_blog')
    except:
        return HttpResponse('Error in deleting post. Just watch your code and do something!!!  \^-^/')


def just_redact(request, id):
    post_id = id
    post = Post.objects.filter(id=post_id)
    return render(request, 'polls/just_redact.html', {'posts': post})

def redacting(request, id):
    post_id = id
    if request.method == 'POST':
        post = Post()
        post.title = request.POST.get("title")
        post.text = request.POST.get("text")
        post.theme = request.POST.get("theme")
        post.hash_tags = request.POST.get("hash_tags")
        post.post_date = request.POST.get("post_date")

        event_red = Post.objects.filter(id=post_id).update(title=post.title,
                                                            text=post.text,
                                                            theme=post.theme,
                                                            hash_tags=post.hash_tags,
                                                            post_date=post.post_date)
        return HttpResponseRedirect("/burkoff_blog")
    else:
        return HttpResponse('Error in redacting post. Just watch your code and do something!!!  \^-^/')


def my_progress(request):
    post = Post.objects.filter(hash_tags='прогресс')
    return render(request, 'polls/my_progress.html', {'posts': post})

def contacts(request):
    return render(request, 'polls/contacts.html')

def support(request):
    return render(request, 'polls/support.html')

def team(request):
    return render(request, 'polls/team.html')

def create_history(request):
    return render(request, 'polls/create_history.html')

def crhis(request):
    if request.method == "POST":

        hist = HistoryNews()
        hist.text = request.POST.get("text")
        hist.save()


        return HttpResponseRedirect('/burkoff_blog')
    else:
        return HttpResponse('Error in posting. Just watch your code and do something!!!  \^-^/')

