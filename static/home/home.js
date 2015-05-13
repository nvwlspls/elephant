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

        $scope.shows = []

        futureshows.success(function(data){
            $scope.futureshows = data;
        })



            
        //$scope.loadmore = function(){
        //    var last = $scope.futureshows;
        //    for(var i =1; i <=10; i++){
        //        $scope.shows.push(last + 1);
        //    }
        //}
}]);


