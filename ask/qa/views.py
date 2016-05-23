from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.contrib.auth.models import User


def test(request, *args, **kwargs):
    return HttpResponse('OK')

def test1(request, *args, **kwargs):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseNotFound('<h1>Invalid usernamepass</h1>')
    else:
        return render(request,'login.html')

# @login_required
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            print url
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'askform.html', {
        'form': form,
        })

@require_POST
# @login_required
def answer(request):
    form = AskForm(request.POST)
    form._user = request.user
    if form.is_valid():
        question = form.save()
        url = question.get_url()
        return HttpResponseRedirect(url)
    else:
        return HttpResponseNotFound()

def question_detail(request, id):
    question = get_object_or_404(Question, id = id)
    form = AnswerForm()
    return render(request, 'question_details.html', {
    	'question': question,
        'form':form
    	})

def questions_new(request):
    questions = Question.objects.new()
    page = request.GET.get('page',1)
    paginator = Paginator(questions, 10)
    # paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    # except EmptyPage:
    except:
        page = paginator.page(paginator.num_pages)
    # import pdb
    # pdb.set_trace()
    return render(request, 'questions_list.html', {
    	'questions': page.object_list,
        'paginator': paginator,
        'page': page
    	})

def questions_popular(request):
    questions = Question.objects.popular()
    page = request.GET.get('page',1)
    paginator = Paginator(questions, 10)
    # paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    # except EmptyPage:
    except:
        page = paginator.page(paginator.num_pages)
    return render(request, 'questions_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
        })