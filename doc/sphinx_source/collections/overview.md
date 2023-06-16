The result of terminated _Query_ is a collection, specifically an instance of either EntityCollection or EmptyCollection, depending on the outcome. When printed, the collection is represented as:

`EntityCollection[<Entity Type>]{<Number of Results>}` or `EmptyCollection[<Entity Type>]`

An _EntityCollection_ is a container of wrapped ftrack entity objects with the following definitions:
- It is an **ordered** container of entity objects.
- It is **immutable**, meaning its contents entities can not be added or removed once created.
- It is **iterable**, allowing for easy iteration over the entities no matter if there is a single or multiple entities in it.
- It only contains **unique** elements, ensuring there are no duplicate entities.

An _EmptyCollection_ is placeholder for an _EntityCollection_ that doesn't contain any entities.
- It is iterable, allowing for iteration even though it doesn't have any entities.
- It allows for any attribute access that you would typically perform on an _EntityCollection_, providing flexibility for operations or checks on the collection itself.
