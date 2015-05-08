'use strict';

angular.module('moogitShows.addShow', ['ngRoute', "angucomplete-alt"])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/addShow', {
    templateUrl: 'static/addShow/addShow.html',
    controller: 'addShowCtrl'
  });
}])

.controller('addShowCtrl', ['$scope', function($scope) {
        $scope.bands = [
            {
                id : ''
            },{
                id :''
            },
            {
                id : ''
            }
        ]

        $scope.addNewBand = function() {
            $scope.bands.push({
                id :''
            })
        }

        $scope.removeBand = function(bandIndex) {
            $scope.bands.splice(bandIndex, 1)
        }


    }])