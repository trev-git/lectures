# Лабораторная работа №4

## Импортирование файлов из Excel

1.	Создать базу данных.

![img](image-31.png)

2.	Произвести импорт данных из файла clients.csv с помощью графического интерфейса MySQL Workbench. Таблицу клиенты предварительно создать.

![img](image-32.png)

![img](image-33.png)

![img](image-34.png)

![img](image-35.png)

3.	Произвести импорт данных из файла agents.csv с помощью графического интерфейса MySQL Workbench. Таблицу агенты предварительно создавать НЕ надо. Создать таблицу необходимо при импорте данных.

![img](image-36.png)

![img](image-37.png)

![img](image-38.png)

4.	Таблицу клиенты очистить. Не удалить, а именно очистить. Произвести импорт данных из файла clients.csv с помощью команды LOAD DATA.

Очистим таблицу:

```sql
TRUNCATE TABLE clients;
```

![img](image-39.png)

```sql
LOAD DATA INFILE "/Users/trev/Downloads/clients.csv" INTO TABLE clients COLUMNS TERMINATED BY ',' IGNORE 1 LINES (id, FirstName, MiddleName, LastName, Phone, Email);
```

![img](image-40.png)

5.	Таблицу агенты очистить. Произвести импорт данных из файла agents.csv с помощью команды LOAD DATA.

Очистим таблицу:

```sql
TRUNCATE TABLE agents;
```

![img](image-41.png)

```sql
LOAD DATA INFILE "/Users/trev/Downloads/agents.csv" INTO TABLE agents COLUMNS TERMINATED BY ',' IGNORE 1 LINES (id, FirstName, MiddleName, LastName, DealShare);
```

![Alt text](image-42.png)
