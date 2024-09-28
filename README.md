# Проект магазина на Django

## Установка и запуск

1. Установите зависимости из файла `pyproject.toml`, используя Poetry:
    ```bash
    poetry install
    ```
2. Создайте базу данных postgresql и установите настройки подключения как в [config/settings.py](config/settings.py#L75-L82)


3. Примените миграции

   ``` bash
    python manage.py migrate
   ```

4. Создайте учетную запись администратора

   ``` bash
   python manage.py createsuperuser
   ```

5. Заполните базу из фикстур, используя команду `fill_catalog`

   ``` bash
   python manage.py fill_catalog
   ```

6. Запустите сервер:
    ```bash
    python manage.py runserver
    ```
      
7. Перейдите по адресу сервера разработки [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   или в админку [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

> *На текущий момент можно перейти на страницу каталога товаров,
> отдельную страницу каждого товара и страницу контактов, а так же
> создать товар. \
> Товары выводятся с пангинацией по 9 товаров на странице. \
> Так же можно загрузить данные о товарах
> из фикстур в базу данных и посмотреть их в каталоге товаров. \
> \
Добавлено приложение Блога (статей) с возможностью просмотра 
> как списка статей, так и отдельной статьи, создания, редактирования и удаления статей. \
Статьи выводятся с пангинацией по 4 на странице.*

## Автор
Dmitry Skryabin <dimanskr2@gmail.com>