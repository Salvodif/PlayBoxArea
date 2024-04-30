namespace MvcApplication1.Controllers
{
	using System.Web.Mvc;
	using DAL;
	using DTO;

	public class ProductController : Controller
	{
		//
		// GET: /Product/
		public ActionResult Index ( )
		{
			return View ( );
		}

		[ HttpPost ]
		[ OutputCache ( Duration = 0 ) ]
		public JsonResult Sell ( int id )
		{
			var rp = new ProductRepository ( );

			if ( int.MinValue == id && id == 0 )
				return Json ( false, JsonRequestBehavior.AllowGet );

			bool res = rp.Sell ( id );

			if ( res )
				rp.SaveChanges ( );

			var dto = rp.GetProduct ( id );

			return Json ( dto, JsonRequestBehavior.AllowGet );
		}

		[ OutputCache ( Duration = 120 ) ]
		public JsonResult InventoryData ( )
		{
			var rp = new ProductRepository ( );
			var model = rp.GetProducts ( );
			return Json ( model, JsonRequestBehavior.AllowGet );
		}

		[ OutputCache ( Duration = 21600 ) ]
		public JsonResult GetColors ( )
		{
			var rp = new ProductRepository ( );
			var model = rp.GetColors ( );
			return Json ( model, JsonRequestBehavior.AllowGet );
		}

		[ OutputCache ( Duration = 21600 ) ]
		public JsonResult GetProductModels ( )
		{
			var rp = new ProductRepository ( );
			var model = rp.GetProductModels ( );
			return Json ( model, JsonRequestBehavior.AllowGet );
		}

		[ HttpPost ]
		[ OutputCache ( Duration = 0 ) ]
		public JsonResult UpdateProduct ( DTOProduct dto )
		{
			var rp = new ProductRepository ( );

			rp.UpdateProduct ( dto );

			return Json ( true, JsonRequestBehavior.DenyGet );
		}
	}
}