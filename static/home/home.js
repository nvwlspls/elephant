'use strict';

angular.module('moogitShows.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'static/home/home.html',
    controller: 'homeCtrl'
  });
}])

.controller('homeCtrl', [ '$scope', 'getshows' ,function($scope, getshows) {
      $scope.title = "Scope Title";

        getshows.success(function(data){
            $scope.shows = data;
        })
}]);