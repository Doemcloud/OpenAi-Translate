import os
import openai
from datetime import datetime

source_folder = r"C:\API_translate\for_translate"
target_folder = r"C:\API_translate\translated"

openai.api_key = 'ВАШ_API_КЛЮЧ'

def log_action(action):
    print(f"{datetime.now()} - {action}")

def check_api_key():
    try:
        openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Test"}],
            timeout=10
        )
        log_action("API key is valid.")
        print("API key is valid.")
    except openai.error.AuthenticationError:
        log_action("API key is invalid.")
        print("API key is invalid.")
        exit(1)
    except Exception as e:
        log_action(f"Error occurred: {str(e)}")
        print(f"Error occurred: {str(e)}")
        exit(1)

# Функция для перевода текста
def translate_text(text):
    prompt = f"Translate the following text into English in the style of a true crime story. Make it sound as if it was written by a native speaker:\n\n{text}"

    try:
        log_action("Отправка запроса...")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000,
            timeout=60
        )
        log_action("Запрос отправлен...")
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        log_action(f"Ошибка операции: {str(e)}")
        print(f"Ошибка перевода: {str(e)}")
        return None

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

def process_files():
    for filename in os.listdir(source_folder):
        if filename.endswith(".txt"):
            source_path = os.path.join(source_folder, filename)
            target_path = os.path.join(target_folder, filename.replace(".txt", "_translated.txt"))

            print(f"Обработка запроса {filename}...")
            log_action(f"Обработка запроса {filename}...")

            text = read_file(source_path)

            translated_text = ""
            while text:
                chunk = text[:2000]
                text = text[2000:]
                translated_chunk = translate_text(chunk)
                if translated_chunk:
                    translated_text += translated_chunk + "\n"
            write_file(target_path, translated_text)
            print(f"{filename} переведено и сохранено в {target_path}")
            log_action(f"{filename} переведено и сохранено в  {target_path}")

if __name__ == "__main__":
    check_api_key()
    process_files()
