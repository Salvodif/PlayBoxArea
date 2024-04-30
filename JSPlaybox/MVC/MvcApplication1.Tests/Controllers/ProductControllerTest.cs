namespace MvcApplication1.Tests.Controllers
{
	using System.Collections.Generic;
	using System.Linq;
	using System.Web.Mvc;
	using DTO;
	using Microsoft.VisualStudio.TestTools.UnitTesting;
	using MvcApplication1.Controllers;
	using SharpTestsEx;

	/// <summary>
	/// Summary description for ProductController
	/// </summary>
	[ TestClass ]
	public class ProductControllerTest
	{
		public ProductControllerTest ( )
		{
			//
			// TODO: Add constructor logic here
			//
		}

		/// <summary>
		///Gets or sets the test context which provides
		///information about and functionality for the current test run.
		///</summary>
		public TestContext TestContext { get; set; }

		#region Additional test attributes

		//
		// You can use the following additional attributes as you write your tests:
		//
		// Use ClassInitialize to run code before running the first test in the class
		// [ClassInitialize()]
		// public static void MyClassInitialize(TestContext testContext) { }
		//
		// Use ClassCleanup to run code after all tests in a class have run
		// [ClassCleanup()]
		// public static void MyClassCleanup() { }
		//
		// Use TestInitialize to run code before running each test 
		// [TestInitialize()]
		// public void MyTestInitialize() { }
		//
		// Use TestCleanup to run code after each test has run
		// [TestCleanup()]
		// public void MyTestCleanup() { }
		//

		#endregion

		[ TestMethod ]
		public void ProductionController_Index_DTOProductCount ( )
		{
			var controller = new ProductController ( );
			var view = controller.Index ( ) as ViewResult;

			Assert.IsNotNull ( view );

			var model = view.Model as IEnumerable < DTOProduct >;

			model.Count ( ).Should ( ).Be.GreaterThan ( 0 );
		}
	}
}