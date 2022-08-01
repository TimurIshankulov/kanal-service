# Каналсервис
Тестовое задание Каналсервис

Необходимо разработать скрипт на языке Python 3, который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1f-qZEX1k_3nj5cahOzntYAnvO4ignbyesVO7yuBdv_g/edit) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:

4. a. Упаковка решения в docker контейнер
    
    b. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
    
    c. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.


5. Решение на проверку передается в виде ссылки на проект на Github.
В описании необходимо указать ссылку на ваш Google Sheets документ (открыть права чтения и записи для пользователя [amkolotov@gmail.com](mailto:amkolotov@gmail.com)), а также инструкцию по запуску разработанных скриптов.

**Критерии оценки:**

Всего за выполнение тестового задания можно получить 100 баллов, количество баллов выставляется согласно таблице ниже.

Внимание! Работы соискателей, не выполнивших первые 3 пункта, не будут проверяться.

1. При проверке под правильностью работы будет пониматься соответствие функционала программы поставленному ТЗ.
2. При оценке читаемости кода, не требуется 100% соблюдения стандарта PEP 8, но код должен быть логичен и не перегружен, необходимо соблюдение отступов и логики названия переменных и структур данных.
3. Оценка эффективности будет включать в правильность применения алгоритмов и структур данных. Например, стоит учитывать, что кортеж (tuple) работает быстрее, чем списки (list).
4. Комментированность кода – комментарии должны быть понятны проверяющему, и содержать достаточную информацию о функции, классе или методе.
5. По 5 пункту оценивается соответствие требованиям и подробность инструкции по запуску. Если для пользователя проверяющего не будет открыт доступ, или согласно инструкции не предоставленное ПО не запуститься баллы не будут начислены.
