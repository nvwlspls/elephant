'use strict';

// Declare app level module which depends on views, and components
var moogitShows = angular.module('moogitShows', [
      'ngRoute',
      'moogitShows.home',
      'moogitShows.addShow',
      'moogitShows.version',
      'angucomplete-alt'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.otherwise({redirectTo: '/home'});
}]);
