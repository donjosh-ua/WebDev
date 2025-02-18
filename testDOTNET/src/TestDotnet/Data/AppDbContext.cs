using Microsoft.EntityFrameworkCore;

using TestDotnet.Domain;

namespace TestDotnet.Data;

public class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Product> Products { get; set; }
}
