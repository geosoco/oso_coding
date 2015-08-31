(function() {
	var codingApp = angular.module('coding.app', ['coding.services' ]);

	/*
	 * set up app config (csrf )
	 */
	codingApp.config(
		['$resourceProvider', '$httpProvider', '$locationProvider', 
			function($resourceProvider, $httpProvider, $locationProvider) {
				$resourceProvider.defaults.stripTrailingSlashes = false;

				$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
				$httpProvider.defaults.xsrfCookieName = 'csrftoken';

				$locationProvider.html5Mode(false).hashPrefix('!');
			}
		]);	

})();
