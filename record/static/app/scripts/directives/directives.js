'use strict';

var directives = angular.module('emuserApp.directives', []);

directives.directive('waiting', ['$rootScope', function($rootScope) {
	return {
		link: function(scope, element, attrs) {
			element.addClass('hide');

			$rootScope.$on('$routeChangeStart', function() {
				element.removeClass('hide');
			});

			$rootScope.$on('$routeChangeSuccess', function() {
				element.addClass('hide');
			});
		}
	};
}]);

directives.directive('focus', function() {
	return {
		link: function(scope, element, attrs) {
			element[0].focus();
		}
	};
});

directives.directive('bounce', ['$rootScope', function($rootScope) {
	return {
		link: function(scope, element, attrs) {
			element.bind("mouseover", function(){
				element.addClass('animated bounceOutLeft');
			})
		}
	};
}]);


directives.directive('piechart', ['$rootScope', function($rootScope) {
	return {
		restrict: 'E',
        template: '<canvas width="200" height="200"></canvas>',
		replace: true,
		link: function(scope, element, attrs) {
			var codeschool = scope.codeschool;
			var codecademy = scope.codecademy;
			var coursera = scope.coursera;

			var pieData = [{
					value: codeschool.length,
					color:"#F38630"
				},
				{
					value : codecademy.length,
					color : "#E0E4CC"
				},
				{
					value : codecademy.length,
					color : "#69D2E7"
				}
				]
			var ctx = element[0].getContext("2d");
			new Chart(ctx).Pie(pieData);

		}
	};
}]);

directives.directive('barchart', ['$rootScope', function($rootScope) {
	return {
		restrict: 'E',
        template: '<canvas width="500" height="200"></canvas>',
		replace: true,
		link: function(scope, element, attrs) {
			console.log(scope);
			var codeschool = scope.codeschool.length;
			var codecademy = scope.codecademy.length;
			var coursera = scope.coursera.length;
			var barData = {
				labels : ["Coursera", "CodeSchool", "Codecademy"],

				datasets : [
					{
						fillColor : "rgba(220,220,220,0.5)",
						strokeColor : "rgba(220,220,220,1)",
						data : [codeschool,codecademy, coursera]
					}
				]
			}
			var ctx = element[0].getContext("2d");
			new Chart(ctx).Bar(barData);

		}
	};
}]);

