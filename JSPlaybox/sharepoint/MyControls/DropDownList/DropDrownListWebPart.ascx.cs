namespace MyControls.DropDownList
{
	using System;
	using System.ComponentModel;
	using System.Linq;
	using System.Web.UI.WebControls.WebParts;
	using Microsoft.SharePoint;

	[ ToolboxItem ( false ) ]
	public partial class DropDownListWebPart : WebPart
	{
		// Uncomment the following SecurityPermission attribute only when doing Performance Profiling using
		// the Instrumentation method, and then remove the SecurityPermission attribute when the code is ready
		// for production. Because the SecurityPermission attribute bypasses the security check for callers of
		// your constructor, it's not recommended for production purposes.
		// [System.Security.Permissions.SecurityPermission(System.Security.Permissions.SecurityAction.Assert, UnmanagedCode = true)]
		public DropDownListWebPart ( )
		{
		}

		protected override void OnInit ( EventArgs e )
		{
			base.OnInit ( e );
			InitializeControl ( );
		}

		protected void Page_Load ( object sender, EventArgs e )
		{
			if ( Page.IsPostBack )
				return;

			var web = SPContext.Current.Web;

			var list = web.Lists [ "TestExList" ];

			var items = list.Items.Cast < SPListItem > ( ).Select ( s => s.Title );

			myDropDownList.DataSource = items;
			myDropDownList.DataBind ( );
		}
	}
}