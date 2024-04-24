import openai
import json
from django.shortcuts import HttpResponse
from dotenv import load_dotenv
import os

# Load environmental variables from .env file
load_dotenv()

  # Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_feedback(domain , question1, answer1, question2, answer2, question3, answer3, question4, answer4, question5, answer5, question6, answer6, question7, answer7, question8, answer8, question9, answer9, question10, answer10):

    # Generate feedback for interview answers using ChatGPT
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt= f'I gave a mock interview of a {domain} domain. Here are the questions and my answers:\n\nQuestion 1: {question1}\nAnswer 1: {answer1}\n\nQuestion 2: {question2}\nAnswer 2: {answer2}\n\nQuestion 3: {question3}\nAnswer 3: {answer3}\n\nQuestion 4: {question4}\nAnswer 4: {answer4}\n\nQuestion 5: {question5}\nAnswer 5: {answer5}\n\nQuestion 6: {question6}\nAnswer 6: {answer6}\n\nQuestion 7: {question7}\nAnswer 7: {answer7}\n\nQuestion 8: {question8}\nAnswer 8: {answer8}\n\nQuestion 9: {question9}\nAnswer 9: {answer9}\n\nQuestion 10: {question10}\nAnswer 10: {answer10}\n\n please provide me the overall feedback based on my performance in the mock interview make sure you include the keywords i need to use while answering and i used in the answers and also make sure not to include questions and demo answers in feedback.\n\nFeedback: provide the feedback output in html format but make sure not to use css i am already using bootstrap in output just use html formatting tags.\n\n',
        max_tokens=1000
    )

    # Extract generated questions from response
    feedback = response.choices[0].text.strip()
    return feedback
    
