$(document).ready(function(){
  $(" .registerb").click(function(){
    $("#register").show(500);
     $("#login").hide(500); 
  });
  $(" .loginb").click(function(){
    $("#login").show(500);
    $("#register").hide(500);
  });
});
