namespace MyControls.BulletedListPro
{
	using System;
	using System.Collections.Generic;
	using System.ComponentModel;
	using System.Web.UI.WebControls.WebParts;
	using Interfaces;
	using PresentationLayer;

	[ToolboxItemAttribute(false)]
	public partial class BulletedListPro : WebPart, ISDFDataList
	{
		// Uncomment the following SecurityPermission attribute only when doing Performance Profiling on a farm solution
		// using the Instrumentation method, and then remove the SecurityPermission attribute when the code is ready
		// for production. Because the SecurityPermission attribute bypasses the security check for callers of
		// your constructor, it's not recommended for production purposes.
		// [System.Security.Permissions.SecurityPermission(System.Security.Permissions.SecurityAction.Assert, UnmanagedCode = true)]
		public BulletedListPro()
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

			var presenter = new MyControlsPresenter ( this );
			presenter.Populate ( );
		}

		public IEnumerable < string > DisplayData
		{
			get
			{
				return new List < string > ();
			}
			set
			{
				myBulletedList.DataSource = value;
				myBulletedList.DataBind ( );
			}
		}
	}
}
