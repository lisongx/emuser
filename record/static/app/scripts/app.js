'use strict';

var app = angular.module('emuserApp', ['emuserApp.directives', 'emuserApp.services']);
app.config(function ($routeProvider) {
	$routeProvider
	.when('/', {
		controller: 'ResumeCtrl',
		resolve: {
			records: function(MultiRecordsLoader) {
				return MultiRecordsLoader();
			},
			user: function(UserLoader) {
				return UserLoader();
			}
		},
		templateUrl: 'views/resume.html'
	})
	.otherwise({
		redirectTo: '/'
	});
});
