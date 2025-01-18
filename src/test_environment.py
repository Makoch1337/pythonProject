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

# Токенизация входного текста с паддингом и маской внимания
input_ids = tokenizer.encode(input_text, return_tensors="pt")
attention_mask = torch.ones_like(input_ids)

# Генерация текста с включенным сэмплированием
outputs = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=50,  # Длина текста
    num_return_sequences=1,  # Количество результатов
    no_repeat_ngram_size=3,  # Запрет на повторение n-грамм длиной 3
    repetition_penalty=2.5,  # Усиленный штраф за повторения
    top_k=50,  # Ограничение по вероятности токенов
    top_p=0.9,  # Суммарная вероятность
    temperature=0.5,  # Более низкая "творческая" температура
    do_sample=True,  # Сэмплирование включено
    pad_token_id=tokenizer.pad_token_id,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))