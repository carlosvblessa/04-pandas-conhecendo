import os
import json
import requests

import os

def get_github_token_from_gitconfig():
    home = os.path.expanduser("~")
    git_credentials_path = os.path.join(home, ".git-credentials")

    if not os.path.exists(git_credentials_path):
        raise FileNotFoundError("Arquivo ~/.git-credentials não encontrado.")

    with open(git_credentials_path, "r") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if "github.com" in line and line.startswith("https://"): 
            try:
                # Extrair usuário e token do formato:
                # https://usuario:token@github.com 
                user_token_part = line.split("://")[1]  # -> usuario:token@github.com
                user_token = user_token_part.split("@")[0]  # -> usuario:token
                token = user_token.split(":")[1]  # -> token

                if token.startswith("ghp_") and len(token) == 40:
                    return token
                else:
                    raise ValueError("Token inválido (não parece ser um token do GitHub)")
            except IndexError:
                raise ValueError("Formato inválido no ~/.git-credentials")

    raise ValueError("Token do GitHub não encontrado em ~/.git-credentials")


# Configurações
GITHUB_TOKEN = get_github_token_from_gitconfig()
REPO_OWNER = "carlosvblessa"
REPO_NAME = "04-pandas-conhecendo"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_github_issue(title, body, labels):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues" 
    data = {"title": title, "body": body, "labels": labels}
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Issue criada: {title}")
        return response.json()['url']
    else:
        print(f"Falha ao criar issue: {title} - {response.text}")
        return None


def main():
    with open('pandas-conhecendo-a-biblioteca.json', 'r', encoding='utf-8') as f:
        trello_data = json.load(f)

    label_map = {lbl["id"]: lbl["name"] for lbl in trello_data.get("labels", [])}
    lists_map = {lst["id"]: lst["name"] for lst in trello_data.get("lists", [])}

    for card in trello_data.get("cards", []):
        title = card["name"]
        desc = card.get("desc", "").strip()
        labels = [label_map[label_id] for label_id in card.get("idLabels", [])]

        # Adicionar nome da lista como prefixo opcional
        list_name = lists_map.get(card["idList"], "")
        if list_name:
            desc = f"**Lista:** {list_name}\n\n{desc}"

        issue_url = create_github_issue(title, desc, labels)


if __name__ == "__main__":
    main()
