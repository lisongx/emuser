'use strict';

var app = angular.module('emuserApp');

app.controller('ResumeCtrl', function ($scope, records, user) {
	$scope.codeschool = records[0].codeschool;
	$scope.codecademy = records[0].codecademy;
	$scope.coursera = records[0].coursera;

	$scope.user = user;


});
