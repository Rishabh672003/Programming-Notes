QUICK DBMS Notes

1. Definition:

- A Database Management System is software that provides an interface to create, manage, and manipulate databases.
- Purpose: To store, retrieve, update, and manage data efficiently while ensuring data integrity and security.

2. DBMS Components

- Hardware: Physical devices (servers, disks, I/O devices) used to store and process data.
- Software: The DBMS engine and associated programs (utilities, drivers).
- Data: Actual data plus metadata (data about data).
- Procedures: Rules and guidelines on how to use and maintain the database.
- Database Languages:
  - DDL (Data Definition Language): CREATE, ALTER, DROP, etc.
  - DML (Data Manipulation Language): SELECT, INSERT, UPDATE, DELETE
  - DCL (Data Control Language): GRANT, REVOKE
  - TCL (Transaction Control Language): COMMIT, ROLLBACK
- Users: DBAs, application programmers, end-users, data analysts, etc.

3. Key Concepts and Terminologies

- ACID Properties:

  - Atomicity: All-or-nothing transactions.
  - Consistency: Transactions preserve database rules.
  - Isolation: Concurrent transactions do not interfere.
  - Durability: Once committed, changes are permanent.

- Normalization: Process of organizing data to reduce redundancy (1NF, 2NF, 3NF, BCNF).

- Keys:

  - Primary Key: Uniquely identifies records.
  - Candidate Key: A minimal set of attributes for unique identification.
  - Foreign Key: References primary key in another table.

- Indexing: (A lookup table for specific colums)

  - It is a data structure technique used to locate and quickly access data in databases.
  - Several database fields are used to generate indexes.
  - The main key or candidate key of the table is duplicated in the first column, which is the Search key.
  - To speed up data retrieval, the values are also kept in sorted order.
  - It should be highlighted that sorting the data is not required.
  - The second column is the Data Reference or Pointer which contains a set of pointers holding the address of the disk
    block where that particular key value can be found.
  - Indexing improves database performance by minimizing the number of disc visits required to fulfill a query.
  - Dense Index and Sparse Index

- Joins: Combining rows from two or more tables (INNER, LEFT, RIGHT, FULL, self-joins, cross joins).
  - Retrive Data from multiple related tables.
    - Minimizes duplicate data storage across tables.
    - Optimizes operations for faster queries.
    - Types of JOINS: (https://sql-joins.leopard.in.ua/)
      - INNER JOIN -> Returns only matching rows. If no match found, NULL is returned.
      - LEFT JOIN -> Returns all rows from the left table and matching ones from the right.
      - RIGHT JOIN -> Returns all rows from the right table and matching ones from the left.
      - FULL OUTER JOIN -> Returns all rows when there's a match in either table.
      - CROSS JOIN -> Froms every possible combination of rows. Used to get cartesian product (all x all)
      - NATURAL JOIN -> Automatically detecting and joining tables on colums with same name. Can cause unintended
        matches. Unlike CROSS join, it ensures only matching colums are included
- Locking Mechanisms:
  - Shared Locks: For reading.
  - Exclusive Locks: For writing.

3. Popular Database Types:

   1. Relational Databases:

      - Store data in structured tables.
      - Schema & Query Language: Uses a fixed schema and SQL to perform CRUD operations.
      - ACID Compliance: Ensures transactions are Atomic, Consistent, Isolated, and Durable.
      - Use Cases: Ideal for applications with structured data and well-defined relationships: like banking systems,
        inventory management, and ERP systems.
      - eg: MySQL, Postgre SQL, Oracle.

   2. Document Store:

      - Data is stored as documents (usually in JSON, BSON, or XML format) which can contain nested structures.
      - Schema Flexibility: Schemas are dynamic—each document can have a different structure, making it ideal for evolving
        data models.
      - Querying: Supports rich queries on document content, indexing, and aggregation.
      - Use Cases: Well-suited for content management systems, real-time analytics, and applications with semi-structured
        data. - Examples: MongoDB, CouchDB.

   3. Key-Value Databases:

      - Data is stored as a simple key-value pair, similar to a dictionary or hash table.
      - Performance: Extremely fast for lookups when the key is known; minimal overhead in data retrieval.
      - Flexibility: Keys can reference simple values, complex objects, or even serialized data.
      - Use Cases: Commonly used for caching, session management, and scenarios where rapid access to data is critical.
      - Examples: Redis, Amazon DynamoDB (in its key-value use case), Riak KV.

   4. Graph Databases:
      - Data is represented as nodes (entities) and edges (relationships) along with properties for both.
      - Relationships: Optimized to handle complex relationships and interconnected data, allowing efficient traversal and pattern matching.
      - Querying: Uses graph query languages (e.g., Cypher) to navigate relationships and perform analytics.
      - Use Cases: Excellent for social networks, recommendation systems, fraud detection, and network analysis.
      - Examples: Neo4j, JanusGraph, Amazon Neptune.
