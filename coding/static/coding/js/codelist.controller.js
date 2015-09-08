(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodeListController", CodeListController);

	CodeListController.$inject = ['$rootScope', '$scope', '$stateParams',  '$q', 'CodeScheme', 
		'UserCodeInstance', 'usSpinnerService', 'toastr'];


	function CodeListController($rootScope, $scope, $stateParams, $q, CodeScheme, 
		UserCodeInstance, usSpinnerService, toastr) {
			var self = this;

			self.test = "Testing!";
			self.codeName = "";
			self.codeScheme = null;
			self.codes = null;
			self.codeSchemeId = 0;

			self.instance_map = {};

			init();

			////////

			function updateInstances() {
				self.loading = true;
				usSpinnerService.spin("code-instance-list");

				$rootScope.user_instances = UserCodeInstance.query({
					created_by: "current",
					assignment: $stateParams.assignment_id,
					user: $stateParams.user_id
				});

				$rootScope.user_instances.$promise.then(function(data){
					console.log("got instances");
					console.dir(data);
					self.loading = false;
					usSpinnerService.stop("code-instance-list");
					

					self.instance_map = {}
					for( var i = 0; i < data.length; i++ ) {
						var ci = data[i]; 

						self.instance_map[ci.code] = ci;
					}

					
				})

			}

			function init() {
				CodeScheme.query()
					.$promise.then(function(schemes){

						if(schemes != null && schemes.length > 0) {
							var scheme = schemes[0];

							self.codeScheme = scheme;
							self.codes = scheme.code_set;

							usSpinnerService.stop("code-list");

							updateInstances();
						}
					});

					if($rootScope.coding_user !== undefined && $rootScope.coding_user.$promise != undefined ) {
						$q.all($rootScope.assignment.$promise, $rootScope.coding_user.$promise).then(updateInstances);	
					} else {
						$rootScope.$watch("coding_user", function(){
							if($rootScope.coding_user !== undefined && $rootScope.coding_user.$promise != undefined ) {
								$q.all($rootScope.assignment.$promise, $rootScope.coding_user.$promise).then(updateInstances);	

							}
						});	

					}

					
					//$rootScope.$watch("assignment", updateInstances);
					//$rootScope.$watch("user", updateInstances);

					console.log("state params in codelist");
					console.dir($stateParams);


			}

			function getCodeId(codeName) {
				for(var i = 0; i < self.codes.length; i++) {
					if(self.codes[i].name.toLowerCase() == codeName.toLowerCase()) {
						return self.codes[i].id;
					}
				}
				return -1;
			}

			self.addCode = function(id) {
				console.log("addCode");

				if(id === undefined || id === null || id == -1) {
					if(self.filteredItems && self.filteredItems.length > 0) {
						id = self.filteredItems[0].id;
					}
					if(id === undefined || id === null || id == -1) {
						id = getCodeId(self.codeName);	
					}				
				}

				console.log("id: " + id);

				if(id !== undefined && id != null && id >= 0) {

					if(id in self.instance_map) {
						toastr.info("Code already applied");
						return;
					}


					console.log(">>assignment: " + $rootScope.assignment.id);
					console.log(">>user: " + $rootScope.coding_user.id);

					var codeInstance = new UserCodeInstance({
						user: $rootScope.coding_user.id, 
						assignment: $rootScope.assignment.id,
						code: id});
					codeInstance.$save().then(function(data){
						updateInstances();
					});
				}

				

			}


			self.createCode = function(name) {
				console.log("create code: " + name);
			}


			function deleteInstance(id) {

			}


			self.deleteCode = function(old_instance) {
				console.log("delete code");

				console.dir(old_instance);

				var instance = new UserCodeInstance({id: old_instance.id});

				console.dir(instance);
				var ret = instance.$delete({id: old_instance.id}).then(function(data){
					updateInstances();	
				});
			}

			self.deleteCodeById = function(code_id) {

				if(code_id in self.instance_map) {
					var instance = self.instance_map[code_id];
					self.deleteCode(instance);
				}
			}			


			self.isApplied = function(code_id) {
				return (code_id in self.instance_map);
				//var ret = (code_id in self.instance_map);

				//console.log("isApplied(" + code_id + ") = " + ret);
				//return ret;
			}


			$rootScope.deleteCode = self.deleteCode;


		}


})();