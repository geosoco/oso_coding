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

        if($scope.tweet.geo_coordinates_0 && $scope.tweet.geo_coordinates_1) {
            $scope.oso_distance = calculateGeoDistanceFromOso();
        }

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


        function calculateGeoDistanceFromOso() {
            return calcDistance($scope.tweet.geo_coordinates_0,
                    $scope.tweet.geo_coordinates_1,
                    48.277781, -121.843519);            
        }


        // Haversine formula
        // borrwed from http://stackoverflow.com/a/21623206
        function calcDistance(lat1, lon1, lat2, lon2) {
            var p = 0.017453292519943295;    // Math.PI / 180
            var c = Math.cos;
            var a = 0.5 - c((lat2 - lat1) * p)/2 + 
                    c(lat1 * p) * c(lat2 * p) * 
                    (1 - c((lon2 - lon1) * p))/2;

            return 12742 * Math.asin(Math.sqrt(a)); // 2 * R; R = 6371 km
        }

	}

})();
