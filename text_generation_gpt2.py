# task4_gpt2.py #

from transformers import pipeline

# Load GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Your prompt
prompt = "The future of space exploration"

# Generate text
result = generator(prompt, max_length=50, num_return_sequences=1)

# Print the result
print("Generated Text:\n")
print(result[0]['generated_text'])




 # text_generation_gpt2.py #

from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Create pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, framework="pt")

# Set your prompt
prompt = "The future of space exploration"

# Generate text
result = generator(prompt, max_length=100, num_return_sequences=1)

# Display result
print("\nGenerated Text:\n")
print(result[0]["generated_text"])


