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
