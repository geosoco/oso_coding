(function() {
	'use strict';

	angular
		.module("coding.app")
		.controller("UserCodingController", UserCodingController);

	UserCodingController.$inject = ['$rootScope', '$scope', '$state', '$stateParams',
		'User',  'usSpinnerService', 'toastr'];


	function UserCodingController($rootScope, $scope, $state, $stateParams, 
		User, usSpinnerService, toastr ) {
			var self = this;


			init();

			
			///////////////


			function init() {
				$rootScope.coding_user_id = $stateParams.user_id;


				$rootScope.coding_user = User.get({id: $stateParams.user_id});

				$rootScope.coding_user.$promise.then(
					function(data){	// success
						usSpinnerService.stop("user-details");
						//angular.extend(self, data);
						self.user = data;
					}, 
					function(error){ // error
						console.error(error);
					});

				self.user_href = $state.href("user.tweets", $state.params, "absolute");

				// save the state params
				self.state_params = angular.extend({}, $state.params);
			}


			self.copyUserLink = function() {
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
