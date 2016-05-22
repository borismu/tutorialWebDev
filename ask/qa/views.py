from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator
from qa.models import Question, Answer
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def test1(request, *args, **kwargs):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def question_detail(request, id):
    question = get_object_or_404(Question, id = id)
    return render(request, 'question_details.html', {
    	'question': question,
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