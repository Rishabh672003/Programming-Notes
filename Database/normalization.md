# Normalization forms

A good database design can protect us from data integrity issues, this is the case where the data disagrees with
itself for example, the same person in a database can't have 2 birth dates, a good database design can protect us
from this issues, and also we do normalization to protect us from data integrity issues.
When we normalize the data, we are structuring the data in a way where it cant express redundant information.

We use different normal forms to basically tell how safe the database is from redundant data.

We will discuss 5 normal forms

## First Normal Form

- Don't convey information about a row using the row order.
  - Instead use a different column to convey that information
  - To convey the height of people use a different column for the height

- Don't have different data types in a same column
  - Most database software prevent us from doing this by default

- Not having a primary key is a violation of first normal form
  - Primary key uniquely identifies a row in a table
  - SQL query: `ALTER TABLE table_name ADD PRIMARY KEY (row_name)`

- Storing a repeating group of data items in a single row violates first normal form
  - Make a row for each group of data

## Second Normal Form

**Deletion Anomalies**: When a deletion of a record from a table results in a data loss in a table, that is called a
deletion anomaly.

**Update Anomalies**: Same as deletion anomalies but at the time of update.

**Insertion Anomalies**: These anomalies occur when it is not possible to insert data into a database because the
required fields are missing or because the data is incomplete.

- First Normal form can be more prone to deletion, update and insertion anomalies, Second normal form tries to prevent this

- Second normal form is about how the non key column relates to the primary key.
  - Each non-key attribute must depend on the entire primary key

![Image](https://github.com/user-attachments/assets/a5766d74-9cdd-44ae-a1c2-01b5f8d76b1f)

## Third Normal Form

- Third normal form prevents the existence of transitive dependencies, that is a non key attribute depending on a non
  normal form

- Third Normal Form: Every non-key attribute in a table should depend on the key, the whole key, and nothing but the key.

### Summary

![Image](https://github.com/user-attachments/assets/b79274b3-4233-4d9c-befb-d29fbf335651)

### Reference

- [Learn Database Normalization - 1Nf, 2Nf, 3Nf, 4Nf, 5Nf](https://www.youtube.com/watch?v=GFQaEYEc8_8)

- [Anomalies in DB](https://www.geeksforgeeks.org/anomalies-in-relational-model/)
