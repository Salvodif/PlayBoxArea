using System;
using System.ComponentModel;
using System.Web.UI.WebControls.WebParts;

namespace MyControls.DropDownListPro
{
	using System.Collections.Generic;
	using Interfaces;
	using PresentationLayer;

	[ToolboxItemAttribute(false)]
	public partial class DropDownListPro : WebPart, ISDFDataList
	{
		// Uncomment the following SecurityPermission attribute only when doing Performance Profiling on a farm solution
		// using the Instrumentation method, and then remove the SecurityPermission attribute when the code is ready
		// for production. Because the SecurityPermission attribute bypasses the security check for callers of
		// your constructor, it's not recommended for production purposes.
		// [System.Security.Permissions.SecurityPermission(System.Security.Permissions.SecurityAction.Assert, UnmanagedCode = true)]
		public DropDownListPro()
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
				myDropDownList.DataSource = value;
				myDropDownList.DataBind ( );
			}
		}
	}
}
