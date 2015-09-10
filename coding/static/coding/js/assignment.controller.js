(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("AssignmentController", AssignmentController);

	AssignmentController.$inject = ['$stateParams', '$q', 'Assignment', 'UserCodeInstance', 'CodeScheme'];


	function AssignmentController($stateParams, $q, Assignment, UserCodeInstance, CodeScheme) {
		var self = this;

		self.test = "testing!"

		init();

		//////////

		function init() {
			self.assignment_id = $stateParams.assignment_id;

			// request assignment
			self.assignment = Assignment.get({id: $stateParams.assignment_id, current_user: "true"});

			// request code instances
			self.assigned_user_codes = UserCodeInstance.get({assignment: self.assignment_id, current_user: "true"});


			$q.all([self.assignment.$promise, self.assigned_user_codes.$promise]).then(
				processData);


			console.log("assignment");
			console.dir(self.assignment_id);
			console.dir(self.assignment);
		}


		function processData() {
			buildCodeSchemeArray()

			joinCodeInstancesAndUsers();
		}


		function buildCodeSchemeArray() {
			/*
			self.code_schemes = [];

			for(var i = 0; i < self.assignment.code_schemes.length; i++ ) {
				var scheme = self.assignment.code_scheme[i],
					scheme_array = [];

				for(var j = 0; j < scheme.code_set.length; j++ ) {
					var code = self.assignment.code_set[j];

					scheme_array.push(code);
				}

				code_map[scheme.id] = scheme_map;
			}
			*/
		}


		function joinCodeInstancesAndUsers() {
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

				// codes
				user.codes = user.codes || [];
				user.codes.push({
					created_date: instance.created_date,
					created_by: instance.created_by,
					code: instance.code_obj
				});


				user.code_map = user.code_map || {};
				user.code_map[instance.code] = instance;

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

		self.isCodeAppliedForUser = function(code_id, user_codes) {
			console.log("isCodeAppliedForUser");
			console.dir(code_id);
			console.dir(user_codes);

			return (code_id in user_codes);
		}
	}

})();