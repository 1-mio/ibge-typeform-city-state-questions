import requests
import json

with open('config.json', 'r') as file:
    config = json.load(file)
TYPEFORM_API_KEY = config["TYPEFORM_API_KEY"]

FORM_ID = "zUZSxXin"

def get_current_form():
    GET_FORM_URL = f"https://api.typeform.com/forms/{FORM_ID}"

    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}"
    }

    response = requests.get(GET_FORM_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter o formulário:", response.text)
        return None

def update_form_with_new_questions(current_form, new_questions):
    current_form["fields"].extend(new_questions)

    UPDATE_FORM_URL = f"https://api.typeform.com/forms/{FORM_ID}"

    headers = {
        "Authorization": f"Bearer {TYPEFORM_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.put(UPDATE_FORM_URL, headers=headers, data=json.dumps(current_form))
    if response.status_code == 200:
        print("Formulário atualizado com sucesso!")
    else:
        print("Erro ao atualizar o formulário:", response.text)

if __name__ == "__main__":
    with open('new_questions.json', 'r', encoding='utf-8') as file:
        NEW_QUESTIONS = json.load(file)

    current_form = get_current_form()
    if current_form:
        update_form_with_new_questions(current_form, NEW_QUESTIONS)
