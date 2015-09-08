(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("AssignmentNavigationController", AssignmentNavigationController);

	AssignmentNavigationController.$inject = ['$rootScope', '$scope', '$state', 'usSpinnerService' ];



	function AssignmentNavigationController($rootScope, $scope, $state, uiSpinnerService) {
		var self = this;

		self.next_user = null;
		self.prev_user = null;

		self._watch = $rootScope.$watch("assignment", onAssignmentChanged);
		self._destroy = $rootScope.$on("$destroy", onDestroy);


		if($rootScope.assignment) {
			updateAssignmentIndices($rootScope.assignment);
		}

		function findCurrentUserIndex(assignments) {
			var user_id = $state.params.user_id;

			for( var i = 0; i < assignments.length; i++) {
				var a = assignments[i];

				if(a.id == user_id) {
					return i;
				}
			}

			return -1;
		}

		function getUserIdFromAssignmentList(assignments, index) {

			if(index >= 0 && index < assignments.length) {
				return assignments[index].id;
			} 

			return null;
		}

		function updateAssignmentIndices(data) {
			// reset values
			self.next_user = null;
			self.prev_user = null;

			// only if valid
			if(data && data.assigned_users) {
				var idx = findCurrentUserIndex(data.assigned_users);

				self.next_user = getUserIdFromAssignmentList(data.assigned_users, idx + 1);
				self.prev_user = getUserIdFromAssignmentList(data.assigned_users, idx - 1);
			}

			console.log("prev assignment user: " + self.prev_user);
			console.log("next assignment user: " + self.next_user);			
		}

		function onAssignmentChanged(data) {


			console.log("assignment changed");

			if(data.$promise) {
				data.$promise.then(function(prom_data) {
					updateAssignmentIndices(prom_data);
				})				
			} else {
				console.log("unknown data value in onAssignmentChanged")
			}
			
		}

		function onDestroy() {
			// remove watch handlers
			self._watch();
			self._destroy();
		}
	}

})();