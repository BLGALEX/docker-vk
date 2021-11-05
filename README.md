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

Скрипт выполнит два POST запроса, а также два GET запроса. Доступные запросы 


## Backend 20

Для того чтобы развернуть ваш собственный проект с помощью docker необходимо выполнить следующие комнады на linux машине:
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

## Запуск сервиса

Для установки понадобится установленный docker и docker-compose

> sudo apt install docker.io

Далее клонируем репозиторий в нужную папку

> git clone https://<your_github_username>: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@github.com/BLGALEX/docker-vk.git

Переходим в папку скопированного репозитория и запускаем docker-compose
(Для запуска сервиса необходимо >400 Mb RAM)

> cd docker-vk
> docker-compose up

Теперь rest-api будет доступен через 1234 порт. 

## Запросы 

Отправлять картинки можно через POST запрос на your_host_ip:1234/upload

В запросе необходимо указать единственное поле 'image':

{
  'image' : "example.jpg"
}

Получать ссылки на картинки можно через GET запрос your_host_ip:1234/get/<id>

  Либо через GET запрос your_host_ip:1234/get , указав в запросе поле 'id':
  
{
  'id' : 1
}
