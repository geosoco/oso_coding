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
			scope: { tweet: '=', assignment: '=', text: '=' },
			transclude: true,
			template: '<ng-include src="getTemplateUrl()"/>',
			controller: "TweetController as cntrl"
		}
	}

	function emTweetTextDirective($compile) {
		return {
			restrict: 'EA', 
			scope: { tweet: '=', assignment: '=', text: '='},
			transclude: true,
			replace: true,
			link: emTweetTextDirectiveLink
		}

		//

		function emTweetTextDirectiveLink($scope, $elem, $attrs) {
			var tweet = $scope.tweet,
				html = $scope.text;

			$scope.unresolved_mentions = [];
			$scope.unresolveld_urls = [];
			$scope.unresolved_hashtags = [];

			//
			// Mentions
			//
			if( tweet.mentions ) {
				for(var i=0; i < tweet.mentions.length; i++) {
					var mention = tweet.mentions[i];

					var mentionLink = '<tweet-mention assignment_id="' + $scope.assignment.id + '" screen_name="' + 
					mention.screen_name + '" user_id="' + mention.id + '"></tweet-mention>';

					if(html.indexOf(mention.screen_name) >= 0) {
						var mention_re = new RegExp('@' + mention.screen_name, "ig");
						html = html.replace(mention_re, mentionLink);
					} else {
						$scope.unresolved_mentions.push(mention);
					}
				}				
			}
			//
			// URLS
			//
			if( tweet.url_set ) {
				for(var i=0; i < tweet.url_set.length; i++) {
					var url = tweet.url_set[i];

					var urlLink = '<tweet-url id="' + url.id + 
						'" expanded_url="' + url.expanded_url + '" display_url="' + 
						url.display_url + '" url="' + url.url + '" ></tweet-url>';

						html = html.replace(url.url, urlLink);
				}

			}

			//
			// Hashtags
			//
			if( tweet.hashtag_set) {
				for(var i=0; i < tweet.hashtag_set.length; i++) {
					var ht = tweet.hashtag_set[i];

					var htLink = '<tweet-hashtag ht-id="' + ht.id + '" ht-text="' + ht.text + '" ></tweet-hashtag>';

					var hashtag_re = new RegExp('#' + ht.text, "ig");
					html = html.replace(hashtag_re, htLink);
				}

			}

			//
			// Media
			//
			if( tweet.media_set) {
				for(var i=0; i < tweet.media_set.length; i++) {
					var media = tweet.media_set[i];

					var mediaLink = '<tweet-media id="' + media.id + 
						'" media_id="' + media.media_id + '" type= "' + media.type +
						'"  expanded_url="' + media.expanded_url + '" display_url="' + 
						media.display_url + '" media_url="' + media.media_url +
						 '" ></tweet-media>';

						var short_url = media.display_url.replace(
							"pic.twitter.com/",
							"http://t.co/"); 

						html = html.replace(short_url, mediaLink);
				}
				
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
			scope: { imgUrl: '=', size: '@', user: '='},
			transclude: 'element',
			replace: true,
			template: '<div class="profile-image-url {{size}}"></div>',
			link: emTweetProfileImageLink
		}
	}

	function emTweetProfileImageLink($scope, $elem, $attrs) {
		var url = $scope.user.profile_image_url || "",
			size = $scope.size,
			html = "",
			user = $scope.user;

		if(size && size.length > 0) {
			size = size.toLowerCase();

			if($scope.size === "large") {
				url = url.replace("_normal.", "_400x400.");
			}
			else if($scope.size === "medium") {
				url = url.replace("_normal.", "_bigger.")
			}
		}

		html = '<img src="' + url + '">';

		$elem.html(html);
	}


})();