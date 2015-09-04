(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$rootScope', '$location', '$document', '$stateParams',
		'CodeScheme', 'User', 'Tweet', 'UserCodeInstance'];


	function UserCodingController($rootScope, $location, $document, $stateParams, 
		CodeScheme, User, Tweet, UserCodeInstance ) {
			var self = this;


			init();

			///////////////


			function init() {
				$rootScope.coding_user_id = $stateParams.id;


				self.user = User.get({id: $stateParams.id});
				$rootScope.coding_user = self.user;
				self.user.tweets = Tweet.get({user: $stateParams.id});

				self.user.tweets.$promise.then(function(data) {
					console.log("user data");
					self.user.tweets = data.results;
				})
			}
		}

})();