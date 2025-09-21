using Microsoft.EntityFrameworkCore;
using Ecommerce.Core.Models;

namespace Ecommerce.Infrastructure.Data;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<Product> Products => Set<Product>();
    // TODO: add Users, Orders, OrderItems, CartItems
}
