'use strict';

angular.module('moogitShows.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/home', {
    templateUrl: 'static/home/home.html',
    controller: 'homeCtrl'
  });
}])

.controller('homeCtrl', [ '$scope' ,function($scope) {
      $scope.title = "Scope Title";
      $scope.shows = [
        {
          venue: 'The Grand Delmar',
          bands: ['Apples', 'Oranges', 'Peaches'],
          price: 19,
          age: 18,
          date: new Date('2014', '03', '08', '20', '30'),
          comments: "Comments about the show at the Grand Delmar"
        },
        {
          venue: 'Radio Room',
          bands: ['Celery', 'Lettuce', 'Cabbage'],
          price: 19,
          age: 18,
          date: new Date('2014', '03', '08', '20', '30'),
          comments: "Comments about the show at Radio Room"
        }

      ];

}]);