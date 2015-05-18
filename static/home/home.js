'use strict';

angular.module('moogitShows.home', ['ngRoute',
                                    'ngResource','homeservice'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'static/home/home.html',
    controller: 'homeCtrl'
  })
  ;
}])

.controller('homeCtrl', function homeCtrl($scope, Shows) {

        $scope.shows = [];
        $scope.showLimit = 0;

        Shows.query( function(response){
            $scope.shows = response;
            $scope.showLimit+= 20;
            $scope.visShows= $scope.shows.slice(0, $scope.showLimit)
        });

        $scope.viewMore = function () {
            $scope.showLimit+=20;
        };


    })