namespace MvcApplication1.Tests.Controllers
{
	using System.Web.Mvc;
	using Microsoft.VisualStudio.TestTools.UnitTesting;
	using MvcApplication1.Controllers;
	using SharpTestsEx;

	[ TestClass ]
	public class HomeControllerTest
	{
		[ TestMethod ]
		public void HomeController_Index_ViewBag ( )
		{
			// Arrange
			var controller = new HomeController ( );

			// Act
			var result = controller.Index ( ) as ViewResult;

			// Assert, "Welcome to ASP.NET MVC!"
			result.ViewBag.Message.Should ( ).StartWith ( "Welcome" ).And ( ).EndWith ( "!" ).And ( ).Contain ( "MVC" );
		}

		[ TestMethod ]
		public void HomeController_About_NotBeNull ( )
		{
			// Arrange
			var controller = new HomeController ( );

			// Act
			var result = controller.About ( ) as ViewResult;

			// Assert
			result.Should ( ).Not.Be.Null ( );
		}
	}
}