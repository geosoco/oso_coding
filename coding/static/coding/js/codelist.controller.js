(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("CodeListController", CodeListController);

	CodeListController.$inject = ['$rootScope', '$window', '$document', '$scope', '$stateParams',  '$q', 'CodeScheme', 
		'UserCodeInstance', 'usSpinnerService', 'toastr'];


	function CodeListController($rootScope, $window, $document, $scope, $stateParams, $q, CodeScheme, 
		UserCodeInstance, usSpinnerService, toastr) {
			var self = this;

			self.test = "Testing!";
			self.codeName = "";
			self.codeScheme = null;
			self.codes = null;
			self.codeSchemeId = 0;

			self.instance_map = {};

			self.key_map = {};

			self._onDestroy = $scope.$on("$destroy", onDestroy);
			$document.on("keydown", onKeyDown);

			init();

			////////

			function updateInstances() {
				console.log("------------------------")
				console.log("requesting instances....");
				self.loading = true;
				usSpinnerService.spin("code-instance-list");

				// request instances
				$rootScope.user_instances = UserCodeInstance.query({
					created_by: "current",
					assignment: $stateParams.assignment_id,
					user: $stateParams.user_id
				});

				// handle promise
				$rootScope.user_instances.$promise.then(function(data){
					console.log("got instances");
					console.dir(data);
					

					self.instance_map = {}
					for( var i = 0; i < data.length; i++ ) {
						var ci = data[i]; 

						self.instance_map[ci.code] = ci;
					}

					self.loading = false;
					usSpinnerService.stop("code-instance-list");

					
				}, function(error) {
					toastr.error("Try refreshing the page.", "Could not load code instances.");
				})

			}

			function init() {
				CodeScheme.query()
					.$promise.then(function(schemes){

						if(schemes != null && schemes.length > 0) {
							var scheme = schemes[0];

							self.codeScheme = scheme;
							self.codes = scheme.code_set;

							updateKeyMap();

							usSpinnerService.stop("code-list");

							updateInstances();
						}
					},function(error) {
						toastr.error("Try refreshing the page.", "Could not load code scheme.");
				});

					/*
					if($rootScope.coding_user !== undefined && $rootScope.coding_user.$promise != undefined ) {
						$q.all($rootScope.assignment.$promise, $rootScope.coding_user.$promise).then(updateInstances);	
					} else {
						$rootScope.$watch("coding_user", function(){
							if($rootScope.coding_user !== undefined && $rootScope.coding_user.$promise != undefined ) {
								$q.all($rootScope.assignment.$promise, $rootScope.coding_user.$promise).then(updateInstances);	

							}
						});	

					}
					*/

					
					//$rootScope.$watch("assignment", updateInstances);
					//$rootScope.$watch("user", updateInstances);

					console.log("state params in codelist");
					console.dir($stateParams);


			}


			function onDestroy(event) {
				console.log("<><><> unbinding handlers ...");
				self._onDestroy();
				//self._onKeyDown();
				$document.off("keydown", onKeyDown);
			}


			function onKeyDown(event) {
				//console.log("keydown: " + event.keyCode);
				//console.dir(event);
				var key = String.fromCharCode(event.keyCode);
				if(key in self.key_map) {
					self.toggleCode(self.key_map[key]);
				}
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
					}, function(error) {
						toastr.error("<div>Try refreshing the page.</div><pre>raw data: " + JSON.stringify(error) + "</pre>", "Failed to delete code", {timeOut: 0, allowHtml: true, extendedTimeOut: 0});
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
				}, function(error) {
					toastr.error("<div>Try refreshing the page.</div><pre>raw data: " + JSON.stringify(error) + "</pre>", "Failed to delete code", {timeOut: 0, allowHtml: true, extendedTimeOut: 0});
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


			function updateKeyMap() {
				for(var i = 0; i < self.codes.length; i++) {
					var code = self.codes[i],
						codekey = code.key;

					self.key_map[codekey] = code.id;
				}
			}


			self.toggleCode = function(code_id) {
				if(self.isApplied(code_id)){
					self.deleteCodeById(code_id);
				} else {
					self.addCode(code_id);
				}
			}


			$rootScope.deleteCode = self.deleteCode;


		}


})();