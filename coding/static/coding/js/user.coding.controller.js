(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$rootScope', '$location', '$document', '$stateParams',
		'CodeScheme', 'User', 'Tweet', 'UserCodeInstance', 'usSpinnerService'];


	function UserCodingController($rootScope, $location, $document, $stateParams, 
		CodeScheme, User, Tweet, UserCodeInstance, usSpinnerService ) {
			var self = this;


			init();

			///////////////


			function init() {
				$rootScope.coding_user_id = $stateParams.id;


				$rootScope.coding_user = User.get({id: $stateParams.id});

				$rootScope.coding_user.$promise.then(
					function(data){	// success
						usSpinnerService.stop("user-details");
						angular.copy(data, self);
					}, 
					function(error){ // error
						console.error(error);
					});

				
				self.tweets = Tweet.get({user: $stateParams.id});

				self.tweets.$promise.then(function(data) {
					console.log("user data");
					usSpinnerService.stop("tweet-list");
					self.tweets = data.results;
				})
			}
		}

})();