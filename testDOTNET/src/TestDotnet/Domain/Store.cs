namespace TestDotnet.Domain;

public class Store
{
    public Guid Id { get; init; } = Guid.NewGuid();
    public required string Name { get; init; }
    public required string Address { get; init; }
    public required List<Product> Products { get; init; }
    public required List<Client> Clients { get; init; }
    public required List<Category> Categories { get; init; }
}