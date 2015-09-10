(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodeComparisonController", CodeComparisonController);

	CodeComparisonController.$inject = ['$scope', '$stateParams', '$q',
		'SysUser', 'Assignment', 'CodeScheme', 'UserCodeInstance'];


	function CodeComparisonController($scope, $stateParams, $q,
		SysUser, Assignment, CodeScheme, UserCodeInstance) {

			var self = this;

			self.filter = {
				users: [],
				assignments: [],
				schemes: [],
				codes: []
			}


			self._ondestroy = $scope.$on("$destroy", onDestroy);

			init();




			////////

			function init() {
				self.sysusers = SysUser.query();
				self.assignments = Assignment.query();
				self.code_schemes = CodeScheme.query();
				

				$q.all([
					self.sysusers.$promise,
					self.assignments.$promise,
					self.code_schemes.$promise
				])
				.then(function(data){
						console.log("code comparison finished loading!");
						console.dir(data);
						createFilteredCodeList();
					})
			}


			function onDestroy() {

				// remove handler
				self._ondestroy();
			}



			function createFilteredCodeList() {
				self.codes = [];

				self.code_schemes.forEach(function(d,i){
					self.codes.push.apply(self.codes, d.code_set);
				})
			}



			function buildUserInstanceQuery() {
				self.query = {page: 1, page_size: 100};

				if(self.filter.users.length) {
					self.query['coder__in'] = self.filters.users;
				}

				if(self.filter.assignments.length) {
					self.query['assignment__in'] = self.filters.assignments;
				}

				if(self.filter.schemes.length) {
					self.query['code__scheme__in'] = self.filters.schemes;
				}

				if(self.filter.codes.length) {
					self.query['code__in'] = self.filters.codes;
				}

				
			}


			function onInstanceData(data) {
				console.log("got instance data: " + data.results.length);

				self.code_instances.push.apply(
					self.code_instances,
					data.results
					)

				if(self.code_instances.length < data.count) {
					self.query.page += 1;
					requestUserCodeInstances();
				} else {
					processData();
				}

			}

			function requestUserCodeInstances() {
				var req = UserCodeInstance.get(self.query);

				req.$promise.then(onInstanceData, function(error){
					console.error("failed to get instances")
				});				
			}


			self.doFilter = function() {
				// build the query
				buildUserInstanceQuery();


				// TEMPORARY HACK
				// XXX TODO
				if(self.code_instances === undefined || self.code_instances.length == 0) {
					self.code_instances = [];

					requestUserCodeInstances();					
				}
			}


			function processData() {
				self.sysuser_map = self.sysusers.reduce(function(obj,u){ obj[u.id] = u; return obj}, {});

				buildAssignedUsersList();
				buildCodeSchemeMap();

				joinCodeInstancesAndUsers();

				buildSchemeList();

				//buildCodeSchemeMap();
				//buildSchemeList();

				
			}


			function buildAssignedUsersList() {
				var set = {};

				self.assigned_users_list = [];

				self.assignments.forEach(function(assignment){
					assignment.assigned_users.forEach(function(user){
						if(!(user.id in set)) {
							self.assigned_users_list.push(user);
							set[user.id] = 0;	
						}
						
					})
				});
			}


			function buildCodeSchemeMap() {
				self.code_map = {}

				self.code_schemes.forEach(function(scheme){
					scheme.code_set.forEach(function(code){
						self.code_map[code.id] = {
							id: code.id,
							name: code.name,
							description: code.description,
							scheme: code.scheme
						}
					});
				});

				self.code_list = Object.keys(self.code_map);
			}


			function buildSchemeList() {

				self.processed_schemes = [];

				self.code_schemes.forEach(function(scheme){

					var coders = self.sysusers.map(
						function(coder){
							return { 
								id: coder.id,
								username: coder.username
							};
						});

					// create array of simplified code objects
					var codes = scheme.code_set.map(function(code) {
						return { id: code.id, name: code.name }
					});

					var users = buildUserCodeArray(
						scheme.id,
						self.assigned_users_list);
					

					self.processed_schemes.push({
						id: scheme.id,
						name: scheme.name,
						coders: coders,
						users: users,
						_order_dirs: {},
						_order_by: []
					});


				})

			}


			function buildUserCodeArray(scheme_id, users) {
				var array = [];

				users.forEach(
					function(user){
						self.code_list.forEach(
							function(code, i) {
								var row = angular.extend(
									{}, 
									user, 
									{code_id: code, first_row: (i===0)}
								);

								array.push(row);
							}
						);
					}
				);

				return array;
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
				self.user_instance_map = {};




				// start with users
				for(var i = 0; i < self.assigned_users_list.length; i++) {
					var user = self.assigned_users_list[i];

					var coders = self.sysusers.reduce(
								function(obj,u){ 
									obj[u.id] = {}; 
									return obj;
								}, {});

					self.user_instance_map[user.id] = angular.extend(
						{}, 
						user, 
						{ coders: angular.extend({}, coders) }
					);
				}

				// now do codes;
				for(var i = 0; i < self.code_instances.length; i++) {
					var instance = self.code_instances[i];

					var user = self.user_instance_map[instance.user];

					// add coders



					var coder = user.coders[instance.created_by];

					coder.codes = coder.codes || {};

					coder.codes[instance.code] = instance;;

				}

				// create assigned_users
				/*
				self.assigned_users = [];
				for(var uid in user_map) {
					self.assigned_users.push(user_map[uid]);
				}
				*/
			}


			self.isCodeApplied = function(code_id, user_id, coder_id) {
				var coder = self.user_instance_map[user_id].coders[coder_id];

				return (coder.codes && code_id in coder.codes);
			}
			
	}

})();