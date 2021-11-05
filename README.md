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
