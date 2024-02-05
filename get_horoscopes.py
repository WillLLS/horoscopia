from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)

def get_horoscope():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "Tu es un astrologue designé pour produire des horoscopes journalier pour chaque signe du zodiaque en retournant la réponse au format JSON. Les clefs doivent être les suivantes: [\"belier\", \"taureau\", \"gemeaux\", \"cancer\", \"lion\", \"vierge\", \"balance\", \"scorpion\", \"sagittaire\", \"capricorne\", \"verseau\", \"poisson\"]."},
        {"role": "user", "content": "génère moi un horoscope du jour pour chaque signe du zodiaque suffisamment long."}
    ]
    )

    with open('horoscopes.json', 'w', encoding="utf-8") as outfile:
        outfile.write(response.choices[0].message.content)