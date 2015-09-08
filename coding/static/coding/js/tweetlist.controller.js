(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("TweetListController", TweetListController);

	TweetListController.$inject = ['$scope', '$state', 'usSpinnerService', 'Tweet'];


	function TweetListController($scope, $state, usSpinnerService, Tweet) {
		var self = this;

		console.log("^^^^^^^^^^^^^^ tweetlist");
		console.dir($state);


		$scope.page_data = null;
		self.loading = true;
		self.current_view = $state.current.name;
		self.list_type = $state.params.list_type;

		init();

		// set up our destroy callback
		self._watches = []
		self._watches.push($scope.$on("$destroy", destroy));
		self._watches.push($scope.$on(""));


		//////////////


		function init() {
			var user_id = $state.params.user_id,
				page = $state.params.page || 1,
				query = { user: user_id, page: page};

			self.loading = true;

			switch(self.list_type) {
				case 'original':
					query.retweeted_status__isnull = 'True';
					break;
				case 'media':
					query.media__isnull = 'False'
					break;
			}

			self.tweets = Tweet.get(query);

			self.tweets.$promise.then(function(data) {
				console.log("got tweets...");
				usSpinnerService.stop("tweet-list");

				$scope.page_data = data;
				self.tweets = data.results;
				self.loading = false;
			});			
		}

		function destroy() {
			// remove the watch
			for(var i=0; i < self._watches.length; i++) {
				self._watches[i]();
			}

			self._watches = [];
		}

	}

})();