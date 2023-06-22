The concept of the `EmptyCollection` shares similarities with the [optional type](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html) found in various programming languages. It serves as a mechanism to handle the absence of values or empty results.

Similar to optional types in other languages, the `EmptyCollection` provides a consistent interface and allows for operations and attribute access without the need for explicit checks for empty or null values. It acts as a container that represents the absence of a value or result.

By utilizing the `EmptyCollection`, developers can write cleaner and more concise code by treating empty results as a valid state without the need for verbose conditional statements. This promotes a more functional programming style, allowing for seamless chaining and composition of operations even in scenarios where the result might be empty.

Just as optional types in different programming languages offer methods or functions to check for presence (_isPresent()_) and provide fallback values (_orElse()_), the `EmptyCollection` provides a simple fallback functionality to handle cases where the collection is empty as it always evaluates to `False`.

This demonstrates how you can implement a straightforward fallback mechanism using the or operator when retrieving the final data.
```{include} collections/examples.md
:start-after: example fallback1 start
:end-before: example fallback1 end
```

This code example showcases how to gracefully handle scenarios where the intermediate steps of querying, filtering, and retrieving data may result in an empty collection. By utilizing the or operator and providing an empty list as a fallback, we ensure that the final result is either the desired data or an empty list, mitigating the risk of errors or unexpected behavior.

```{include} collections/examples.md
:start-after: example fallback2 start
:end-before: example fallback2 end
```
