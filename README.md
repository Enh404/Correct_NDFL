# Correct_NDFL
## Cервис, проверяющий корректность исчисления НДФЛ сотрудникам.

Веб-приложение на Django, с помощью которого пользователь может отправить файл Exel с исходными данными и в ответ получить сформированный отчет Exel, основанный на исходных данных.

## Стек технологий

`Python 3.9.10` `Django 4.2` `openpyxl 3.1.2`

## Настройка и запуск на ПК
Клонируем проект:

`git clone git@github.com:Enh404/Correct_NDFL.git`

Переходим в папку с проектом:

`cd Correct_NDFL`

Устанавливаем виртуальное окружение:

`python -m venv venv`

Активируем виртуальное окружение:

`source venv/Scripts/activate`

Для деактивации виртуального окружения выполним (после работы):

`deactivate`

Устанавливаем зависимости:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Запускаем проект:

`cd NDFL_project`

`python manage.py runserver`
