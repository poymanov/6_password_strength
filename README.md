# Password Strength Calculator

Скрипт анализирует введенный пароль и выводит рейтинг его сложности (1-10)

# Предварительные настройки

Для функционала проверки пароля по списку нерекомендуемых слов требуется разместить файл со списком слов в директории проекта под именем `blacklist.txt`. 

Список слов можно составить самостоятельно или воспользоваться [готовым](https://github.com/danielmiessler/SecLists/tree/master/Passwords).

# Как запустить

Скрипт требует для своей работы установленного интерпретатора **Python** версии **3.5**

**Запуск на Linux**

```bash
$ python password_strength.py # или python3, в зависимости от настроек системы

# cкрипт предложит ввести пароль
Enter the password to calculate its complexity:

# и выведет результат анализа
Your password rating is 3 (Weak)

# скрипт выведет прежупреждение, если файл со списком нерекомендуемых слов не был использован
Can't find blacklist file. This check will be skipped
```

Запуск на **Windows** происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
