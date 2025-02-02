#self created file

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    nav='''
        <h1>Home</h1>
            <ul type=square>
            <li><a href="about">About</a>
            <li><a href="removepunc">remove punc</a>
            <li><a href="capfirst">cap first</a>
            <li><a href="newlineremove">newline remove</a>
            <li><a href="spaceremove">space remove</a>
            </ul>
        '''
    return HttpResponse(nav)

def about(request):
    nav1='''
        <a href="https://tint.techtron.net/"> My college</a><br>
        <a href="http://127.0.0.1:8000/">Go back to home</a>

    '''
    return HttpResponse(nav1)

def analyse(request):
    djtext=request.POST.get('text','default')
    removepuncs=request.POST.get('removepunc','off')
    extraspaceremover=request.POST.get('spaceremove','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    charcount=request.POST.get('charcount','off')
    print(djtext)
    print(removepuncs)
    if removepuncs=='on':
        analysed=''
        puncs='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in puncs:
                analysed=analysed+char

        para={'purpose':'removed punctuations','analysed':analysed}
        #return render(request, 'analysed.html', para)
        djtext=analysed
    if(extraspaceremover == "on"):
        analysed =""
        for index, char in enumerate (djtext):
            if djtext[index] == " " and djtext [index+1] == " ":
                pass
            else:
                analysed = analysed+char

        para={'purpose':'space removed','analysed':analysed}
        #return render(request, 'analysed.html', para)
        djtext=analysed
    if(fullcaps=="on"):
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()

        para = {'purpose':'Removed Punctuations', 'analysed':analysed}
       # return render(request, 'analysed.html', para)
        djtext=analysed
    if newlineremover=='on':
        analysed=""
        for char in djtext:
            if char!="\n" and char!='\r' :
                analysed=analysed+char

        para={'purpose':'Removed new line', 'analysed':analysed}
        #return render(request, 'analysed.html', para)
        djtext=analysed
    if charcount=='on':
        analysed=""
        for char in djtext:
            analysed=len(djtext)

        para={'purpose':'Removed new line', 'analysed':analysed}
        #return render(request, 'analysed.html', para)
        djtext=analysed
    if(removepuncs!='on' and extraspaceremover!='on' and charcount!='on' and newlineremover!='on' and fullcaps!='on'):
        return HttpResponse('<h1>ERROR! Please tick the box</h1>')

    return render(request, 'analysed.html', para)

def capfirst(request):
    return HttpResponse('''Cap first"<br>
                        <a href="http://127.0.0.1:8000/">Go back to home</a>''')

def newlineremove(request):
    return HttpResponse('''newline remove<br>
                        <a href="http://127.0.0.1:8000/">Go back to home</a>''')

def removepunc(request):
    return HttpResponse('remove punc')

def spaceremove(request):
    return HttpResponse('remove space')

def charcount(request):
    return HttpResponse('char count')
'''
def spaceremove(request):
    djtext_space=request.GET.get('text','default')
    removespace=request.GET.get('spaceremove','off')
    print(djtext_space)
    print(removespace)
    if removespace=="on":
        analysedspace=""
        space=" "
        for char in djtext_space:
            if char not in space:
                analysedspace=analysedspace+char

        para_space={'purposespace':'removed space','analysedspace':analysedspace}
        return render(request, 'spaceremove.html', para_space)
    else:
        return HttpResponse('<h1>ERROR! Please tick the box</h1>')
'''



def temp(request):
    return render(request, 'index.html')