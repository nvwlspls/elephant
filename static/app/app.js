'use strict';

// Declare app level module which depends on views, and components
var moogitShows = angular.module('moogitShows', [
  'ngRoute',
  'moogitShows.home',
  'moogitShows.addShow',
  'moogitShows.version'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/home'});
}]);
