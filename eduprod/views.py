from django.core import serializers
from django.shortcuts import render, redirect
from .models import Sentence
import random
from .models import Question
from django.contrib.auth.decorators import login_required
from .models import Essay
from .forms import EssayForm

@login_required
def submit_essay(request):
    if request.method == 'POST':
        form = EssayForm(request.POST)
        if form.is_valid():
            essay = form.save(commit=False)
            essay.user = request.user
            essay.save()
            return redirect('eduprod:essay_list')
    else:
        form = EssayForm()
    return render(request, 'eduprod/submit_essay.html', {'form': form})

@login_required
def essay_list(request):
    essays = Essay.objects.filter(user=request.user)
    return render(request, 'eduprod/essay_list.html', {'essays': essays})

@login_required
def home(request):
    return render(request, 'eduprod/home.html')

#This is the code where the program will use a sentence, and randomly select a spot to generate a gap, which is the answer.
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