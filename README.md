## Основная машина http://207.154.252.202:1234/
## Резервная машина http://159.65.207.158:1234/
## Backend 10 

Для запуска скрипта демоснтрации достаточно скопировать файлы 'Screenshot 2021-11-05 102431.jpg', 'Screenshot 2021-11-04 230526.jpg', '234354.jpg' и 'script.py' из репозитория в одну папку и выполнить команду:
```shell
> python3 script.py 
```
Либо выполнить следующие команды:
```shell
> git clone https://<your_github_username>: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@github.com/BLGALEX/docker-vk.git
> cd docker-vk
> python3 script.py 
```

Скрипт выполнит два POST запроса, а также два GET запроса. Доступные запросы:
* GET http://207.154.252.202:1234/get/ – список всех доступных изображений с id и ссылкой на изображение (поля 'id' и 'image').
* GET http://207.154.252.202:1234/get/"id"/ – ссылка на изображение по id.
* GET http://207.154.252.202:1234/get/?id="id" – ссылка на изображение по id.
* HOST http://207.154.252.202:1234/upload/ – загрузка изображения. Необходимо передать json с единственным полем 'image', которое содержит файл .jpg. В случае удачной загрузки возвращается json с id изображения.
* Поддерживается работа с изображениями при разрешении сторон не более 10000.

## Backend 20

Для того чтобы развернуть ваш собственный проект с помощью docker необходимо выполнить следующие комнады на linux машине (Для запуска сервиса необходимо >400 Mb RAM):
```shell
> sudo apt install docker.io
> git clone https://<your_github_username>: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@github.com/BLGALEX/docker-vk.git
> cd docker-vk
> docker-compose up
```
После чего сервис будет доступен через порт 1234, например http://127.0.0.1:1234/
В случае если сервис недоступен после сборки docker-compose выполнить ещё две команды:
```shell
> docker-compose down
> docker-compose up
```
По умолчанию в скрипте задан url основной виртуальной машины, но если развернуть сервис на другой машине, то единственным аргументом можно передать скрипту url другой машины, например:
```shell
> python3 script.py http://127.0.0.1:1234/
```

## Backend 30

Также доступен запрос
* GET http://207.154.252.202:1234/get/?id="id"&scale="scale" – получить ссылку на отмаштабированное изображение по id в соответствии с параметром scale.
* Поддерживается масштабирование изображений при результирующем разрешении сторон не более 10000.

## Backend 40

Одинаковые изображения не дублируются на сервере. Для проверки этого функционала см. backend 50

## Backend 50

Тестовые пары изображений доступны в корне репозитория в папке "тесты", все пары разложены по папкам

1. 9% noise - программа должна оставить только один файл на сервере. Изображения имеют одинаковое разрешение, различие 9%.
2. 9% noise scale - программа должна оставить один файл с большим разрешением на сервере. Различие 9%.
3. 11% noise - программа должна записать оба файла на сервере. Разрешение одинаковое, различие 11%.
4. 11% noise scale - программа должна записать оба файла на сервере. Разные разрешения, различие 11%.
5. different resolution - программа должна записать оба файла на сервере. Соотнощение сторон различается на сотую долю.
6. high_resolution_strong_scale - программа должна записать один файл на сервере. Тестируется способность корректно сравнивать одно и то же изображение при сильном маштабировании. Изображение идентичные.


