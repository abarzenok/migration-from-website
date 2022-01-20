# Обрезка ссылок с помощью Битли

Программа позволяет получать сокращенные ссылки Битли ([bit.ly](http://bit.ly)) через терминал, а также получать статистику кликов по имеющимся ссылкам.

### Как установить

Для корректной работы, необходимо зарегистрировать API-ключ и положить его рядом с программой в `.env` файл.
Чтобы получить ключ, необходимо:
1. Зайти в настройки аккаунта [bit.ly](http://bit.ly)
2. Перейти в раздел API
3. Ввести свой пароль
4. Нажать "Generate token"
5. Скопировать сгенерированный токен

![image](https://user-images.githubusercontent.com/69277070/150213702-0e95fbe1-ebc0-45d2-afbe-a562123ab87c.png)

6. Рядом с программой создать файл `.env` со следующим содержимым:
```BITLY_API_TOKEN=<токен>```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

### Как запустить
Для запуска необходимо запустить `main.py` с HTTP-ссылкой в качестве параметра. Если ссылка - не [bit.ly](http://bit.ly), она будет сокращена и возвращена. 
```commandline
(venv) C:\Users\Dev>python main.py https://devman.org
Битлинк: bit.ly/3fE8ryb
```
Если ссылка [bit.ly](http://bit.ly) и у токена есть необходимые права - будет отображена статистика кликов за все время.
```commandline
(venv) C:\Users\Dev>python main.py bit.ly/3fE8ryb
Количество кликов: 1
```

### Решение проблем
В некоторых случаях, программа может вернуть ошибку. Например:
```
(venv) C:\Users\Dev>python main.py notalink
Не удалось обработать ссылку "notalink". Ответ от bit.ly:
 400 Client Error: Bad Request for url: https://api-ssl.bitly.com/v4/shorten
```
В таких случаях стоит проверить:
1. Нет ли опечатки в ссылке.
2. Если ссылку требуется сократить - указан ли у нее протокол (`http[s]`), он должен быть.
3. Если требуется посмотреть статистику - имеются ли у владельца токена права на просмотр статистики. 
Это можно сделать в личном кабинете, см. [Как установить](#Как-установить)
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
