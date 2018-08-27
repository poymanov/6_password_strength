# Password Strength Calculator

Скрипт анализирует введенный пароль и выводит рейтинг его сложности (1-10)

# Предварительные настройки

Для функционала проверки пароля по списку нежелательных слов рекомедуется использовать словарь со списком таких слов.

Словарь можно составить самостоятельно или воспользоваться [готовым](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора **Python** версии **3.5**

**Запуск на Linux**

```bash
$ python password_strength.py --blacklist file.txt # или python3, в зависимости от настроек системы

# cкрипт предложит ввести пароль
Enter the password to calculate its complexity:

# и выведет результат анализа
Your password rating is 3 (Weak)

# скрипт выведет предупреждение, если файл со списком нерекомендуемых слов не был использован
$ python password_strength.py
Enter the password to calculate its complexity:
Failed to read blacklist file. This check will be skipped
Your password rating is 3 (Weak)
```

Запуск на **Windows** происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
