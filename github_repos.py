import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# AI-based repo learning decision engine (KISS style)
def ai_decision(description):
    if not description:
        return "🕳️ Description missing — consider updating README"
    elif "portfolio" in description.lower():
        return "🧑‍💼 Portfolio Project — polish UI/UX and deploy it"
    elif "API" in description.upper():
        return "🔗 API Learning — build a real API client using requests or Flask"
    elif "blog" in description.lower():
        return "📝 Blogging Project — turn into static site with Jekyll or Flask"
    elif "javascript" in description.lower():
        return "📚 Focus: JavaScript — improve JS logic and UI effects"
    elif "python" in description.lower():
        return "🐍 Python Learning — wrap it into a CLI or Flask project"
    else:
        return "🌱 Explore deeper — add features, improve code quality"

def fetch_and_store_repos(username, token):
    url = "https://api.github.com/user/repos"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        repos = response.json()

        data = []
        print(f"🗂 Total Repositories: {len(repos)}\n")

        for repo in repos:
            name = repo['name']
            url = repo['html_url']
            description = repo.get('description', '')
            decision = ai_decision(description)

            print(f"📦 {name} → {url}")
            print(f"   📝 {description}")
            print(f"   💡 {decision}\n")

            data.append({
                "name": name,
                "url": url,
                "description": description,
                "ai_decision": decision
            })

        # Save to JSON file
        with open("repos.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("✅ Repositories saved to repos.json")
    else:
        print(f"❌ Error: {response.status_code} - {response.json().get('message')}")

if __name__ == "__main__":
    fetch_and_store_repos(GITHUB_USERNAME, GITHUB_TOKEN)
