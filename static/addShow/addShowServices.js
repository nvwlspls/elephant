/**
 * Created by waynejessen on 5/10/15.
 */

moogitShows.factory('matchbands', ['$http', function($http){
               return $http.get('/shows/matchbands/:matchbandstext')
                   .success(function(data){
                       return data;
                   })
                   .error(function(err){
                       return err;
                   })
                }
]);