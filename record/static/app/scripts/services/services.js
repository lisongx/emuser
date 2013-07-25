'use strict';

var services = angular.module('emuserApp.services', ['ngResource']);

services.factory('Record', ['$resource', function($resource) {
	//return $resource('/resume/:id', {id: '@id'});
	return $resource('2');
}]);

services.factory('User', ['$resource', function($resource) {
	return $resource('../user');
}]);


services.factory('MultiRecordsLoader', ['Record', '$q', function(Record, $q) {
	return function() {
		var delay = $q.defer();
		Record.query(function(records) {
			delay.resolve(records);
			console.log(records);
		}, function() {
			delay.reject('Unable to fetch records.Douwork is too slow!!');
		});
		return delay.promise;
	};
}]);


services.factory('RecordLoader', ['Record', '$route', '$q', function(Record, $route, $q) {
	 return function() {
		 var delay = $q.defer();
		 Record.get({id: $route.current.params.recordId}, function(record) {
			 delay.resolve(record);
		 }, function() {
			 delay.reject('Unable to fetch record '  + $route.current.params.recordId);
		 });
		 return delay.promise;
	 };
 }]);

services.factory('UserLoader', ['User', '$route', '$q', function(User, $route, $q) {
	 return function() {
		 var delay = $q.defer();
		 User.get({id: $route.current.params.userId}, function(user) {
			 delay.resolve(user);
		 }, function() {
			 delay.reject('Unable to fetch record '  + $route.current.params.userId);
		 });
		 return delay.promise;
	 };
 }]);
