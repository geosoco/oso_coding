(function() {
	var services = angular.module('coding.services', ['ngResource']);

	/*
	 * basic service
	 */
	var basicService = {
				query: { 
					method: 'GET',
					transformResponse: transformGetResponse,
					isArray: true
				},
				update: { method: 'PUT'}
			};

	/*
	 *
	 * common function for transforming results
	 * 
	 */
	function transformGetResponse(data) {
		var results = angular.fromJson(data);
		return results.results;
	}


	services.factory("User", UserService);
	services.factory("Tweet", TweetService);
	services.factory("CodeScheme", CodeSchemeService);
	services.factory("UserCodeInstance", UserCodeInstanceService);
	services.factory("TweetCodeInstance", TweetCodeInstanceService);



	function UserService($resource) {
		return $resource("/api/user/:id", {id: "@id"}, basicService );
	}

	function TweetService($resource) {
		return $resource("/api/tweet/:id", {id: "@id"}, basicService );
	}

	function CodeSchemeService($resource) {
		return $resource("/api/codescheme/:id", {id: "@id"}, basicService );
	}

	function UserCodeInstanceService($resource) {
		return $resource("/api/usercodeinstance/:id", {id: "@id"}, basicService );
	}

	function TweetCodeInstanceService($resource) {
		return $resource("/api/tweetcodeinstance/:id", {id: "@id"}, basicService );
	}

})();