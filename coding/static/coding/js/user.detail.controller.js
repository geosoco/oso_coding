(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserDetailController", UserDetailController);

	UserDetailController.$inject = ['$scope', '$stateParams', 'User', 'Tweet', 'usSpinnerService', 'toastr'];


	function UserDetailController($scope, $stateParams, User, Tweet, usSpinnerService, toastr ) {
			var self = this;

			console.log("user detail controller");
			console.dir($stateParams);

			init();
			
			///////////////


			function init() {

				self.user = User.get({id: $stateParams.user_id });

				self.user.$promise.then(function(data){
					console.log("loaded user data");
					console.dir(data);
				}, function(error) {
					if(error.status === 404) {
						toastr.error("User does not exist in local database");
					} else {
						toastr.error("Unexpected error from server");
					}
					
				})
			}
		}

})();