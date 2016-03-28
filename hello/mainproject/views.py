from django.shortcuts import render

# Create your views here.


def mainpage(request):
    main_text={'mainmessage': 'choose a link...'}
    return render(request, 'mainpage/mainpage.html', main_text)
