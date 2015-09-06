(function() {
	'use strict';

	var app = angular.module("coding.app");

	app.directive("emtweet", ['$compile', emTweetDirective]);
	app.directive("emtweetText", ['$compile', emTweetTextDirective]);
	app.directive("tweetMention", ['$compile', emTweetMentionDirective]);
	app.directive("tweetUrl", ['$compile', emTweetUrlDirective]);
	app.directive("tweetMedia", ['$compile', emTweetMediaDirective]);
	app.directive("tweetHashtag", ['$compile', emTweetHashtagDirective]);
	app.directive("tweetProfileImage", ['$compile', emTweetProfileImageDirective]);
	//app.controller("tweetController", ["$compile", "$scope", "$element" tweetController]);


	function emTweetDirective($compile) {
		return {
			restrict: 'E', 
			scope: { tweet: '=', assignment: '='},
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

			$scope.unresolved_mentions = [];
			$scope.unresolveld_urls = [];
			$scope.unresolved_hashtags = [];

			//
			// Mentions
			//
			for(var i=0; i < tweet.mentions.length; i++) {
				var mention = tweet.mentions[i];

				var mentionLink = '<tweet-mention assignment_id="' + $scope.assignment.id + '" screen_name="' + 
				mention.screen_name + '" user_id="' + mention.id + '"></tweet-mention>';

				if(html.indexOf(mention.screen_name) >= 0) {
					html = html.replace('@' + mention.screen_name, mentionLink);
				} else {
					$scope.unresolved_mentions.push(mention);
				}
			}

			//
			// URLS
			//
			for(var i=0; i < tweet.url_set.length; i++) {
				var url = tweet.url_set[i];

				var urlLink = '<tweet-url id="' + url.id + 
					'" expanded_url="' + url.expanded_url + '" display_url="' + 
					url.display_url + '" url="' + url.url + '" />';

					html = html.replace(url.url, urlLink);
			}

			//
			// Hashtags
			//
			for(var i=0; i < tweet.hashtag_set.length; i++) {
				var ht = tweet.hashtag_set[i];

				var htLink = '<tweet-hashtag ht-id="' + ht.id + '" ht-text="' + ht.text + '" />';

				html = html.replace('#' + ht.text, htLink);
			}

			//
			// Media
			//


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
				'<i class="fa fa-twitter"></i><span class="sr-only">Twitter</a></a></span>')
		}
	}

	function emTweetUrlDirective($compile) {
		return {
			restrict: 'E',
			scope: { displayUrl: '@', url: '@', id: '@', expandedUrl: '@'},
			transclude: 'element',
			replace: true,
			template: ('<span class="tweet-url">' + 
				'<a href="{{expandedUrl}}" target="_blank" data-id="{{id}}">{{url}}</a></span>' )
		}		
	}

	function emTweetMediaDirective($compile) {
		return {
			restrict: 'E',
			scope: { displayUrl: '@', mediaId: '@', id: '@', expandedUrl: '@', mediaUrl: '@', type: '@'},
			transclude: 'element',
			replace: true,
			template: ('<span class="tweet-media">' + 
				'<a href="{{mediaUrl}}" target="_blank" data-id="{{id}}">{{displayUrl}}</a></span>' )
		}		
	}

	function emTweetHashtagDirective($compile) {
		return {
			restrict: 'E',
			scope: { id: '@htId', text: '@htText'},
			transclude: 'element',
			replace: true,
			template: ('<span class="tweet-hashtag">' + 
				'<a href="/hashtags/{{id}}/" target="_blank" data-id="{{id}}">#{{text}}</a></span>' )
		}		
	}	


	function emTweetProfileImageDirective($compile) {
		return {
			restrict: 'E',
			scope: { user: '=', imgUrl: '=', size: '@'},
			transclude: 'element',
			replace: true,
			template: '<img src="{{imgUrl}}">',
			link: emTweetProfileImageLink
		}
	}

	function emTweetProfileImageLink($scope, $elem, $attrs) {
		var url = $scope.imgUrl || "",
			size = $scope.size,
			html = "";

		if(size && size.length > 0) {
			size = size.toLowerCase();

			if($scope.size === "large") {
				url = url.replace("_normal.jpeg", "_400x400.jpeg");
			}
			else if($scope.size === "medium") {
				url = url.replace("_normal.jpeg", "_bigger.jpeg")
			}
		}

		html = '<img src="' + url + '">';

		console.log("emTweetProfileImageLink: " + html)

		return $elem.html(html);
	}


})();