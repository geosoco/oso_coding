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
				update: { method: 'PATCH'},
				delete: { method: 'DELETE'},
				save: { method: 'POST'},
				get: { method: 'GET'}
			};

	var tweetService = angular.extend({}, basicService, {
		query: {
			method: 'GET',
			transformResponse: transformTweetQueryResponse,
			isArray: true
		},
		get: {
			method: 'GET',
			transformResponse: transformTweetQueryResponse	
		}
	});

	var userService = angular.extend({}, basicService, {
		get: {
			method: 'GET',
			transformResponse: transformUserGetResponse
		}
	})

	/*
	 *
	 * common function for transforming results
	 * 
	 */
	function transformGetResponse(data) {
		var results = angular.fromJson(data);
		return results.results;
	}

	function transformTweetQueryResponse(data) {
		var results = angular.fromJson(data);

		for(var i=0; i < results.results.length; i++) {
			var t = results.results[i];

			t.created_ts = moment(t.created_ts).toDate();
			t.local_time = moment(t.local_time).toDate();
			t.user.created_ts = moment(t.created_ts).toDate();
			if(t.retweeted_status) {
				t.retweeted_status.created_ts = moment(t.retweeted_status.created_ts).toDate();
				t.retweeted_status.local_time = moment(t.retweeted_status.local_time).toDate();
				t.retweeted_status.user.created_ts = moment(t.retweeted_status.user.created_ts).toDate();
			}
		}

		return results;
	}

	function transformUserGetResponse(data) {
		var results = angular.fromJson(data);
		results.created_ts = moment(results.created_ts).toDate();

		return results;
	}

	services.factory("SysUser", SysUserService);
	services.factory("User", UserService);
	services.factory("Tweet", TweetService);
	services.factory("CodeScheme", CodeSchemeService);
	services.factory("UserCodeInstance", UserCodeInstanceService);
	services.factory("TweetCodeInstance", TweetCodeInstanceService);
	services.factory("Assignment", AssignmentService);

	function SysUserService($resource) {
		return $resource("/api/sysusers/:id/", {id: "@id"}, basicService );
	}

	function UserService($resource) {
		return $resource("/api/user/:id/", {id: "@id"}, userService );
	}

	function TweetService($resource) {
		return $resource("/api/tweet/:id/", {id: "@id"}, tweetService );
	}

	function CodeSchemeService($resource) {
		return $resource("/api/codescheme/:id/", {id: "@id"}, basicService );
	}

	function UserCodeInstanceService($resource) {
		return $resource("/api/usercodeinstance/:id/", {id: "@id"}, basicService );
	}

	function TweetCodeInstanceService($resource) {
		return $resource("/api/tweetcodeinstance/:id/", {id: "@id"}, basicService );
	}

	function AssignmentService($resource) {
		return $resource("/api/assignment/:id/", {id: "@id"}, basicService );
	}
})();