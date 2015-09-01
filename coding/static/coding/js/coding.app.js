(function() {
	var codingApp = angular.module('coding.app', ['ui.router', 'coding.services' ]);

	/*
	 * set up app config (csrf )
	 */
	codingApp.config(
		['$resourceProvider', '$httpProvider', '$locationProvider', '$stateProvider', '$urlRouterProvider', 
			function($resourceProvider, $httpProvider, $locationProvider, $stateProvider, $urlRouterProvider) {
				$resourceProvider.defaults.stripTrailingSlashes = false;

				// csrf
				$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
				$httpProvider.defaults.xsrfCookieName = 'csrftoken';

				// locprovider setup
				$locationProvider.html5Mode(false).hashPrefix('!');


				/*
				 * route setup
				 */
				$urlRouterProvider.otherwise("");

				$stateProvider
					.state(
						"code", {
							url: "/code/",
							templateUrl: "static/coding/html/code.html",
							controller: "CodingController"									
						})
					.state(
						"code.user", {
							url: "user/{id:int}/",
							"views": {
								"sidebar": {
									templateUrl: "static/coding/html/code.sidebar.html",
									controller: function($scope) {
										console.log("----sidebar")
									}
								},
								"main-content": {
									templateUrl: "static/coding/html/code.user.html",
									controller: "UserCodingController as user"
								}
							}
						})
					.state(
						"assignment", {
							url: "/{id:int}",
							templateUrl: "/static/coding/html/assignment.detail.html",
							controller: "AssignmentController as assignment"
						})

			}
		]);


	codingApp.run(['$rootScope', '$state', '$stateParams', 
		function($rootScope, $state, $stateParams){
			$rootScope.$state = $state;
			$rootScope.$stateParams = $stateParams;

			$rootScope.$on("$stateChangeStart", 
				function(event, toState, toParams, fromState, fromParams) {
					console.log("stateChangeStart");
					console.dir(event);
					console.dir(toState);
				});

			$rootScope.$on("$stateChangeError",
				function(event, toState, toParams, fromState, fromParams) {
					console.log("stateChangeError");
				});

			$rootScope.$on("$stateNotFound",
				function(event, unfoundState, fromState, fromParams){
					console.log("stateNotFound");
				})

		}])

})();
