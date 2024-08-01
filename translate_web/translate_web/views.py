from django.shortcuts import render
from googletrans import Translator

def main(request):
    if request.method == 'POST':
        lang = request.POST.get('lang', None)
        txt = request.POST.get('txt',None)

        translator = Translator()
        tr = translator.translate(txt, dest=lang)

        return render(request,'main/main.html',{'result':tr.text})

    return render(request,'main/main.html')
