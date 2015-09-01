(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodeListController", CodeListController);

	CodeListController.$inject = ['$location', '$document', 'CodeScheme'];


	function CodeListController($location, $document, CodeScheme) {
		var vm = this;

		vm.test = "Testing!";

		vm.tweets = CodeScheme.query();
	}

})();