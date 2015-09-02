(function() {
	var codingApp = angular.module('coding.app', ['ngAnimate', 'ui.router', 'coding.services', 'toastr' ]);

	/*
	 * set up app config (csrf )
	 */
	codingApp.config(
		['$resourceProvider', '$httpProvider', '$locationProvider', 
		 '$stateProvider', '$urlRouterProvider', 'toastrConfig',
			function(
				$resourceProvider, 
				$httpProvider, 
				$locationProvider, 
				$stateProvider, 
				$urlRouterProvider,
				toastrConfig) {

				$resourceProvider.defaults.stripTrailingSlashes = false;

				// csrf
				$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
				$httpProvider.defaults.xsrfCookieName = 'csrftoken';


				angular.extend(toastrConfig, {
					timeOut: 30000,
					tapToDismiss: true,
					maxOpened: 6,
				});

				// locprovider setup
				$locationProvider.html5Mode(false).hashPrefix('!');

				/*
				 * route setup
				 */
				$urlRouterProvider.otherwise("");

				$stateProvider
					.state(
						"code", {
							url: "/code/{assignment_id:int}/",
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
							url: "/{id:int}/",
							templateUrl: "/static/coding/html/assignment.detail.html",
							controller: "AssignmentController as assignment"
						})

			}
		]);


	codingApp.run(['$rootScope', '$state', '$stateParams', 'toastr', 'SysUser', 
		function($rootScope, $state, $stateParams, toastr, SysUser){
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


			var user = SysUser.get({'pk': "current"}).$promise.then(function(data){
				console.log(">>> got user")
				console.dir(data);
				if(data.results && data.results.length == 1) {
					$rootScope.sysuser = data.results[0];
					$rootScope.sysuserid = data.results[0].id;
					toastr.success('Logged in!', 'Success');
				} else {
					toastr.error('Could not get current user');
				}
			})


		}])

})();
