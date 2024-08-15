from jinja2 import Template
from openai import OpenAI
from settings import OPENAI_API_KEY, OPENAI_BASE_URL, MAX_TOKENS_OUTPUT, PROMPT_TEMPLATE


class Expert:
    client = None

    def __init__(self, model, base_url=None, api_key=None, prompt_template=None):
        self.model = model
        self.base_url = base_url or OPENAI_BASE_URL
        self.api_key = api_key or OPENAI_API_KEY
        self.prompt_template = prompt_template or PROMPT_TEMPLATE

        if self.client is None:
            self.init_client()

    def init_client(self):
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def rate_sample(self, sample: str) -> int | None:
        prompt = Template(self.prompt_template).render(context=sample)
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
        response = self.client.chat.completions.create(
            model=self.model, messages=messages,
            temperature=0, n=1, max_tokens=MAX_TOKENS_OUTPUT
        )

        # Extract the response text and parse it as an integer rating from 1 to 5
        response_text = response.choices[0].message.content
        try:
            rating = int(''.join(filter(str.isdigit, response_text)))
        except ValueError:
            print("Invalid rating value in response: {}".format(response_text))
            return None

        # Ensure the rating is within the valid range [1, 5]
        if rating < 1: rating = 1
        if rating > 5: rating = 5

        return rating
