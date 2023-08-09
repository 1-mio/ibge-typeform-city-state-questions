import requests
import json

BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"

def estados():
    response = requests.get(f"{BASE_URL}/estados")
    return response.json()

def municipios(estado_id):
    response = requests.get(f"{BASE_URL}/estados/{estado_id}/municipios")
    return response.json()

def generate_questions():
    questions = []

    states = estados()
    states_sorted = sorted(states, key=lambda x: x['nome'])

    state_choices = [{"label": state["nome"]} for state in states_sorted]
    questions.append({
        "type": "dropdown",
        "title": "Qual é o seu estado?",
        "properties": {
            "choices": state_choices
        }
    })

    for state in states_sorted:
        city_choices = [{"label": city["nome"]} for city in municipios(state["id"])]
        questions.append({
            "type": "dropdown",
            "title": f"Qual é a sua cidade em {state['nome']}?",
            "properties": {
                "choices": city_choices
            }
        })

    return questions

if __name__ == "__main__":
    questions = generate_questions()
    with open('new_questions.json', 'w', encoding='utf-8') as file:
        json.dump(questions, file, ensure_ascii=False, indent=4)
