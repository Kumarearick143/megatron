# Load model again for generation
model.load_state_dict(torch.load("trained_gpt_model.pt"))
model.eval()

# Generate text
prompt = "Once upon a time"
generated_text = generate(model, tok, prompt, max_new_tokens=100)
print(generated_text)