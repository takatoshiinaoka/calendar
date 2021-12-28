function getParam(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}
var sort = false
function answersort(){
  sort = true
}
function newsort(){
  sort = false
}
function initialize() {
  str = "";
  show_comments = ""
  path = 'getQuestion?subject='+getParam('subject')
  if(sort){
    path += '&sort=""'
  }

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
        // console.log(data.tasks);
        
        for(let i = 0; i < data.questions.length; i++) {
          obj = data.questions[i]
          show_comments += obj.resolved ? "<div class='comment solvedQuestion'>":"<div class='comment unsolvedQuestion'>"
          show_comments += "<h2>回答数："+obj.answerNum+"</h2>"
          show_comments += "<h2 id="+obj.id+">"+obj.author+":"+obj.message+"</h2>"+
          "<p>"+obj.created_at+"</p>"
          +"<a class='buttonDetail' href=create_answer?question="+obj.id+"></a> "
          show_comments += data.myquestions.includes(obj.id) ? "<a class='buttonSolved' href='create_question?solved="+obj.id+"&subject="+getParam('subject')+"'>解決済みにする</a> ":" "
          show_comments += obj.resolved ? "解決済み":""
          show_comments += "</div>"
        }
        
        const list = document.getElementById('questions');
        list.innerHTML = show_comments ;
        // list.scrollTo(0, list.scrollHeight);
      })
      .catch(error => {
        console.error(error);
      });
  

}
function load_data() {
  str = "";
  show_comments = ""
  path = 'getQuestion?subject='+getParam('subject')
  if(sort){
    path += '&sort=""'
  }
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
        // console.log(data.tasks);
        
        for(let i = 0; i < data.questions.length; i++) {
          obj = data.questions[i]
          show_comments += obj.resolved ? "<div class='comment solvedQuestion'>":"<div class='comment unsolvedQuestion'>"
          show_comments += "<h2>回答数："+obj.answerNum+"</h2>"
          show_comments += "<h2 id="+obj.id+">"+obj.author+":"+obj.message+"</h2>"+
          "<p>"+obj.created_at+"</p>"
          +"<a class='buttonDetail' href=create_answer?question="+obj.id+"></a> "
          show_comments += data.myquestions.includes(obj.id) ? "<a class='buttonSolved' href='create_question?solved="+obj.id+"&subject="+getParam('subject')+"'>解決済みにする</a> ":" "
          show_comments += obj.resolved ? "解決済み":""
          show_comments += "</div>"
        }
        console.log(show_comments)
        const list = document.getElementById('questions');
        list.innerHTML = show_comments ;
      })
      .catch(error => {
        console.error(error);
      });
  

  setTimeout(function() {load_data()},1000);//todo websocketで必要なときだけデータを受け取る仕様に変更したい
}
function save_question(){
  
  message = document.getElementById('message').value
  path = "create_question?subject="+getParam('subject')+"&message="+message
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
        initialize();
        
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
      setTimeout(function() {load_data()},1000);//todo websocketで必要なときだけデータを受け取る仕様に変更したい
})