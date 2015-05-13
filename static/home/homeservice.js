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
        this.items = [];
        this.busy = false;
        this.after = '1';
    };

    Getshows.prototype.nextPage = function(){
        if (this.busy) return;
        this.busy = true;
        var url = "/shows/getshows/" + this.after

        $http.get(url).success(function(data){
            var items = data.children;
            for (var i = 0; i < items.length; i++){
                 this.items.push(items[i], data);
            }
            this.after += 1;
            this.busy = false;
        }.bind(this));
        };

    return Getshows;
})

moogitShows.factory('futureshows', function($http){

    return $http.get("/shows/getfutureshows/")
                .success(function(data){
                    return data
                })
                .error(function (err) {
                        return err
                    })
        })