/**
 * Created by waynejessen on 5/9/15.
 */

moogitShows.factory('getshows', ['$http', function($http){
               return $http.get('/shows/getshows')
                   .success(function(data){
                       return data;
                   })
                   .error(function(err){
                       return err;
                   })
                }
]);