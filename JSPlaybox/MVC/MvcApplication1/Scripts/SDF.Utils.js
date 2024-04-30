var SDF = SDF || {};

SDF.Utils = (function ( ) {
	var __getInventoryData, __getProductColors, __getProductModels;
	var buffer = [];

	__getInventoryData = function ( ) {
		"use strict";

		$.ajax ( {
			url: '/Product/InventoryData',
			dataType: 'json',
			async: false,
			success: function ( data ) {
				buffer = [];
				buffer = data;
			},
			fail: function ( ) {
				buffer = [];
			}
		} );

		return buffer;
	};

	__getProductColors = function ( ) {
		$.ajax ( {
			url: '/Product/GetColors',
			dataType: 'json',
			async: false,
			success: function ( data ) {
				buffer = [];
				buffer = data;
			},
			fail: function ( ) {
				buffer = [];
			}
		} );

		return buffer;
	};

	__getProductModels = function ( ) {
		$.ajax ( {
			url: '/Product/GetProductModels',
			dataType: 'json',
			async: false,
			success: function ( data ) {
				buffer = [];
				buffer = data;
			},
			fail: function ( ) {
				buffer = [];
			}
		} );
		
		return buffer;
	};

	return {
		ajax: {
			getInventoryData: __getInventoryData,
			getProductColors: __getProductColors,
			getProductModels: __getProductModels
		},

		namespace: function ( nsString ) {
			var parts = nsString.split ( '.' ),
				parent = SDF,
				i;

			// strip redundant leading global
			if ( parts[0] === "SDF" ) {
				parts = parts.slice ( 1 );
			}

			for ( i = 0; i < parts.length; i += 1 ) {
				// create a property if it doesn't exist
				if ( typeof parent[parts[i]] === "undefined" ) {
					parent[parts[i]] = {};
				}
				parent = parent[parts[i]];
			}
			return parent;
		}
	};
}) ( );