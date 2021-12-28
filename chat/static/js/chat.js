function getParam(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}
function getComments(data){
  show_comments = ""
  for(let i = 0; i < data.comments.length; i++) {
          obj = data.comments[i]
          show_comments += "<div class='comment'>"
          show_comments += "  <div class='row'>"
          show_comments += "    <div class='name'>"+obj.author+"</div>"
          show_comments += "    <div class='time'>"+obj.created_at+"</div>"
          show_comments += "  </div>"
          show_comments += "  <h3 class='message'>"+obj.message+"</h3>"
          show_comments += "</div>"
  }
  if(data.comments.length == 0){
    show_comments += "<div class='comment'>まだメッセージがありません。</div>"
  }

  show_comments += "<div class='box'></div>"//余白用
  return (show_comments)
}
function initialize(){
  fetch('getLog?subject='+getParam('subject'))
      .then(response => {

        // (1) 通信が成功したか確認する
        if (!response.ok) {

          // (2) 通信に失敗したときはエラーを発生させる
          throw new Error('Not ok');
        }
        // (3) レスポンスデータからJSONデータを取得
        return response.json();
      })
      .then(data => {
        const list = document.getElementById('comments');
        document.getElementById('comments').innerHTML = getComments(data) ;
        
        //スクロールバーの位置をリストの最下部に設定
        list.scrollTo(0, list.scrollHeight);
      })
      .catch(error => {
        console.error(error);
      });
}
function load_data() {
  fetch('getLog?subject='+getParam('subject'))
      .then(response => {

        // (1) 通信が成功したか確認する
        if (!response.ok) {

          // (2) 通信に失敗したときはエラーを発生させる
          throw new Error('Not ok');
        }
        // (3) レスポンスデータからJSONデータを取得
        return response.json();
      })
      .then(data => {
        // console.log(data.tasks);
        const list = document.getElementById('comments');
        document.getElementById('comments').innerHTML = getComments(data) ;
          
      })
      .catch(error => {
        console.error(error);
      });
 
  setTimeout(function() {load_data()},1000);//todo websocketで必要なときだけデータを受け取る仕様に変更したい
}
function save_comments(){
  
  message = document.getElementById('message').value
  path = "?subject="+getParam('subject')+"&message="+message
  fetch(path)
      .then(response => {

        // (1) 通信が成功したか確認する
        if (!response.ok) {

          // (2) 通信に失敗したときはエラーを発生させる
          throw new Error('Not ok');
        }
        // (3) レスポンスデータからJSONデータを取得
        return response.json();
      })
      .then(data => {
        initialize()          
      })
      .catch(error => {
        console.error(error);
      });

}
function delete_all_comments(){
  
  
  path = "getLog?subject="+getParam('subject')+"&delete=all"
  alert(path)
  fetch(path)
      .then(response => {

        // (1) 通信が成功したか確認する
        if (!response.ok) {

          // (2) 通信に失敗したときはエラーを発生させる
          throw new Error('Not ok');
        }
        // (3) レスポンスデータからJSONデータを取得
        return response.json();
      })
      .then(data => {
        console.log(data);
        
      })
      .catch(error => {
        console.error(error);
      });
}
document.addEventListener
('DOMContentLoaded', function () { 
  initialize();
  setTimeout(function() {load_data()},1000);
})