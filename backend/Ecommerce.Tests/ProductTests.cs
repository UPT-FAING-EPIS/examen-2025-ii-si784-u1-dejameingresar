using Ecommerce.Core.Models;
using Xunit;


public class ProductTests
{
[Fact]
public void Product_Has_Name()
{
var p = new Product { Name = "Test" };
Assert.Equal("Test", p.Name);
}
}