(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("TweetListController", TweetListController);

	TweetListController.$inject = ['$location', '$document', 'Tweet'];


	function TweetListController($location, $document, Tweet) {
		var vm = this;

		vm.test = "Testing!";

		vm.tweets = Tweet.query();
	}

})();