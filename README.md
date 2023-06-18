
# <p align="center">🤖 ChatGPT</p>

Welcome to the ChatGPT Clone project! This repository contains the code and resources for creating a conversational AI system similar to ChatGPT, based on the GPT-3.5 architecture. This project aims to provide a user-friendly and extensible implementation of a chatbot that can understand and respond to natural language input.
## Installation

```
$ git clone https://github.com/jaypokharna/ChatGPT.git

$ cd ChatGPT

```
    
## Quickstart

1. Clone this repository to your local machine.

2. Set up the required dependencies by running `pip install -r requirements.txt`.

3. Ensure you have `MongoDB` installed and running on your system.

4. Create a new MongoDB database for the chatbot application.

5. Obtain an `API key` for the `GPT-3.5` model from OpenAI.

6. Set your API key as an environment variable or update the `main.py` file with your API key.

7. Configure the MongoDB connection settings in the `main.py` file.

8. Run `npm rebuild` command to build the frontend application.

9. Run `npm run tailwind` to automatically rebuild the frontend application every time you make a change(In 1st terminal).

10. Launch the chatbot application by running `python main.py` (In 2nd terminal).
## Usage

```python
openai.api_key = "<OpenIA API KEY>"

app.config["MONGO_URI"] = "<MongoDB Database Connection URI>"

```
Please put your own working OpenAI API key. 

You can get one at - https://platform.openai.com/overview

```
response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
```
You can opt for other GPT-3.5 models and play with other properties according to your need.

You can get others at - https://platform.openai.com/playground

Please note that the performance of the chatbot depends on the underlying `GPT-3.5 model` and your `API key` limitations. Ensure that you have an active and valid API key to use this project effectively.




## Screenshots

![App Screenshot](/static/images/snapshot.gif)

## Customizations

You can customize the behavior of the ChatGPT Clone project to suit your specific needs. Here are a few areas you might consider customizing:

- Prompt Engineering: Modify the prompts in the chatbot.py file to guide the user or provide context for the conversation.
- Response Filtering: Implement custom logic to filter or modify the generated responses based on your requirements.
- `Integration: Integrate the chatbot with other applications or platforms by extending the existing codebase.

Feel free to explore the code and experiment with different customization options to enhance the chatbot's performance and capabilities.

## Contributing

Contributions to the `ChatGPT Clone` project are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request. Make sure to follow the existing code of conduct and conventions when contributing.


<footer>
<p align="center" style="background-color: black; padding-top: 2px; padding-bottom: 2px; rounded:5px;" >
Made with ❤️ and no 💤 by Jay Pokharna
</p>

</footer>