(function() {
	var codingApp = angular.module('coding.app', ['ngAnimate', 'ui.router', 'coding.services', 
		'toastr', 'angularSpinner', 'angularMoment' ]);

	/*
	 * set up app config (csrf )
	 */
	codingApp.config(
		['$resourceProvider', '$httpProvider', '$locationProvider', 
		 '$stateProvider', '$urlRouterProvider', 'toastrConfig', 'usSpinnerConfigProvider', 
			function(
				$resourceProvider, 
				$httpProvider, 
				$locationProvider, 
				$stateProvider, 
				$urlRouterProvider,
				toastrConfig, 
				usSpinnerConfigProvider) {

				$resourceProvider.defaults.stripTrailingSlashes = false;

				// csrf
				$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
				$httpProvider.defaults.xsrfCookieName = 'csrftoken';


				angular.extend(toastrConfig, {
					timeOut: 5000,
					tapToDismiss: true,
					maxOpened: 6,
					closeButton: true
				});

				// spinner
				usSpinnerConfigProvider.setDefaults({width: 3, radius: 8, length: 6});

				// locprovider setup
				$locationProvider.html5Mode(false).hashPrefix('!');

				/*
				 * route setup
				 */
				$urlRouterProvider.otherwise("");

				$stateProvider
					.state(
						"code", {
							url: "/code/{assignment_id:int}",
							templateUrl: "static/coding/html/code.html",
							controller: "CodingController"				
						})
					.state(
						"code.user", {
							url: "/user/{user_id:int}",
							abstract: true,							
							views: {
								"sidebar": {
									templateUrl: "static/coding/html/code.sidebar.html"
								},
								"main-content": {
									templateUrl: "static/coding/html/code.user.html",
									controller: "UserCodingController as user",
								}
							}
						})
					.state(
						"code.user.tweets", {
							url: "/{list_type}/{page:int}",
							params: {
								list_type : {
									value: "tweets"
								},
								page: {
									value: 1
								}
							},
							views: {
								"tweet-list": {
									templateUrl: "static/coding/html/user.tweetlist.html",
									controller: "TweetListController as tweetlist"
								}
							}
						})
					.state(
						"assignment", {
							url: "/{assignment_id:int}/",
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
					console.log("!!! stateChangeStart: " + fromState.name + " -> " + toState.name);
					console.dir(event);
					console.dir(toState);
				});

			$rootScope.$on("$stateChangeError",
				function(event, toState, toParams, fromState, fromParams) {
					console.log("!!! stateChangeError");
				});

			$rootScope.$on("$stateNotFound",
				function(event, unfoundState, fromState, fromParams){
					console.log("!!! stateNotFound");
				})


			var user = SysUser.get({'current_user': "True"}).$promise.then(function(data){
				console.log("got user")
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
