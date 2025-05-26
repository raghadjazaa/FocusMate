from flask import Flask, render_template, request, redirect, url_for, session
from question_generator import generate_sample_questions
import os

app = Flask(__name__)
app.secret_key = 'focusmate_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_quiz():
    questions = generate_sample_questions()
    session['questions'] = questions
    return redirect(url_for('quiz'))

@app.route('/quiz') 
def quiz():
    questions = session.get('questions', [])
    if not questions:
        return redirect(url_for('index'))
    return render_template('quiz.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    questions = session.get('questions', [])
    if not questions:
        return redirect(url_for('index'))

    user_answers = []
    correct_answers = []

    for i, q in enumerate(questions):
        user_answer = request.form.get(f'q{i}')
        user_answers.append(user_answer)
        correct_answers.append(q['answer'])

    score = sum(1 for ua, ca in zip(user_answers, correct_answers) if ua == ca)
    
    # رسالة حسب الأداء
    if score == len(questions):
        message = "Perfect! You got all answers right 🎉"
        color = "green"
    elif score >= len(questions) * 0.7:
        message = "Well done! You scored high 🔥"
        color = "orange"
    elif score >= len(questions) * 0.4:
        message = "Not bad, but you can do better!"
        color = "blue"
    else:
        message = "Keep practicing! 💪"
        color = "red"

    return render_template('result.html', score=score, total=len(questions), message=message, color=color)

if __name__ == '__main__':
    app.run(debug=True)