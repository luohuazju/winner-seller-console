'use strict';

/**
 * @ngdoc function
 * @name userConsoleApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the userConsoleApp
 */
angular.module('userConsoleApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
