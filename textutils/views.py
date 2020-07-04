# I have created this file - yukesh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

   return render(request, 'index.html')

def about(request):
    return HttpResponse('''<h1>Most visited sites are:</h1> <br> <ul><li><a href= "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Facebook</a></li> <li>Code with Harry</li>
    <li>Youtube</li> <li>Corona Virus Update</li> <li>Machine Learning</li>
    
    </ul>''')


def analyze(request):
    djtext= request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    uppercase= request.POST.get('uppercase', 'off') 
    newlinerem= request.POST.get('newlinerem', 'off')
    extraspace= request.POST.get('extraspace', 'off')
    charcount= request.POST.get('charcount', 'off')
    # yo agadi ko charcount ra removepunc index file ko checkbox tag sanga milnu parxa
    
    if removepunc == 'on':
        punctuation= '''/[-[\]{()}*+?.,\^'"$|#\]/,;"\$&"'''
        analyzed= ""
        for char in djtext:
            if char not in punctuation:
                analyzed= analyzed + char
        params= { 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    elif uppercase == 'on':
       analyzed= djtext.upper()
       param1= {'analyzed_text': analyzed}
       return render(request, 'analyze.html', param1)

    elif newlinerem== 'on':
        analyzed= ''
        for chari in djtext:
            if chari != '\n' and chari!= '\r':
                analyzed= analyzed + chari

        param2= {'analyzed_text': analyzed}
        return render(request, 'analyze.html', param2)

    elif extraspace == 'on':
        analyzed= ''
        for index, char in enumerate(djtext):
            if(djtext[index]== " " and djtext[index+1]== " "):
                pass
            else:
                analyzed= analyzed + char
            
        param3= {'analyzed_text': analyzed}
        return render(request, 'analyze.html', param3)
    
    elif charcount == 'on':
        analyzed= len(djtext)

        param4= {'analyzed_text': analyzed}
        return render(request, 'analyze.html', param4)


    else:
        return HttpResponse('Error')
# def charcount(request):
#     return HttpResponse('''<h1>Char Count </h1><br><button type="button">Go Back</button> ''')

# def spaceremove(request):
#     return HttpResponse('''<h1>Space Remover</h1> <br> <button type="button">Go Back</button>''')

# def removepunc(request):
#     djtext= request.GET.get('text', 'default')
#     print(djtext)
#     return HttpResponse('''<h1>Remove Punctuation..</h1><br> <button type="button">Go Back</button> ''')

# def capfirst(request):
#     return HttpResponse('''<h1>Capitalize firat letter..</h1><br> <button type="button">Go Back</button>''')

# def newlineremove(request):
#     return HttpResponse('''<h1>Space ...</h1><br> <button type="button">Go Back</button> ''')

