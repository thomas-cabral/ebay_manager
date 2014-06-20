/**
 * Created by Thomas on 6/5/2014.
 */
var managerApp = angular.module('managerApp', ['ngRoute', 'ngResource', 'ngAnimate', 'djangoRESTResources', 'ngCookies']);

managerApp.config(function($routeProvider, $locationProvider, $httpProvider) {
    $routeProvider

    // Index
        .when('/', {
            templateUrl : '/angular_index/',
            controller : 'ItemListCtrl'
        })

        .when('/new', {
            templateUrl : '/angular_new/',
            controller : 'ItemCreationCtrl'
        })

        .when('/:id', {
            templateUrl : '/angular_detail/',
            controller : 'ItemDetailCtrl'
        })

        .when('/:id/edit', {
            templateUrl : '/angular_edit',
            controller : 'ItemDetailCtrl'
        });

    //$locationProvider.html5Mode(true);
    //$httpProvider.provider.defaults.headers.post["X-CSRFToken"] = getCookie('csrftoken');
});

managerApp.run( function run($http, $cookies ){

    // For CSRF token compatibility with Django
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

managerApp.factory('ItemsFactory', function (djResource) {
    return djResource('/api/items/', {}, {
        query: { method: 'GET', isArray: true },
        create: { method: 'POST' }
    })
});

managerApp.factory('ItemFactory', function ($resource) {
    return $resource('/api/item/:id/', {}, {
        show: { method: 'GET' },
        update: { method: 'PUT', params: {id: '@id'} },
        delete: { method: 'DELETE', params: {id: '@id'} }
    })
});

managerApp.controller('ItemDetailCtrl', ['$scope', '$routeParams', 'ItemFactory', '$location',
    function ($scope, $routeParams, ItemFactory, $location) {

        // callback for ng-click 'updateItem':
        $scope.save = function () {
            ItemFactory.update($scope.item);
            $location.path('/');
        };

        // callback for ng-click 'cancel':
        $scope.cancel = function () {
            $location.path('/');
        };

        $scope.destroy = function () {
            ItemFactory.delete($scope.item);
            $location.path('/');
        };

        $scope.item = ItemFactory.show({id: $routeParams.id});
    }
]);

managerApp.controller('ItemCreationCtrl', ['$scope', 'ItemsFactory', '$location',
    function ($scope, ItemsFactory, $location) {

        // callback for ng-click 'createNewItem':
        $scope.createNewItem = function () {
            ItemsFactory.create($scope.item);
            $location.path('/');
        }
    }]);

managerApp.controller('ItemListCtrl', ['$scope', 'ItemsFactory',
    function ($scope, ItemsFactory) {

        $scope.items = ItemsFactory.query();

    }]);