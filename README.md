Основная функциональность:
Перевод файлов: Скрипт считывает все .txt файлы из папки source_folder, отправляет их содержимое на перевод с помощью OpenAI GPT-4, и сохраняет переведённые файлы в папку target_folder с добавлением суффикса "_translated" к именам файлов.

Логирование: Все основные действия логируются с меткой времени, чтобы отслеживать этапы выполнения и возможные ошибки.

Проверка ключа API: Перед началом работы скрипт проверяет, является ли предоставленный API-ключ OpenAI валидным, чтобы избежать лишних запросов и ошибок во время перевода.

Структура кода:
Импорт библиотек:

os: Используется для работы с файловой системой, в частности для чтения и записи файлов.
openai: Библиотека OpenAI для взаимодействия с их API.
datetime: Для добавления меток времени к записям в логе.
Переменные:

source_folder: Путь к папке с исходными текстовыми файлами, которые нужно перевести.
target_folder: Путь к папке, в которую сохраняются переведенные файлы.
openai.api_key: API-ключ для использования OpenAI. Для работы необходимо заменить 'ВАШ_API_КЛЮЧ' на реальный ключ.
Функция log_action(action):

Логирует любое действие или событие с указанием текущего времени. Это помогает отслеживать действия в процессе выполнения скрипта.
Функция check_api_key():

Проверяет, правильный ли API-ключ. Выполняется тестовый запрос к GPT-4, чтобы убедиться, что ключ работает.
Если ключ недействителен, выводится соответствующее сообщение, и выполнение программы завершается.
Функция translate_text(text):

Формирует запрос для перевода текста в стиле "true crime story". Запрос отправляется в OpenAI API с помощью модели GPT-4.
Если запрос успешен, функция возвращает переведенный текст. В случае ошибки она логирует ошибку и возвращает None.
Функции для работы с файлами:

read_file(file_path): Считывает содержимое текстового файла с указанным путем.
write_file(file_path, content): Записывает переведенный текст в новый файл.
Функция process_files():

Выполняет основной процесс перевода. Проходит по каждому файлу в source_folder, считывает его, разбивает на куски по 2000 символов (из-за ограничения на количество токенов), отправляет каждый кусок на перевод и сохраняет результат в новом файле с суффиксом _translated.
Основной блок if __name__ == "__main__"::

Выполняется проверка API-ключа через функцию check_api_key().
Запускается процесс обработки файлов через функцию process_files().
Примечания:
API-ключ: Необходимо заменить 'ВАШ_API_КЛЮЧ' на актуальный ключ от OpenAI.
Ограничения на количество символов: Тексты разбиваются на части по 2000 символов, чтобы соответствовать лимитам запросов API.
Логи: Каждое действие записывается с временной меткой, что помогает отслеживать процесс и выявлять ошибки.