(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$location', '$document', '$stateParams', 'CodeScheme', 'User'];


	function UserCodingController($location, $document, $stateParams, CodeScheme, User ) {
		var self = this;

		console.log("user coding controller!!!!");

		init();

		///////////////


		function init() {
			self.user = User.get({id: $stateParams.id});
			console.log("usercoding init");
			console.dir($stateParams.id);
			console.dir(self.user);
		}
	}

})();