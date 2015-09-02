(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodeListController", CodeListController);

	CodeListController.$inject = ['$location', '$document', 'CodeScheme', 'UserCodeInstance'];


	function CodeListController($location, $document, CodeScheme, UserCodeInstance) {
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

		function getCodeId(codeName) {
			for(var i = 0; i < self.codes.length; i++) {
				if(self.codes[i].name.toLowerCase() == codeName.toLowerCase()) {
					return self.codes[i].id;
				}
			}
			return -1;
		}

		self.addCode = function(id) {
			console.log("addCode");


			if(id === undefined || id === null || id == -1) {
				if(self.filteredItems && self.filteredItems.length > 0) {
					id = self.filteredItems[0].id;
				}
				if(id === undefined || id === null || id == -1) {
					id = getCodeId(self.codeName);	
				}				
			}



			console.log("id: " + id);

		}


		self.createCode = function(name) {
			console.log("create code: " + name);
		}

	}


})();