import json
import os


# Головна функція
def main():
    # Змінні
    current_version = None
    author = None
    laboratory_works = None

    # Функція для завантаження даних з json-файлу
    def load_data(file_name="config.json"):
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)

    # Завантужуємо інформацію
    json_content = load_data()
    current_version = json_content["version"]
    author = json_content["creator"]

    print(f" Вас вітає LAWoMan - LAboratory WArk MAnager!\n Версія: {current_version}\n Автор: {author}")
    print(" Доступні лабораторні роботи: ")

    # Знаходимо всі доступні лабораторні роботи
    laboratory_works = [i for i in os.listdir() if not os.path.isfile(i) and i.startswith("LR_")]
    if len(laboratory_works) == 0:
        print(" На жаль, доступних лабораторних робіт немає, але вони точно скоро з'являться!\n Натисніть ентер для входу")
        input()
        return

    # У кожній знайденій лабораторній роботі парсимо конфіг-файл
    laboratory_configs = {i.split("_")[1]:load_data(f"{i}/config.json") for i in laboratory_works} #[load_data(i) for i in laboratory_works]
    print("\n".join([f" [{i}] {laboratory_configs[i]["title"]}" for i in laboratory_configs.keys()]))

    while True:
        print("\n ВВедіть номер лабораторної роботи або 0 для виходу\n > ", end="")
        choice = input()
        if choice == "0" or choice == "":
            break
        else:
            if choice in laboratory_configs.keys():
                current_laboratory_work = laboratory_configs[choice]
                print(f"\n {current_laboratory_work["title"]}\n\n"
                      f" Тема: {current_laboratory_work["theme"]}\n"
                      f" Мета: {current_laboratory_work["target"]}\n"
                      f" Коментар до завдання:\n {current_laboratory_work["comment"]}")
                # TODO: додати до конфігу поле is_python; якщо True - виконати скрипт, який знаходиться в папці


if __name__ == "__main__":
    main()
