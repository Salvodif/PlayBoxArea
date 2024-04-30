namespace Model.Tests
{
	using System.Collections.Generic;
	using System.Linq;
	using DTO;
	using FizzWare.NBuilder;
	using Interfaces;
	using Microsoft.VisualStudio.TestTools.UnitTesting;
	using Moq;
	using SharpTestsEx;


	[TestClass]
	public class TestExListTest
	{
		[TestMethod]
		public void ISDFDataList_View_TenElementsExist()
		{
			IList< MyItemDTO > items = Builder < MyItemDTO >.CreateListOfSize ( 10 )
				.All ( )
				.With ( x => x.Title = "some title" )
				.Build ( );

			var mock = new Mock < ISDFDataList > ( );

			mock.Setup ( s => s.DisplayData ).Returns ( items.Select ( i => i.Title ) );

			mock.Object.DisplayData.Should ( ).Not.Be.Empty ( );
			mock.Object.DisplayData.Count ( ).Should ( ).Be.EqualTo ( 10 );
		}
	}
}
