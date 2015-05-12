/**
 * Created by waynejessen on 5/9/15.
 */

//moogitShows.factory('getshows', [ '$http', function($http) {
//
//
//
//            return $http.get("/shows/getshows/9")
//                .success(function(data) {
//                    return data;
//                })
//                .error(function(err) {
//                    return err;
//                })
//        }
//]);


moogitShows.factory('getshows', function($http){

    var Getshows = function(){
        this.items = function[];
        this.busy = false;
        this.after = '';
    }

    Getshows.prototype.nextPage = function(){
        if (this.busy) return;
        this.busy = true;
        var url = "/shows/getshows" + this.after
    }
})