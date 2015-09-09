(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("TweetController", TweetController);

	TweetController.$inject = ['$scope', '$state', '$sce', 'usSpinnerService', 'Tweet'];


	function TweetController($scope, $state, $sce, usSpinnerService, Tweet) {
		var self = this;

		self.showDetails = false;

		self.retweet_difference = false;

		$scope.tweet.source_html = $sce.trustAsHtml($scope.tweet.source);


		checkRetweetDifference();


		function checkRetweetDifference() {
			if($scope.tweet && $scope.tweet.retweeted_status) {
				var original = $scope.tweet.retweeted_status.text,
					simple_rt = ("RT @" + 
						$scope.tweet.retweeted_status.user.screen_name + 
						": " + original),
					actual = $scope.tweet.text;

				if(simple_rt.length > 140) {
					simple_rt = simple_rt.slice(0,139) + "\u2026";
				}

				self.retweet_difference = (simple_rt !== actual) 
			}
		}


		$scope.getTemplateUrl = function() {
			var base = "/static/coding/html/";

			if ($scope.tweet.retweeted_status) {
				return base + "tweet.retweet.html";
			} else {
				return base + "tweet.normal.html";
			}
		}



	}

})();