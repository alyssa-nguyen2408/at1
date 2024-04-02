from django.core import serializers
from django.shortcuts import render
from .models import Sentence
import random
from .models import Question
from django.contrib.auth.decorators import login_required

@login_required


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
            'answer': gap_word,
            'is_red': sentence.is_red  # Add the color field to the context
        })
    sentence_count = len(sentence_data)  # Pass the length of sentence_data to the template
    context = {
        'sentence_data': sentence_data,
        'sentence_count': sentence_count
    }
    return render(request, 'eduprod/chemistry.html', context)


def index(request):
    # Fetch all sentences from the database
    sentences = Sentence.objects.all()

    # Get sentences with "red" color variable
    red_sentences = []
    for i, sentence in enumerate(sentences):
        choice = request.session.get(f"sentence{i}")
        if choice == 'red':
            red_sentences.append(sentence)

    return render(request, 'eduprod/index.html', {'red_sentences': red_sentences})

def tests(request):
    return render(request, 'eduprod/tests.html')

def engmod1(request):
    return render(request, 'eduprod/engmod1.html')



def english(request):
    return render(request, 'eduprod/english.html')