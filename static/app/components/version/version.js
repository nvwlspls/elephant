'use strict';

angular.module('moogitShows.version', [
  'moogitShows.version.interpolate-filter',
  'moogitShows.version.version-directive'
])

.value('version', '0.1');
