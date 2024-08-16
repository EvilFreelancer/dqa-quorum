# Quorum of LLMs for Dataset Quality Assessment

This project is designed to assess the quality of a dataset by evaluating each sample and determining if it should be
included in the cleaned version of the dataset. This project uses multiple Large Language Models (LLMs) as experts to
rate samples based on their content and provides a summary of the average rating along with a classification as `bad`
or `good`.

The evaluation process uses a quorum-based approach, where each sample is rated by a pool of experts and a majority vote
determines its inclusion in the cleaned dataset. If a majority vote has not been achieved, the sample will be excluded
from the cleaned version.

## Features

* Uses multiple LLMs to rate samples based on their content
* Calculates the average rating for each sample
* Determines if the majority vote of quorum has been achieved for each sample
* Classifies the average rating as `bad` or `good` based on a threshold of 3.5

## Architecture

<p align="center">
<img src="https://github.com/EvilFreelancer/dqa-quorum/blob/main/assets/arch.png?raw=true" alt="arch" width=50% height=50%/>
</p>

### Quorum of experts

You may use any LLM as an expert for your quorum; the only limitation is that the remote API should be compatible with
the OpenAI API client.

Example of `experts.yml` configuration:

```yaml
experts:
  - model: gpt-3.5-turbo
  - model: anthropic/claude-3-haiku
  - model: perplexity/llama-3-sonar-small-32k-online
  - model: google/palm-2-chat-bison-32k
  - model: google/gemma-2-9b-it
```

Here you may set multiple models; they will work as experts in the quorum.

### Advanced settings of experts

You may use different API keys, base URLs, and prompt templates:

```yaml
experts:
  - model: gpt-3.5-turbo
    api_key: sk-XXXX
    base_url: https://api.openai.com/v1
    prompt_template: Evaluate how well this example conveys its meaning?\nPlease rate text below from 1 (poor) to 5 (excellent), RESPONSE ONLY ONE NUMBER:\n\n{{ context }}\n
  - model: gpt-3.5-turbo
    api_key: sk-YYYY
    base_url: https://api.vsegpt.ru/v1
```

### Prompt template

The template should at least include the `{{ context }}` field.

```text
Can you evaluate how well this example conveys its meaning, how well it is organized and structured, whether it fits the theme of the conversation, and whether its responses are accurate?
Please rate text below from 1 (bad) to 5 (good), RESPONSE ONLY ONE NUMBER:

{{ context }}
```

See [prompt_template.txt](./prompt_template.txt) for details.

### Example

See [dqa.ipynb](./dqa.ipynb) for a detailed example.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Citation

If you use this project in your research or work, please cite it as follows:

```text
[Pavel Rykov]. (2024). Quorum of LLMs for Dataset Quality Assessment. GitHub. https://github.com/EvilFreelancer/dqa-quorum
```

Alternatively, in BibTeX format:

```bibtex
@misc{pavelrykov2024dqaquorum,
  author = {Pavel Rykov},
  title  = {Quorum of LLMs for Dataset Quality Assessment},
  month  = {aug},
  year   = {2024},
  url    = {https://github.com/EvilFreelancer/dqa-quorum}
}
```
