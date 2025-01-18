from flask import Flask, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Настройка Flask
app = Flask(__name__)

# Загрузка модели и токенизатора
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Установка pad_token, если он не задан
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
if model.config.pad_token_id is None:
    model.config.pad_token_id = tokenizer.eos_token_id

@app.route("/chat", methods=["POST"])
def chat():
    """Обработчик текстовых запросов."""
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"response": "Введите сообщение."}), 400

    # Генерация ответа
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    outputs = model.generate(
        input_ids,
        max_length=50,
        no_repeat_ngram_size=3,
        repetition_penalty=2.5,
        top_k=50,
        top_p=0.9,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
