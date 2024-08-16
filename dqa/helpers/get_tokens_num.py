import tiktoken


def get_tokens_num(sample: str) -> int:
    encoding = tiktoken.get_encoding("gpt2")
    return len(encoding.encode(sample))
