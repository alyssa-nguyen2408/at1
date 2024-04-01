from django.core import serializers
from django.shortcuts import render
from .models import Sentence
import random
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/index.html', {'questions_json': questions_json})


def home(request):
    return render(request, 'eduprod/home.html')

def chemistry(request):
    sentences = Sentence.objects.all()
    sentence_data = []
    for sentence in sentences:
        words = sentence.content.split()
        gap_index = random.randint(0, len(words) - 1)
        gap_word = words[gap_index]
        words[gap_index] = '________'
        sentence_with_gap = ' '.join(words)
        sentence_data.append({
            'sentence': sentence_with_gap,
            'answer': gap_word
        })
    sentence_count = len(sentence_data)  # Pass the length of sentence_data to the template
    context = {
        'sentence_data': sentence_data,
        'sentence_count': sentence_count
    }
    return render(request, 'eduprod/chemistry.html', context)





def english(request):
    return render(request, 'eduprod/english.html')