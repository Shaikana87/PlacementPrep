import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import QuizQuestion
# Create your views here.

def quiz_results(request):
    return render(request, 'quiz_results.html', {})

def quiz(request):
    if request.method == 'POST':
        questions = request.session.get('questions', [])
        score = 0
        for ques_id in questions:
            question = QuizQuestion.objects.get(id=ques_id)
            # print(request.POST)
            user_answer = request.POST.get(str(ques_id))
            if question.correct_ans == user_answer:
                score+=1
        messages.success(request, f'You scored {score} out of {len(questions)}')
        # return redirect('results/')
        return render(request, 'quiz_results.html', {'score':score})
    
    if request.user.is_authenticated:
        quiz_questions = QuizQuestion.objects.all()
        quiz_questions = random.sample(list(quiz_questions), k=5)
        request.session['questions'] = [q.id for q in quiz_questions]
        # for ques in quiz_questions:
        #     print(ques.correct_ans)
        return render(request, 'quiz.html', {'i':1, 'questions':quiz_questions}) 
    
    return  redirect('login')


    