namespace TestDotnet.Domain;

public class Category
{
    public Guid Id { get; init; } = Guid.NewGuid();
    public required string Name { get; init; }
    public required List<Product> Products { get; init; }
}