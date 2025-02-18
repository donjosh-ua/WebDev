using Microsoft.AspNetCore.Mvc;

using TestDotnet.Data;
using TestDotnet.Domain;

namespace TestDotnet.Service;

public class ProductService(AppDbContext appDbContext)
{

    private readonly AppDbContext _appDbContext = appDbContext;

    public async Task Create(Product product)
    {
        _appDbContext.Products.Add(product);
        await _appDbContext.SaveChangesAsync();
    }

    public ActionResult<Product?> Get(Guid productId)
    {
        var product = _appDbContext.Products.Find(productId);

        return product;
    }
}