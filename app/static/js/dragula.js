(function($) {
    'use strict';
    var iconTochange;
   
    dragula([document.getElementById("profile-list-all1"), document.getElementById("profile-list-subj1")], {

        removeOnSpill: true,
         
       
        
      });
      dragula([document.getElementById("profile-list-all2"), document.getElementById("profile-list-subj2")], {
        copy: function (el, source) {
          return source === document.getElementById("profile-list-all2")
        },
        removeOnSpill: true,
         verify: function(el,target)
         {
           if(global > 0)
           {
            return removeOnSpill = false
          }

         }, 
       
        accepts: function (el, target) {
          return target !== document.getElementById("profile-list-all2")
        }
      });
      dragula([document.getElementById("profile-list-all3"), document.getElementById("profile-list-subj3")], {
        copy: function (el, source) {
          return source === document.getElementById("profile-list-all3")
        },
        removeOnSpill: true,
         verify: function(el,target)
         {
           if(global > 0)
           {
            return removeOnSpill = false
          }

         }, 
       
        accepts: function (el, target) {
          return target !== document.getElementById("profile-list-all3")
        }
      });
  

})(jQuery);

