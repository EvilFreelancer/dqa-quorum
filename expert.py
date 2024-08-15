from jinja2 import Template
from openai import OpenAI
from settings import OPENAI_API_KEY, OPENAI_BASE_URL


class Expert:
    client = None

    def __init__(self, model, base_url=None, api_key=None, prompt_template=None):
        self.prompt_template = prompt_template
        self.model = model
        self.base_url = base_url or OPENAI_BASE_URL
        self.api_key = api_key or OPENAI_API_KEY

        if self.client is None:
            self.init_client()

    def init_client(self):
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def rate_element(self, data: str) -> int:
        prompt = Template(self.prompt_template).render(context=data)
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat.completions.create(model=self.model, messages=messages, temperature=0, n=1)

        # Extract the response text and parse it as an integer rating from 1 to 5
        response_text = response.choices[0].message.content
        try:
            rating = int(response_text.strip())
        except ValueError:
            raise ValueError("Invalid rating value in response: {}".format(response_text))

        # Ensure the rating is within the valid range [1, 5]
        if rating < 1 or rating > 5:
            raise ValueError("Rating out of range: {}".format(rating))

        return rating
