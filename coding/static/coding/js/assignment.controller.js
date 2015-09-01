(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("AssignmentController", AssignmentController);

	AssignmentController.$inject = ['$location', '$document', '$stateParams', 'Assignment'];


	function AssignmentController($location, $document, $stateParams, Assignment) {
		var self = this;

		self.test = "testing!"

		init();

		//////////

		function init() {
			self.assignment_id = $stateParams.id;
			self.assignment = Assignment.get({id: $stateParams.id});
			console.log("assignment");
			console.dir(self.assignment_id);
			console.dir(self.assignment);
		}
	}

})();