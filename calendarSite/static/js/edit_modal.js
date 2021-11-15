   // ボタン、モダル、モダルの閉じるボタン、オーバーレイを変数に格納
   const edit_btn = document.querySelector('.edit_btn');
   const edit_modal = document.querySelector('.edit_modal');
   const edit_closeBtn = document.querySelector('.edit_close');
   const edit_overlay = document.querySelector('.edit_overlay');
   
  
   
   // モダルの閉じるボタンをクリックしたら、モダルとオーバーレイのactiveクラスを外す
   edit_closeBtn.addEventListener('click', function(){
     edit_modal.classList.remove('active');
     edit_overlay.classList.remove('active');
   });
   
   // オーバーレイをクリックしたら、モダルとオーバーレイのactiveクラスを外す
   edit_overlay.addEventListener('click', function() {
     edit_modal.classList.remove('active');
     edit_overlay.classList.remove('active');
   });