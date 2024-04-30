namespace DAL
{
	using System.Collections.Generic;
	using System.Linq;
	using AutoMapper;
	using DTO;

	public class ProductRepository
	{
		private readonly AdventureWorksEntities _entities;

		public ProductRepository ( )
		{
			_entities = new AdventureWorksEntities ( );

			Mapper.CreateMap < Product, DTOProduct > ( )
				  .ForMember ( dest => dest.Id, opt => opt.MapFrom ( src => src.ProductID ) )
				  .ForMember ( dest => dest.ProductModel, opt => opt.MapFrom ( src => src.ProductModel.Name ) )
				  .ForMember ( dest => dest.Quantity,
							   opt =>
							   opt.MapFrom (
										    src => src.ProductInventory
													  .FirstOrDefault ( w => w.ProductID.Equals ( src.ProductID ) ).Quantity ) );

			Mapper.CreateMap < ProductModel, DTOProductModel > ( );
		}

		public DTOProduct GetProduct ( int productId )
		{
			Product product = _entities.Products.SingleOrDefault ( s => s.ProductID.Equals ( productId ) );
			DTOProduct dto = Mapper.Map < Product, DTOProduct > ( product );
			return dto;
		}

		public IEnumerable < DTOProduct > GetProducts ( )
		{
			var products = _entities.ProductInventory
									.Where ( w => w.Quantity > 0 && w.Product.ProductModel.Name != "" && !string.IsNullOrEmpty ( w.Product.Color ) )
									.Select ( s => s.Product )
									.Take ( 200 ).ToArray ( );

			var dtos = Mapper.Map < Product [ ], IList < DTOProduct > > ( products );
			return dtos;
		}

		public bool Sell ( int productId )
		{
			var product = _entities.Products.SingleOrDefault ( w => w.ProductID.Equals ( productId ) );

			if ( product == null )
				return false;

			var pi = _entities.ProductInventory.Single ( s => s.ProductID.Equals ( productId ) );
			pi.Quantity -= 1;

			return true;
		}

		public IEnumerable < DTOProductModel > GetProductModels ( )
		{
			var productModels = _entities.ProductModels
										 .Distinct ( )
										 .OrderBy ( o => o.Name )
										 .ToArray ( );
			var dtos = Mapper.Map < ProductModel [ ], IList < DTOProductModel > > ( productModels );
			return dtos;
		}

		public void SaveChanges ( )
		{
			_entities.SaveChanges ( );
		}

		public IEnumerable < string > GetColors ( )
		{
			var colors = from p in _entities.Products
						 where !string.IsNullOrEmpty ( p.Color )
						 group p by p.Color
						 into g
						 select new { Color = g.Key };

			return colors.Select ( s => s.Color ).ToList ( );
		}

		public void UpdateProduct ( DTOProduct dto )
		{
			var product = _entities.Products.SingleOrDefault ( w => w.ProductID.Equals ( dto.Id ) );

			if ( product == null )
				return;

			product.Color = dto.Color;
			product.ListPrice = dto.ListPrice;
			product.Name = dto.Name;
			product.ProductModel = _entities.ProductModels.SingleOrDefault ( w => w.Name.Equals ( dto.ProductModel ) );
			var inventory = _entities.ProductInventory.SingleOrDefault ( w => w.ProductID.Equals ( dto.Id ) );
			inventory.Quantity = dto.Quantity;

			_entities.SaveChanges ( );
		}
	}
}