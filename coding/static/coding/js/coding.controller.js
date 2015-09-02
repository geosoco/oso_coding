(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodingController", CodingController);

	CodingController.$inject = ['$rootScope', '$location', '$document', 'CodeScheme'];


	function CodingController($rootScope, $location, $document, CodeScheme) {
		var self = this;

		self.instances = [];

		init();

		////////

		function init() {
			console.log(self.assignment_id);
		}

		
	}

})();