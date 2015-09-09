(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("AssignmentNavigationController", AssignmentNavigationController);

	AssignmentNavigationController.$inject = ['$rootScope', '$document', '$scope', '$state', 'usSpinnerService', 'toastr' ];



	function AssignmentNavigationController($rootScope, $document, $scope, $state, uiSpinnerService, toastr) {
		var self = this;

		self.next_user = null;
		self.prev_user = null;

		self._watch = $rootScope.$watch("assignment", onAssignmentChanged);
		self._destroy = $scope.$on("$destroy", onDestroy);

		$document.on("keypress", onKeyDown);


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

			$document.off("keypress", onKeyDown);
		}

		self.navigateToUser = function(user_id) {
			//console.log("navigating to user: " + user_id)
			$state.go("code.user.tweets", {
				assignment: $state.params.assignment_id,
				user_id: user_id,
				page: 1,
				list_type: "tweets"
			}, {location: true});
		}

		self.navigateNextUser = function() {
			if(self.next_user !== null) {
				self.navigateToUser(self.next_user);
			} else {
				toastr.info("This is the last profile", "end of the road");
			}
		}

		self.navigatePreviousUser = function() {
			if(self.prev_user !== null) {
				self.navigateToUser(self.prev_user);
			} else {
				toastr.info("This is the first profile. Try the next one.", "end of the road");
			}
		}

		function onKeyDown(event) {
			var key = String.fromCharCode(event.keyCode);

			//console.log("keydown! : " + event.keyCode);
			//console.dir(event);
			switch(event.keyCode) {
				case 91: 
					// go back
					self.navigatePreviousUser();
					break;
				case 93:
					// go forward
					self.navigateNextUser();
					break;
			}
		}
	}

})();