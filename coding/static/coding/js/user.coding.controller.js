(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$rootScope', '$scope', '$location', '$document', '$stateParams',
		'CodeScheme', 'User', 'Tweet', 'UserCodeInstance', 'usSpinnerService'];


	function UserCodingController($rootScope, $scope, $location, $document, $stateParams, 
		CodeScheme, User, Tweet, UserCodeInstance, usSpinnerService ) {
			var self = this;


			init();
			
			///////////////


			function init() {
				$rootScope.coding_user_id = $stateParams.user_id;


				$rootScope.coding_user = User.get({id: $stateParams.user_id});

				$rootScope.coding_user.$promise.then(
					function(data){	// success
						usSpinnerService.stop("user-details");
						angular.copy(data, self);
					}, 
					function(error){ // error
						console.error(error);
					});
				
			}
		}

})();