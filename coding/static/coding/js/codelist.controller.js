(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodeListController", CodeListController);

	CodeListController.$inject = ['$location', '$document', 'CodeScheme'];


	function CodeListController($location, $document, CodeScheme) {
		var self = this;

		self.test = "Testing!";
		self.codeName = "";
		self.codeScheme = null;
		self.codes = null;
		self.codeSchemeId = 0;

		init();

		////////

		function init() {
			CodeScheme.query()
				.$promise.then(function(schemes){
					console.log("schemes");
					console.dir(schemes);
					if(schemes != null && schemes.length > 0) {
						var scheme = schemes[0];

						self.codeScheme = scheme;
						self.codes = scheme.code_set;
					}
				})
		}

		self.addCode = function(id) {
			console.log("addCode");
			console.dir(id);

			
		}

	}


})();