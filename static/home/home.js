'use strict';

angular.module('moogitShows.home', ['ngRoute',
                                    'infinite-scroll'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'static/home/home.html',
    controller: 'homeCtrl'
  })
  ;
}])

.controller('homeCtrl', [ '$scope', 'getshows', function($scope, getshows) {

        $scope.shows = new Shows();

}]);


