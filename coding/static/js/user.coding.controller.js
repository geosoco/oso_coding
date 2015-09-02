(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$location', '$document', '$stateParams', 'CodeScheme', 'User', 'Tweet'];


	function UserCodingController($location, $document, $stateParams, CodeScheme, User, Tweet ) {
		var self = this;

		console.log("user coding controller!!!!");

		init();

		///////////////


		function init() {
			self.user = User.get({id: $stateParams.id});
			self.tweet = Tweet.get({user: $stateParams.id});
			console.log("usercoding init");
			console.dir($stateParams.id);
			console.dir(self.user);
		}
	}

})();