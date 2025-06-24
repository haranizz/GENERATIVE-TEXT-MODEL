# GENERATIVE-TEXT-MODEL

COMPANY : CODTECH IT SOLUTIONS

NAME : HARANI C

INTERN ID : CT04DF167

DOMAIN : ARTIFICIAL INTELLIGENCE

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH KUMAR

# DESCRIPTION OF TASK 4 - GENERATIVE TEXT MODEL #

The goal of this task was to implement a text generation system using a pre-trained deep learning model, specifically GPT-2, which is part of the Transformer family of models. GPT-2 (Generative Pretrained Transformer 2) is a powerful language model developed by OpenAI that can generate human-like text given a short prompt. It uses a transformer-based architecture and has been trained on a large corpus of internet text data.

For this task, I built a simple but effective Python script that uses the transformers library from Hugging Face to load the GPT-2 model and tokenizer. Once the model is loaded, it accepts a custom input prompt and generates coherent and contextually relevant text of a specified length.

# Technologies and Libraries Used:

1.Python – Programming language used for scripting

2.PyTorch – Backend framework used under the hood by the model

3.Transformers (by Hugging Face) – To load and interact with the pre-trained GPT-2 model

4.Jupyter Notebook / VS Code / Colab – Environments used for development and testing

# How the System Works:

1.Setup & Importing Modules:
The project begins by importing the necessary modules from the Hugging Face transformers library, particularly the pipeline utility which simplifies model loading and text generation.

2.Loading the GPT-2 Model:
Using pipeline('text-generation', model='gpt2'), the GPT-2 model is automatically downloaded and loaded into memory. This model is pre-trained and does not require any additional training for basic usage.

3.User Prompt & Text Generation:
A user-defined input string (prompt) such as "The future of space exploration" is passed into the generator. The model then predicts the most likely continuation of the text using its training knowledge. The output is customizable using parameters like max_length and num_return_sequences.

4.Output:
The model returns a generated block of text, which is printed to the console. The generated content is creative and resembles human writing, often including logical continuation of the prompt, proper grammar, and relevant ideas.

# Project Files:

1.text_generation_gpt2.py – Main Python script for running the model

2.Text_Generation_Task4.ipynb – Jupyter notebook version for experimentation

3.check_imports.py – Optional script to test library installations

4.README.md – Documentation and instructions (optional)

# Sample Prompt and Output:
Prompt: "The future of space exploration"
Generated Output:

“The future of space exploration looks promising with advances in propulsion systems, AI-based navigation, and international collaboration between space agencies. NASA and SpaceX are developing missions...”

(Note: output varies slightly on each run due to randomness.)

# Outcome & Learning:

This task helped me understand how large language models work, and how to integrate pre-trained models for natural language generation tasks. I gained hands-on experience using the Hugging Face Transformers library, which is widely used in the AI industry. It also helped me understand key parameters that affect text quality, such as generation length, temperature, and top-k sampling (for advanced tuning).

# Conclusion:

Task 4 was a creative and exciting assignment that showcased the power of language models in generating meaningful and human-like text. The GPT-2 model was easy to integrate using Hugging Face’s high-level API, and it demonstrated impressive performance even without fine-tuning. This type of system has real-world applications in chatbots, content generation, story writing, code suggestion, and more. By completing this task, I enhanced my understanding of transformers, natural language processing, and the importance of pre-trained models in modern AI systems.

# OUTPUT #

![Image](https://github.com/user-attachments/assets/78fb6c1f-9ec5-468a-b11b-99dca48b146a)



