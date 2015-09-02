(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$location', '$document', '$stateParams', 'CodeScheme', 'User', 'Tweet'];


	function UserCodingController($location, $document, $stateParams, CodeScheme, User, Tweet ) {
		var self = this;


		init();

		///////////////


		function init() {
			self.user = User.get({id: $stateParams.id});
			self.user.tweets = Tweet.get({user: $stateParams.id});

			self.user.tweets.$promise.then(function(data) {
				console.log("user data");
				self.user.tweets = data.results;
			})
		}
	}

})();