

using Microsoft.AspNetCore.Mvc;

using TestDotnet.Domain;
using TestDotnet.Service;

namespace TestDotnet.Controller;

[ApiController]
[Route("[controller]")]
public class ProductsController(ProductService productService) : ControllerBase
{

    private readonly ProductService _productService = productService;

    [HttpPost]
    public IActionResult Create(CreateProductRequest request)
    {

        var product = request.ToDomain();

        _ = _productService.Create(product);

        return CreatedAtAction(
            actionName: nameof(Get),
            routeValues: new { ProductId = product.Id },
            value: ProductResponse.FromDomain(product)
        );
    }

    [HttpGet("{productId:guid}")]
    public IActionResult Get(Guid productId)
    {
        var product = _productService.Get(productId);

        return product is null
            ? Problem(statusCode: StatusCodes.Status404NotFound, detail: "Product not found")
            : Ok(ProductResponse.FromDomain(product));
    }

    public record CreateProductRequest(
        string Name,
        string Category,
        int Price,
        string Description)
    {
        public Product ToDomain()
        {
            return new Product
            {
                Name = Name,
                Category = Category,
                Price = Price,
                Description = Description
            };
        }
    }

    public record ProductResponse(
        Guid Id,
        string Name,
        string Category,
        int Price,
        string Description)
    {
        public static ProductResponse FromDomain(Product product)
        {
            return new ProductResponse(
                product.Id,
                product.Name,
                product.Category,
                product.Price,
                product.Description
            );
        }

        public static ProductResponse? FromDomain(ActionResult<Product?> productTask)
        {
            ActionResult<Product?> actionResult = productTask;
            return actionResult.Value is null
                ? null
                : FromDomain(actionResult.Value);
        }
    }
}