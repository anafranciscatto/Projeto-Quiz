import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Rota principal - página inicial
@app.route('/')
def home():
    return render_template("index.html")  # Aqui apenas renderiza o HTML

# Rota para carregar o quiz
@app.route('/quiz')
def quiz():
    return render_template("quiz.html")

# Rota para retornar as perguntas em formato JSON
@app.route('/questions')
def questions():
    # Carregar perguntas do arquivo JSON
    questions = [
    {
        "question": "Qual é o maior animal terrestre do mundo?",
        "answers": [
            "Elefante Africano",
            "Girafa",
            "Cachorro",
            "Hipopótamo"
        ],
        "correct_answer": "Elefante Africano"
    },
    {
        "question": "Qual é o planeta mais próximo do Sol?",
        "answers": [
            "Vênus",
            "Terra",
            "Mercúrio",
            "Marte"
        ],
        "correct_answer": "Mercúrio"
    },
    {
        "question": "Quem pintou a Mona Lisa?",
        "answers": [
            "Pablo Picasso",
            "Leonardo da Vinci",
            "Vincent van Gogh",
            "Claude Monet"
        ],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "Qual é o maior oceano do mundo?",
        "answers": [
            "Atlântico",
            "Índico",
            "Ártico",
            "Pacífico"
        ],
        "correct_answer": "Pacífico"
    },
    {
        "question": "Quantos continentes existem no mundo?",
        "answers": [
            "5",
            "6",
            "7",
            "8"
        ],
        "correct_answer": "7"
    },
    {
        "question": "Qual é o maior país do mundo em área?",
        "answers": [
            "Canadá",
            "Estados Unidos",
            "China",
            "Rússia"
        ],
        "correct_answer": "Rússia"
    },
    {
        "question": "Qual é a capital da França?",
        "answers": [
            "Berlim",
            "Paris",
            "Madrid",
            "Roma"
        ],
        "correct_answer": "Paris"
    },
    {
        "question": "Quem foi o primeiro homem a pisar na Lua?",
        "answers": [
            "Yuri Gagarin",
            "Neil Armstrong",
            "Buzz Aldrin",
            "John Glenn"
        ],
        "correct_answer": "Neil Armstrong"
    },
    {
        "question": "Quantos estados tem o Brasil?",
        "answers": [
            "26",
            "27",
            "28",
            "30"
        ],
        "correct_answer": "26"
    },
    {
        "question": "Qual é o símbolo químico da água?",
        "answers": [
            "O2",
            "H2O",
            "CO2",
            "N2"
        ],
        "correct_answer": "H2O"
    },
    {
        "question": "Em que ano a internet foi inventada?",
        "answers": [
            "1995",
            "1989",
            "2001",
            "1985"
        ],
        "correct_answer": "1989"
    },
    {
        "question": "Qual é o esporte mais popular do mundo?",
        "answers": [
            "Futebol",
            "Tênis",
            "Basquete",
            "Críquete"
        ],
        "correct_answer": "Futebol"
    },
    {
        "question": "Quantos minutos tem uma hora?",
        "answers": [
            "50",
            "60",
            "70",
            "80"
        ],
        "correct_answer": "60"
    },
    {
        "question": "Qual é o animal que simboliza a paz?",
        "answers": [
            "Pomba",
            "Leão",
            "Águia",
            "Cavalo"
        ],
        "correct_answer": "Pomba"
    },
    {
        "question": "Qual é o nome do maior deserto do mundo?",
        "answers": [
            "Deserto do Atacama",
            "Deserto do Saara",
            "Deserto da Arábia",
            "Deserto de Gobi"
        ],
        "correct_answer": "Deserto do Saara"
    }
]


    return jsonify(questions)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
