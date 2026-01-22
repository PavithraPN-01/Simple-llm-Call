from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

result = generator(
    "AI is the Future because",
    max_length = 20,
    num_return_sequences = 2,
    repetition_penalty =1.5
    
)

print(result)



##from transformers import pipeline, set_seed

#generator = pipeline('text-generation', model='distilgpt2')

#set_seed(42)

