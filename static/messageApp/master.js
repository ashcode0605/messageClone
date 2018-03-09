(function() {

  students = ['Ashwani Singh','Amit Kumar','Suraj','Aniket'];

  angular.module('myApp',[])
  .controller('myAppController',function ($scope) {
    $scope.students = students;
  })
})();
