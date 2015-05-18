/**
 * Created by waynejessen on 5/9/15.
 */

angular.module('homeservice', ['ngResource'])
    .factory('Shows', function ($resource) {
        return $resource('shows/getfutureshows/:page');
    })
