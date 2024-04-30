var SDF = SDF || {};

SDF.DTO = (function (  ) {
	var __product;

	__product = function ( data ) {
		var self = this;
		self.id = data.Id;
		self.name = data.Name;
		self.color = data.Color;
		self.price = data.ListPrice;
		//self.model = ko.observable ( data.ProductModel );
		self.model = data.ProductModel;
		self.qty = ko.observable ( data.Quantity );

		self.edit = ko.observable ( false );

		self.editOrSubmit = ko.computed ( function (  ) {
			return (self.edit ( ) === false ? "Edit" : "Submit");
		} );
	};

	return {
		Product: __product
	};
}) ( );