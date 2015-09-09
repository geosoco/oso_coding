(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("AssignmentController", AssignmentController);

	AssignmentController.$inject = ['$stateParams', '$q', 'Assignment', 'UserCodeInstance'];


	function AssignmentController($stateParams, $q, Assignment, UserCodeInstance) {
		var self = this;

		self.test = "testing!"

		init();

		//////////

		function init() {
			self.assignment_id = $stateParams.assignment_id;
			self.assignment = Assignment.get({id: $stateParams.assignment_id, current_user: "true"});

			self.assigned_user_codes = UserCodeInstance.get({assignment: self.assignment_id, current_user: "true"});

			$q.all([self.assignment.$promise, self.assigned_user_codes.$promise]).then(
				joinCodesAndUsers)


			console.log("assignment");
			console.dir(self.assignment_id);
			console.dir(self.assignment);
		}


		function joinCodesAndUsers() {
			var user_map = {};

			// start with users
			for(var i = 0; i < self.assignment.assigned_users.length; i++) {
				var user = self.assignment.assigned_users[i];

				user_map[user.id] = user;
			}

			// now do codes;
			for(var i = 0; i < self.assigned_user_codes.results.length; i++) {
				var instance = self.assigned_user_codes.results[i];

				var user = user_map[instance.user];

				user.codes = user.codes || [];
				user.codes.push({
					created_date: instance.created_date,
					created_by: instance.created_by,
					code: instance.code_obj
				});
			}

			// create assigned_users
			self.assigned_users = [];
			for(var uid in user_map) {
				self.assigned_users.push(user_map[uid]);
			}
		}

		self.filterHasCodes = function(value, index, array) {
			return (value.codes === undefined ||
				value.codes === null ||
			 value.codes.length === 0);
		}

		self.filterHasNoCodes = function(value, index, array) {
			return !self.filterHasCodes(value,index,array);
		}
	}

})();