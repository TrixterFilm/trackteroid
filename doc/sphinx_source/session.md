# Session

Trackeroid's `Session` extends the functionality of the regular [Session](https://ftrack-python-api.readthedocs.io/en/stable/understanding_sessions.html) in the Ftrack Python API by incorporating additional features while preserving all the existing capabilities.

## Deferred Operations

Operations can be tracked and serialized to a [.dbm file](https://docs.python.org/3/library/dbm.html#module-dbm) using the `deferred_operations` contextmanager. These serialized operations can then be committed at a later time, even in a different process.

**Process 1:**
```{include} session/examples.md
:start-after: example deferred operations1 start
:end-before: example deferred operations1 end
```

```{attention}
To commit previously stored operations you need to reconnect the session and commit. This is a single step to ensure no unwanted operations can be committed to the server.
```

**Process 2:**
```{include} session/examples.md
:start-after: example deferred operations2 start
:end-before: example deferred operations2 end
```

## Reusing Query Results

In certain scenarios where you repeatedly execute the same query, you can utilize the `reusing_query_results` context manager if the data you are querying is expected to remain unchanged. This context manager enables the retrieval of previously obtained results, executing the query only if no results have been retrieved before.

```{include} session/examples.md
:start-after: example reuse query results start
:end-before: example reuse query results end
```

## Multiple Sessions

Trackteroid utilizes a single session instance called the `SESSION` Singleton, which serves as the default session for performing queries. If required, additional sessions can be initialized and passed to queries for performing further operations.

Default Query construction:
```{include} query/examples.md
:start-after: example session start
:end-before: example session end
```

Query construction with different session:
```{include} query/examples.md
:start-after: example session2 start
:end-before: example session2 end
```

```{important}
Although it is feasible to work with multiple sessions, there are limitations associated with it. 
Since session objects serve as the foundation for collection containers and manage caches and operations, using collections from different sessions may not work seamlessly. In such cases, attempting operations across collections from different sessions will result in an `EntityCollectionOperationError` being raised to prevent unauthorized actions.

```
