using Microsoft.EntityFrameworkCore;

using TestDotnet.Data;
using TestDotnet.Service;

var builder = WebApplication.CreateBuilder(args);
{
    builder.Services.AddScoped<ProductService>();
    builder.Services.AddControllers();
    builder.Services.AddEntityFrameworkNpgsql().AddDbContext<AppDbContext>(
        options => options.UseNpgsql(
            builder.Configuration.GetConnectionString("SampleDbConnection")));
}

var app = builder.Build();
{
    app.MapControllers();
}

app.Run();