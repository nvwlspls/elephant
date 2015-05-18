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

.controller('homeCtrl', [ '$scope', 'getshows', 'futureshows',
        function($scope, getshows, futureshows) {

            $scope.shows = [];
            $scope.futureshowslist = [];
            $scope.showsPage = 1;

            $scope.loadmore = function() {
                //var last = $scope.futureshowslist;
                //$scope.shows.push(last);
                $scope.shows = $scope.shows.concat($scope.futureshowslist)
                }

            futureshows.success(function (data) {
                    $scope.futureshowslist = data;
                    $scope.loadmore()
                }
            )

            getshows.success(function(data){
                $scope.futureshowslist = data;
                $scope.loadmore()
                $scope.futureshowslist = [];
            })




        }
    ]);


