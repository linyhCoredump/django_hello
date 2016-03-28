from django.shortcuts import render
from django.http import HttpResponse
from subject.models import Subject, Page
from subject.forms import SubjectForm

# Create your views here.


def index(request):
    subject_list = Subject.objects.order_by('name')[:5]
    context_dict = {'categories': subject_list}
    return render(request, 'subject/index.html', context_dict)


def about(request):
    about_dict = {'aboutmessage': 'bazinga'}
    return render(request, 'subject/about.html', about_dict)


def showsubject(request, Subject_name_slug):
    context_dict = {}
    try:
        subjectitem = Subject.objects.get(slug=Subject_name_slug)
        context_dict['subject_name'] = subjectitem.name
        pages = Page.objects.filter(Subject=subjectitem)
        context_dict['pages'] = pages
        context_dict['subject'] = subjectitem
    except Subject.DoesNotExist:
        print "Subject none"
    return render(request, 'subject/subject.html', context_dict)


def add_subject(request):
    form = []
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            form = SubjectForm()
    return render(request, 'subject/add_subject.html', {'form': form})
