# Trackteroid


**Declarative, object-oriented wrapper for Ftrack queries. Powerful functional-style interactions with resulting collections.**


Welcome to Trackteroid’s documentation. Get started with [Installation](installation.md) and then get an overview with the [Quickstart](quickstart.md). 

Trackteroid depends on [Ftrack](https://www.ftrack.com/en/) and its [Python API](https://ftrack-python-api.readthedocs.io/) a project management and production tracking software specifically designed for the media and entertainment industry. It is commonly used in the fields of film, television, animation, visual effects, and gaming.


## Motivation

We have decided to build a wrapping API around the Ftrack Python API to address several limitations and challenges that arise when directly interacting with the Python API. While the Ftrack Python API offers a lot of flexibility, there are certain aspects that can make development and maintenance more cumbersome and less intuitive. By creating a wrapping API, we aim to overcome these challenges and provide a more streamlined and developer-friendly experience. Here are the key reasons for this decision:

- **Simplifying Querying**
  - One of the primary challenges with the Ftrack Python API is the requirement to write queries as SQL-like strings using a custom query language. This approach often leads to complex string formatting and can be hard to read, understand, and debug. This project aims for simplifying the query logic and provides a more expressive and intuitive querying interface. This allows developers to construct queries using a more natural and readable syntax, resulting in improved productivity and reduced errors.


- **Optimizing Query Performance**
  - When working with the Ftrack Python API, developers need to ensure they write efficient queries to minimize unnecessary database calls and optimize performance. This requires careful consideration of the data retrieval logic and understanding the performance implications of different query constructions. In contrast, our API goes the extra mile by attempting to optimize the queries for performance automatically. By leveraging various optimization techniques, we aim to reduce the number of database queries, optimize data retrieval, and improve overall system performance. This alleviates the burden on developers to manually optimize their queries, allowing them to focus more on building features and functionality.


- **Abstracting Database Schema Complexity**
  - Constructing queries with the Ftrack Python API requires a good understanding of the underlying database schema and relationships. This can be a barrier for developers who are not familiar with the intricacies of the Ftrack data model. We aim to abstract away the complexities of the database schema and provide a higher-level interface that shields developers from the details. This simplifies the development process and allows developers to focus on the functionality they want to build, rather than getting lost in the intricacies of the database structure.
  

- **Enhancing Resulting Collections** 
  - The collections returned by the Ftrack Python API after executing queries may not always be convenient enough to interact with directly. They may lack certain methods or properties that would make data manipulation and processing more efficient. We can enrich the resulting collections with additional functionalities and utility methods tailored to the specific needs of our application. This improves the developer experience by providing more convenient and intuitive ways to work with the retrieved data, ultimately enhancing productivity and code maintainability.

  
- **Improved Field Accessibility**
  - The Ftrack Python API does not always present the available fields on entities directly, requiring developers to refer to the documentation or inspect the schema to determine the available properties. We do take steps to enhance field accessibility to some extent. We aim to provide a more intuitive and discoverable way for developers to access entity fields by exposing them directly through the API. This saves developers time and effort by eliminating the need for constant referencing of documentation or inspection of the underlying schema. It enhances productivity and code maintainability by making entity fields more accessible and discoverable within the development workflow.

  
In summary Trackeroid tries to empower developers by providing a more intuitive and efficient way to interact with the Ftrack platform, ultimately accelerating development, improving code quality, and enhancing the overall user experience.

```{toctree}
:maxdepth: 1

installation.md
quickstart.md
configuration.md
session.md
query.md
collections.md
```
