(function() {
	'use strict';

	var app = angular.module("coding.app");

	app.directive("emtweet", ['$compile', emTweetDirective]);
	app.directive("emtweetText", ['$compile', emTweetTextDirective]);
	app.directive("tweetMention", ['$compile', emTweetMentionDirective]);
	app.controller("tweetController", ["$compile", "$scope", "$element", tweetController]);


	function emTweetDirective($compile) {
		return {
			restrict: 'E', 
			scope: { tweet: '=', assignment: '='},
			controller: "tweetController",
			transclude: true,
			templateUrl: "/static/coding/html/tweet.normal.html"
		}
	}

	function emTweetTextDirective($compile) {
		return {
			restrict: 'EA', 
			scope: { tweet: '=', assignment: '='},
			transclude: true,
			replace: true,
			link: emTweetTextDirectiveLink
		}

		//

		function emTweetTextDirectiveLink($scope, $elem, $attrs) {
			var tweet = $scope.tweet,
				html = tweet.text;

			for(var m=0; m < tweet.mentions.length; m++) {
				var mention = tweet.mentions[m];

				var mentionLink = '<tweet-mention assignment_id="' + $scope.assignment.id + '" screen_name="' + 
				mention.screen_name + '" user_id="' + mention.id + '"></tweet-mention>';

				html = html.replace('@' + mention.screen_name, mentionLink);
			}

			html = '<span class="tweet-text">' + html + '</span>';

			var compiledHtml = $compile(html)($scope);

			$elem.append(compiledHtml);
		}		
	}

	function emTweetMentionDirective($compile) {
		return {
			restrict: 'E',
			scope: { assignmentId: '=', screenName: '@', userId: '='},
			transclude: 'element',
			replace: true,
			template: ('<span class="tweet-mention">' + 
				'<a ui-sref="code.user({\'assignment_id\': {{assignmentId}}, \'id\': {{userId}}})">' +
				'@{{screenName}}</a>' + 
				'<a href="http://www.twitter.com/{{screenName}}' + 
				'/" target="_blank" title="View user on Twitter">' + 
				'<i class="fa fa-twitter"></i><span class="sr-only">Twitter</a></a></span>'),
			controller: function($scope) {
				console.log("emTweetMention " + $scope.screenName);
				console.dir($scope);
			}
		}
	}


	function tweetTextController($compile, $scope, $element) {
		init();

		function init() {
			createTweetHtml();
			$scope.test = "lkjlkj";
		}

		function createTweetHtml() {
			var tweet = $scope.tweet,
				html = tweet.text;

			for(var m=0; m < tweet.mentions.length; m++) {
				var mention = tweet.mentions[m];

				var mentionLink = '<tweet-mention assignment_id="{{assignment}}" screen_name="mention.screen_name" user_id="mention.id" />';

				html = html.replace('@' + mention.screen_name, mentionLink);
			}

			console.log("html: ")
			console.dir(html);

			//var compiledHtml = $compile(html)($scope);
			var trustedHtml = $sce.trustAsHtml(html);

			console.log("trustedHtml: ");
			console.dir(trustedHtml);
			//console.log("compiledHtml: ");
			//console.dir(compiledHtml);

			//$scope.html = trustedHtml;

			$element.append(trustedHtml)
			//$scope.html = $compile(html)($scope);
		}

	}


	function tweetController($compile, $sce, $scope, $element) {

	}

})();