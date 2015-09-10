(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("AssignmentController", AssignmentController);

	AssignmentController.$inject = ['$stateParams', '$q', 'Assignment', 'UserCodeInstance', 'CodeScheme'];


	function AssignmentController($stateParams, $q, Assignment, UserCodeInstance, CodeScheme) {
		var self = this;

		self.scheme_order_by = [];

		init();



		//////////

		function init() {
			self.assignment_id = $stateParams.assignment_id;

			// request assignment
			self.assignment = Assignment.get({id: $stateParams.assignment_id, current_user: "true"});

			// request code instances
			self.assigned_user_codes = []
			var userInstancesRequest = getUserCodeInstances(1);


			$q.all([self.assignment.$promise, userInstancesRequest.$promise]).then(function(data){
				getRemainingCodeInstances(data[1]);
			});


			console.log("assignment");
			console.dir(self.assignment_id);
			console.dir(self.assignment);
		}

		function getUserCodeInstances(page) {
			return UserCodeInstance.get({
				assignment: self.assignment_id, 
				current_user: "true", 
				page_size: 100,
				page: page
			});			
		}

		function getRemainingCodeInstances(data) {

			// first append 
			self.assigned_user_codes.push.apply(
				self.assigned_user_codes, 
				data.results);

			// now do the next request
			if(data.count > self.assigned_user_codes.length) {
				var page = (self.assigned_user_codes.length / 100) + 1;
				var next = getUserCodeInstances(page);

				next.$promise.then(getRemainingCodeInstances);
			} else {
				processData();
			}
		}


		function processData() {
			buildCodeSchemeMap();
			buildUserCodeInstanceMap();
			buildCodedArrays()
		}

		function buildCodeSchemeMap() {
			self.codes = self.assignment.code_schemes.reduce(
				function(obj, scheme) {
					scheme.code_set.forEach(function(code){
						obj[code.id] = {
							id: code.id,
							name: code.name,
							description: code.description,
							scheme: code.scheme
						}
					})
					return obj;
				}, 
				{});
		}


		function buildUserCodeInstanceMap() {
			// build a giant map of
			// [scheme id][user id][code name]
			self.user_instance_map = self.assignment.code_schemes.reduce(
				function(map,scheme){
					map[scheme.id] = self.assignment.assigned_users.reduce(
						function(map, user){
							map[user.id] = scheme.code_set.reduce(
								function(map, code){
									map[code.name] = false;

									return map
								}, {})
							return map;
						}, {})
					return map;
				}, {});

			// now apply actual code instances
			for(var i = 0; i < self.assigned_user_codes.length; i++) {
				var inst = self.assigned_user_codes[i],
					instcode = self.codes[inst.code];


				self.user_instance_map[instcode.scheme][inst.user][instcode.name] = true;
			}

		}

		function buildUserCodeArray(scheme_id, users) {
			
			return users.map(function(user){

				return angular.extend(
					{}, 
					self.user_instance_map[scheme_id][user.id], 
					{
						user_id: user.id,
						user_name: user.name,
						user_screen_name: user.screen_name
				})
			});
		}


		function buildCodedArrays() {
			self.code_schemes = self.assignment.code_schemes.map(function(scheme, i){
				// create array of simplified code objects
				var codes = scheme.code_set.map(function(code) {
					return { id: code.id, name: code.name }
				});


				var users = buildUserCodeArray(
					scheme.id,/*
					code_map, */
					self.assignment.assigned_users);

				return {
					id: scheme.id,
					name: scheme.name,
					codes: codes,
					users: users,
					_order_dirs: {},
					_order_by: []
				}
			});



		}



		function joinCodeInstancesAndUsers() {
			var user_map = {};

			// start with users
			for(var i = 0; i < self.assignment.assigned_users.length; i++) {
				var user = self.assignment.assigned_users[i];

				user_map[user.id] = user;
			}

			// now do codes;
			for(var i = 0; i < self.assigned_user_codes.length; i++) {
				var instance = self.assigned_user_codes[i];

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

		self.filterHasNoCodes = function(value, index, array) {
			return (value.codes === undefined ||
				value.codes === null ||
			 value.codes.length === 0);
		}

		self.filterHasCodes = function(value, index, array) {
			return !self.filterHasNoCodes(value,index,array);
		}

		self.isCodeAppliedForUser = function(code_id, user_codes) {
			console.log("isCodeAppliedForUser");
			console.dir(code_id);
			console.dir(user_codes);

			return (code_id in user_codes);
		}


		self.toggleOrderBy = function(scheme, field) {
			var order_by = scheme._order_by;

			for(var i=0; i < order_by.length; i++ ) {
				var col = order_by[i],
					sort = '';

				// parse current status
				var m = col.match(/([+-])?([\w\d-_\.]*)/);
				if(m) {
					sort = m[1];
					col = m[2];
				}

				// if it's not a match, continue to next
				if(col != field) {
					continue;
				}

				// toggle current sort
				switch(sort) {
					case '+': sort = '-'; break;
					case '-': sort = ''; break;
					case '': 
					default: sort = '+'; break;
				}

				// change the order
				if(sort) {
					order_by[i] = sort + col;
					scheme._order_dirs[field] = sort;
				} else {
					// remove the element from the sort
					order_by.splice(i,1);
					delete scheme._order_dirs[field];
				}


				

				// shortcut the rest of the function
				return order_by;
			}

			order_by.push("+" + field);

			scheme._order_dirs[field] = '+';

			return order_by;
		}
	}


	self.getOrderDirection = function(scheme, col) {
		return scheme._order_dirs[col];
	}

})();