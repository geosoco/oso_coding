(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodingController", CodingController);

	CodingController.$inject = ['$rootScope', '$scope', '$location', '$document', '$stateParams', 'Assignment', 'CodeScheme'];


	function CodingController($rootScope, $scope, $location, $document, $stateParams, Assignment, CodeScheme) {
		var self = this;

		self.instances = [];


		self._destroy = $scope.$on("$destroy", onDestroy);

		init();

		////////

		function init() {
			console.log("assignment: " + $stateParams.assignment_id);

			$rootScope.assignment = Assignment.get({id: $stateParams.assignment_id});


			$rootScope.assignment_id = $stateParams.assignment_id;
		}



		function onDestroy() {
			


			// remove handler
			self._ondestroy();
		}
		
	}

})();