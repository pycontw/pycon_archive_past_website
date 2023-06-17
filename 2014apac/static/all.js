// Generated by CoffeeScript 1.8.0
(function() {
  var App;

  App = angular.module('App', ['ngAnimate', 'ngCookies']);

  App.config(function($httpProvider) {
    return $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  });

  App.controller('base', function($rootScope, $scope) {
    $rootScope.slidePageUrl = '';
    $rootScope.closePage = function(event) {
      if ($rootScope.slidePageUrl === '') {
        return;
      }
      $rootScope.slidePageUrl = '';
    };
    $scope.btnNavText = function() {
      if ($scope.showNav) {
        return '✕';
      } else {
        return 'N';
      }
    };
    $scope.$on('$includeContentRequested', function() {
      return $scope.loading = true;
    });
    return $scope.$on('$includeContentLoaded', function() {
      return $scope.loading = false;
    });
  });

  App.controller('Program', function($scope) {
    $scope.em = null;
    $scope.day = null;
    $scope.checkEm = function(time) {
      return $scope.em === time || $scope.em === null;
    };
    return $scope.checkDay = function(day) {
      return $scope.day === day || $scope.day === null;
    };
  });

  App.directive('turbolink', function($http, $rootScope, $document) {
    return {
      restrict: 'A',
      scope: false,
      link: function(scope, element, attrs) {
        element.on('click', function(event) {
          event.preventDefault();
          if ($rootScope.slidePageUrl === '') {
            event.stopPropagation();
          }
          if ($rootScope.slidePageUrl !== '') {
            return;
          }
          return scope.$apply(function() {
            return $rootScope.slidePageUrl = attrs.href;
          });
        });
      }
    };
  });

  App.directive('foldList', function($cookieStore) {
    return {
      restrict: 'A',
      scope: false,
      link: function(scope, element, attrs) {
        var fold, foldIcon, foldSet, id, isFold, li, unfold;
        li = element.find('li');
        if (li.length === 0) {
          return;
        }
        foldSet = $cookieStore.get('foldSet') || {};
        id = attrs.foldList;
        isFold = foldSet[id];
        foldIcon = angular.element('<fold>▾</fold>');
        element.append(foldIcon);
        fold = function() {
          element.addClass('fold');
          return foldIcon.text('▸');
        };
        unfold = function() {
          element.removeClass('fold');
          return foldIcon.text('▾');
        };
        if (isFold) {
          fold();
        }
        element.find('fold').on('click', function() {
          isFold = !isFold;
          foldSet[id] = isFold;
          if (isFold) {
            fold();
          } else {
            unfold();
          }
          scope.$apply(function() {
            return $cookieStore.put('foldSet', foldSet);
          });
        });
      }
    };
  });

}).call(this);