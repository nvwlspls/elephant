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

        futureshows.success(function(data){
           //$scope.shows =  $scope.shows.concat(data)
            $scope.futureshows = data;

            $scope.loadmore = function (){
                var last =  $scope.futureshows[$scope.futureshows.length -1 ];
                console.log("apples")
                $scope.shows.push(last)
                console.log($scope.loadmore())
                console.log(last)
            }

        })

}]);


