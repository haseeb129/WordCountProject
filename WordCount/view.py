from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'homepage.html', {'yoyo': "this is simple text"})


def count(request):
    Orininaltext = request.GET['text']
    text = Orininaltext.split()
    wordcount = {}
    for word in text:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    print(wordcount)

    wordcount1 = sorted(
        wordcount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {"wordcount": wordcount1, "Orininaltext": Orininaltext})
