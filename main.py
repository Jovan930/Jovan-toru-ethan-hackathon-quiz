from question import questions
from quiz_logic import run_quiz
from score import display_score
score = run_quiz(questions) 
display_score(score, len(questions))
