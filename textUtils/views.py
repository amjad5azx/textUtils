from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    # params={'Name':'Amjad','Country':'Afghnistan'}
    # return render(request,'index.html',params)
    # return HttpResponse('Index')

def analyze(request):

    #request.GET.get('','') yaha jitne bhi 'GET' jo capital may likha hua hay aur isko agr POST kr de gay to post ki request ban jae gi 
    dtext = request.POST.get('text', 'default')#print text else it will print default

    removepunc = request.POST.get('removepunc', 'off')#print text else it will print default
    fullcap=request.POST.get('fullcaps','off')
    newlinerem=request.POST.get('newlinerem','off')
    sapcerem=request.POST.get('spacerem','off')
    charcount=request.POST.get('charcount','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(fullcap=='on'):
        analyzed=dtext.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(newlinerem=='on'):
        analyzed=dtext.rstrip('\n')
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif(sapcerem=='on'):
        analyzed=dtext.replace(' ','')
        params={'purpose':'Space Remover','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(charcount=='on'):
        analyzed=len(dtext)
        params={'purpose':'Character Count','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    else:
        return HttpResponse('Error')

# def removePunc(request):
#     dtext = request.GET.get('text', 'default')#print text else it will print default
#     print(dtext)
#     return HttpResponse('remove punc<br><a href="/">Back</a>')

# def capfirst(request):
#     return HttpResponse('Capitalize First<br><a href="/">Back</a>')

# def newlineremove(request):
#     return HttpResponse('New Line First<br><a href="/">Back</a>')

# def spaceremove(request):
#     return HttpResponse('Space Remove<br><a href="/">Back</a>')

# def charcount(request):
    # return HttpResponse('Character Count<br><a href="/">Back</a>')