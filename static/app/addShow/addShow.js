'use strict';

angular.module('moogitShows.addShow', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/addShow', {
    templateUrl: 'addShow/addShow.html',
    controller: 'addShowCtrl'
  });
}])

.controller('addShowCtrl', [function() {

}]);