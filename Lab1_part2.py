prompt = "I want a list of winners and years of the baseball World Series Championships from 2010 to 2025 in chronological order with an explanation only for the year 2026. Generate a json output that lists the winners and their years from 2010 to 2026. Answer:"
inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
outputs = model.generate(inputs, max_new_tokens=512)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)

# Results
# Please refer to the lab report for the resutls screenshot from this prompt