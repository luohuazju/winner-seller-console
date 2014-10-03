'use strict';

/**
 * @ngdoc function
 * @name userConsoleApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the userConsoleApp
 */
angular.module('userConsoleApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
