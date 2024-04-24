import openai
import json
from django.shortcuts import HttpResponse

from dotenv import load_dotenv
import os

# Load environmental variables from .env file
load_dotenv()

def question_generator(domain):
 
    # Set up your OpenAI API key
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Generate interview questions using ChatGPT
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=""""generate 10 questions for """ + domain + """ interview. return the response as a valif JSON string. The format of the string should be this ,
        {
            "questions": [
                {
                    "question": "What is React?",
                    "answer": "React is a JavaScript library for building user interfaces."
                },
                {
                    "question": "What is JSX?",
                    "answer": "JSX is a syntax extension for JavaScript."
                }
            ]
        }""",
        max_tokens=1000
    )

    # Extract generated questions from response
    generated_questions = response.choices[0].text.strip("\n")

    try:
        questions = json.loads(generated_questions)
        questions = [

        {
            'question': questions['questions'][0]['question'],
            "answer": questions['questions'][0]['answer'],
        },

        {
            'question': questions['questions'][1]['question'],
            "answer": questions['questions'][1]['answer'],
        },
        {
            'question': questions['questions'][2]['question'],
            "answer": questions['questions'][2]['answer'],
        },
        {
            'question': questions['questions'][3]['question'],
            "answer": questions['questions'][3]['answer'],
        },
        {
            'question': questions['questions'][4]['question'],
            "answer": questions['questions'][4]['answer'],
        },
        {
            'question': questions['questions'][5]['question'],
            "answer": questions['questions'][5]['answer'],
        },
        {
            'question': questions['questions'][6]['question'],
            "answer": questions['questions'][6]['answer'],
        },
        {
            'question': questions['questions'][7]['question'],
            "answer": questions['questions'][7]['answer'],
        },
        {
            'question': questions['questions'][8]['question'],
            "answer": questions['questions'][8]['answer'],
        },
        {
            'question': questions['questions'][9]['question'],
            "answer": questions['questions'][9]['answer'],
        },
    ]
        return questions
    except json.JSONDecodeError:

        return HttpResponse("this is an excepted error please try again")
    

 

