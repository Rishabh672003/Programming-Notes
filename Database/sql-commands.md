# SQL Commands

Commands in SQL are case insensitive, so `SELECT` and `select` both would just work fine.
In this not all commands are capitalized to make it easy to distinguish them from not commands

## Select command

```sql
SELECT column1, column2, ...
FROM table_name;
```

## Select Distinct command

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

We can include the count function to get the number of unique elements in the row

```sql
SELECT COUNT(DISTINCT column1) FROM table_name;
```

## Where clause

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

Operators allowed in where clause

| operator | description                                      |
| -------- | ------------------------------------------------ |
| =        | Equal                                            |
| >        | greater than                                     |
| <        | less than                                        |
| >=       | greater than or equa                             |
| <=       | less than or equal                               |
| <> or != | not equal                                        |
| BETWEEN  | between a certain range                          |
| LIKE     | search for a pattern                             |
| IN       | to specify multiple possible values for a column |

## Order By keyword

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

## And operator

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```

## Or operator

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;
```

## Not operator

```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```

It can be used with all operators like `NOT BETWEEN`, `NOT LIKE` etc.

## Insert Into Command

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

## Null values

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```

## Update Command

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**If the where clause is omitted all the values in the table will be updated**

## Reference

- [w3 school sql tutorial](https://www.w3schools.com/sql/default.asp)
