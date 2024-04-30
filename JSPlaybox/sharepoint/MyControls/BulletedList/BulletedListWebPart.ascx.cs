using System;
using System.ComponentModel;
using System.Web.UI.WebControls.WebParts;

namespace MyControls.BulletedList
{
	using System.Linq;
	using Microsoft.SharePoint;

	[ToolboxItemAttribute(false)]
	public partial class BulletedListWebPart : WebPart
	{
		// Uncomment the following SecurityPermission attribute only when doing Performance Profiling on a farm solution
		// using the Instrumentation method, and then remove the SecurityPermission attribute when the code is ready
		// for production. Because the SecurityPermission attribute bypasses the security check for callers of
		// your constructor, it's not recommended for production purposes.
		// [System.Security.Permissions.SecurityPermission(System.Security.Permissions.SecurityAction.Assert, UnmanagedCode = true)]
		public BulletedListWebPart()
		{
		}

		protected override void OnInit(EventArgs e)
		{
			base.OnInit(e);
			InitializeControl();
		}

		protected void Page_Load(object sender, EventArgs e)
		{
			if ( Page.IsPostBack )
				return;

			var web = SPContext.Current.Web;

			var list = web.Lists [ "TestExList" ];

			var items = list.Items.Cast < SPListItem > ( ).Select ( s => s.Title );

			myBulletedList.DataSource = items;
			myBulletedList.DataBind ( );
		}
	}
}
