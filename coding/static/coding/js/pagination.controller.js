(function(){	
	'use strict';

	angular
		.module("coding.app")
		.controller("TweetPaginationController", TweetPaginationController);

	TweetPaginationController.$inject = ['$scope', '$stateParams', '$state', '$q'];


	function TweetPaginationController($scope, $stateParams, $state, $q) {
		var self = this;

		self.page_size = 20;
		self.max_pages = 10;

		self.disabled = true;
		self.pagelist = [];
		self.pagelist_min = -1;
		self.pagelist_max = -1;


		self.first_page = 0;
		self.last_page = 0;
		self.total_results = 0;
		self.current_page = $stateParams.page || 1;

		self.current_view = $state.current.name;

		self.next_page = null;
		self.prev_page = null;



		$scope.$watch("page_data", pageDataUpdated);


		function buildPageList() {
			var min_page = 0, max_page = 0;

			self.pagelist = [];

			if(self.total_results > 0) {
				if(self.total_results <= self.page_size) {
					min_page = 1;
					max_page = Math.ceil(self.total_results/self.page_size);
				} else {
					min_page = Math.max(self.current_page - 4, 1);
					max_page = Math.min(min_page + self.max_pages -1, self.last_page);
					if((max_page - min_page) + 1 < self.max_pages && min_page > 1) {
						min_page = Math.max(1, max_page - self.max_pages);
					}
				}

				self.pagelist_min = min_page;
				self.pagelist_max = max_page;
				for(var i=min_page; i <= max_page; i++) {
					self.pagelist.push({
						page: i
					})
				}
			} else {
				self.pagelist_min = 1;
				self.pagelist_max = 1;
			}
		}

		function pageDataUpdated(data) {
			self.disabled = true;

			self.first_page = 0;
			self.last_page = 0;
			self.total_results = 0;
			self.next_page = null;
			self.prev_page = null;

			if(data && data.results) {
				if(data.count) {
					self.total_results = data.count;
					self.first_page = 1;
					self.last_page = Math.ceil(data.count / self.page_size);
					
					self.next_page = Math.min( self.current_page + 1, self.last_page );
					self.prev_page = Math.max( self.current_page - 1, 1 );
				}
			}

			// update the page list
			buildPageList();
		}

	}

})();