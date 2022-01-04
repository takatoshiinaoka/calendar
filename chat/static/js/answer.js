function getParam(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}
  function initialize() {
    str = "";
    show_comments = ""
    fetch('getAnswer?question='+getParam('question'))
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
          
          for(let i = 0; i < data.answers.length; i++) {
            obj = data.answers[i]
            show_comments += "<div class='comment'>"
            show_comments += "<h2>"+obj.author+":"+obj.message+"</h2>"+
            "<p>"+obj.created_at+"</p>"+
            "<a href='create_answer?good="+obj.id+"&question="+getParam('question')+"'>いいね！"+obj.good_count+"</a>"+
            data.done.includes(obj.id)
            show_comments += "</div>"
          }
          if(data.answers.length == 0){
            show_comments += "<div class='comment'>まだメッセージがありません。</div>"
          }
          const list = document.getElementById('questions');
          list.innerHTML = show_comments ;
          list.scrollTo(0, list.scrollHeight);
        })
        .catch(error => {
          console.error(error);
        });
    
  }
  function load_data() {
    str = "";
    show_comments = ""
    fetch('getAnswer?question='+getParam('question'))
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
          
          for(let i = 0; i < data.answers.length; i++) {
            obj = data.answers[i]
            show_comments += "<div class='comment'>"
            show_comments += "<h2>"+obj.author+":"+obj.message+"</h2>"+
            "<p>"+obj.created_at+"</p>"+
            "<a href='create_answer?good="+obj.id+"&question="+getParam('question')+"'>いいね！"+obj.good_count+"</a>"+
            data.done.includes(obj.id)
            show_comments += "</div>"

          }
          if(data.answers.length == 0){
            show_comments += "<div class='comment'>まだメッセージがありません。</div>"
          }
          const list = document.getElementById('questions');
          var isScroll = false;//最後までスクロールされたか
          if(list.scrollHeight  -  list.scrollTop <= list.clientHeight){//判定にはデータ更新前の情報を使いたいので一度変数に格納
            isScroll = true
          }
          list.innerHTML = show_comments;
          if(isScroll){
            list.scrollTo(0, list.scrollHeight);
          }          
        })
        .catch(error => {
          console.error(error);
        });
    

    setTimeout(function() {load_data()},1000);//todo websocketで必要なときだけデータを受け取る仕様に変更したい
  }
  function save_answer(){
    
    message = document.getElementById('message').value
    path = "create_answer?question="+getParam('question')+"&message="+message
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
          load_data()
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