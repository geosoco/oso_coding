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
			self.assignment = Assignment.get({id: $stateParams.id, coder: "current"});
			console.log("assignment");
			console.dir(self.assignment_id);
			console.dir(self.assignment);
		}



		self.filterHasCodes = function(value, index, array) {
			return (value.usercodeinstance_set === null || value.usercodeinstance_set.length === 0);
		}

		self.filterHasNoCodes = function(value, index, array) {
			return !self.filterHasCodes(value,index,array);
		}
	}

})();