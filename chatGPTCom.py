import openai
import configparser

class GPTCommunicator:

    def __init__(self, nume):
        config = configparser.ConfigParser()
        config.read('keys.ini')
        self.key = config.get('keys', 'key')
        self.org = config.get('keys', 'org')

        openai.organization = self.org
        openai.api_key = self.key
        self.nume = nume

    def sendMessage(self, text):
        res = openai.chat.completions.create(
            max_tokens=50,
            model='gpt-3.5-turbo',
            messages=[
                {"role":"system", "content": "Esti un asistent virtual cu numele " + self.nume + ". Vei oferi raspunsuri scurte si la obiect."},
                {"role":"user", "content": text}
            ]
        )
        return res.choices[0].message.content
