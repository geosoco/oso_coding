(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserDetailController", UserDetailController);

	UserDetailController.$inject = ['$scope', '$state', '$stateParams', 'User', 'Tweet', 'usSpinnerService', 'toastr'];


	function UserDetailController($scope, $state, $stateParams, User, Tweet, usSpinnerService, toastr ) {
			var self = this;

			console.log("user detail controller");
			console.dir($stateParams);

			init();
			
			///////////////


			function init() {
				// request user
				self.user = User.get({id: $stateParams.user_id });

				// handle promise
				self.user.$promise.then(function(data){
					console.log("loaded user data");
					console.dir(data);
				}, function(error) {
					if(error.status === 404) {
						toastr.error("User does not exist in local database");
					} else {
						toastr.error("Unexpected error from server");
					}
					
				});

				// copy state params
				self.state_params = angular.extend({}, $state.params);
			}


			self.copyUserLink = function() {
				// modified from a google blog
				var link = document.querySelector(".user-share-profile-link"),
					range = document.createRange();

				range.selectNode(link);
                window.getSelection().removeAllRanges();
				window.getSelection().addRange(range);

				try {
					var successful = document.execCommand("copy");

					if(successful) {
						toastr.success("User link copied!");
					} else {
						toastr.error("Couldn't copy user link.");
					}
					
				} catch(err) {
					toastr.error("Couldn't copy profile link (" + err + ")")
				}

				window.getSelection().removeAllRanges();
			}			
		}

})();
