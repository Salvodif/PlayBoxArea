var SDF = SDF || {};

SDF.Views = (function (   ) {
	var __productViewModel;

	__productViewModel = {
		products: ko.observableArray ( [] ),
		productModels: ko.observableArray ( [] ),
		colors: ko.observableArray ( [] ),
		filter: ko.observable ( "" ),

		init: function ( ) {
			console.log ( "init" );
			var buffer;
			var items = [];

			if ( this.products ( ).length === 0 ) {
				buffer = SDF.Utils.ajax.getInventoryData ( );
				items = [];

				ko.utils.arrayForEach ( buffer, function ( item ) {
					items.push ( new SDF.DTO.Product ( item ) );
				} );

				this.products ( items );
				console.log ( "products" );
			}

			if ( this.colors ( ).length === 0 ) {
				buffer = SDF.Utils.ajax.getProductColors ( );
				items = [];

				ko.utils.arrayForEach ( buffer, function ( item ) {
					items.push ( item );
				} );

				this.colors ( items );
				console.log ( "colors" );
			}

			if ( this.productModels ( ).length === 0 ) {
				buffer = SDF.Utils.ajax.getProductModels ( );
				items = [];

				ko.utils.arrayForEach ( buffer, function ( item ) {
					items.push ( item );
				} );

				this.productModels ( items );
				console.log ( "product models" );
			}
		}


		// Operations
		//                $("a#product-edit").live("click", function () {
		//                    var dto = ko.dataFor(this);

		//                    if (dto.edit() == false) {
		//                        dto.edit(true);
		//                    } else {
		//                        $.post('/Product/UpdateProduct',
		//                            {
		//                                Id: dto.id,
		//                                Name: dto.name,
		//                                Color: dto.color,
		//                                ListPrice: dto.price,
		//                                ProductModel: dto.model,
		//                                Quantity: dto.qty
		//                            },
		//                            function () {
		//                                dto.edit(false);
		//                            });
		//                    }
		//                });

		//                $(document).one("click", "#product-sell", function () {
		//                    var itemToSell = ko.dataFor(this);
		//                    $.post('/Product/Sell',
		//                        { id: itemToSell.id },
		//                        function (data) {
		//                            itemToSell.qty(data.Quantity);
		//                        });
		//                });

		//                $(document).one("click", "#product-add", function () {
		//                    console.log('show dialog');
		//                    $("#product-add-dialog").dialog({
		//                        modal: true,
		//                        width: 500,
		//                        buttons: {
		//                            Save: function () {
		//                                $(this).dialog("close");
		//                            },
		//                            Cancel: function () {
		//                                $(this).dialog("close");
		//                            }
		//                        }
		//                    });
		//                });
		//                // END Operations
	};

	//ko.utils.arrayFilter - filter the items using the filter text
	__productViewModel.filteredItems = ko.dependentObservable ( function (   ) {
		var filter = this.filter ( ).toLocaleLowerCase ( );

		console.log ( filter );
		console.log ( "filteredItems" );

		if ( !filter ) {
			if ( this.products ( ).length === 0 ) {
				this.init ( );
			}

			return this.products ( );
		} else {
			console.log ( "filtered items" );
			return ko.utils.arrayFilter ( this.products ( ), function ( item ) {
				return ko.utils.stringStartsWith ( item.color.toLowerCase ( ), filter );
			} );
		}

	}, __productViewModel );

	return {
		Product: __productViewModel
	};
}) ( );