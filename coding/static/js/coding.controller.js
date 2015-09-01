(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodingController", CodingController);

	CodingController.$inject = ['$location', '$document', 'CodeScheme'];


	function CodingController($location, $document, CodeScheme) {
		var vm = this;

		vm.test = "Testing!";

		vm.tweets = CodeScheme.query();
	}

})();