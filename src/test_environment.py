import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Загрузка токенизатора и модели
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Установка pad_token равным eos_token
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
if model.config.pad_token_id is None:
    model.config.pad_token_id = tokenizer.eos_token_id

# Ввод текста
input_text = "Hello, how can I help you?"

# Токенизация входного текста с паддингом
input_ids = tokenizer.encode(input_text, return_tensors="pt")
attention_mask = torch.ones(input_ids.shape, device=input_ids.device)

# Генерация текста
outputs = model.generate(
    input_ids,
    attention_mask=attention_mask,  # Передаем маску внимания
    pad_token_id=tokenizer.pad_token_id,  # Явно указываем pad_token_id
    max_length=50,
)

# Печать результата
print(tokenizer.decode(outputs[0], skip_special_tokens=True))