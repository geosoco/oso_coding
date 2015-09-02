(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodingController", CodingController);

	CodingController.$inject = ['$rootScope', '$location', '$document', '$stateParams', 'Assignment', 'CodeScheme'];


	function CodingController($rootScope, $location, $document, $stateParams, Assignment, CodeScheme) {
		var self = this;

		self.instances = [];

		init();

		////////

		function init() {
			console.log("assignment: " + $stateParams.assignment_id);

			$rootScope.assignment = Assignment.get({id: $stateParams.assignment_id});


			$rootScope.assignment_id = $stateParams.assignment_id;
		}

		
	}

})();