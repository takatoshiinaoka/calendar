# calendar

サイトにアクセス[pblsrv.cs.fit.ac.jp:18000/](http://pblsrv.cs.fit.ac.jp:18000/)

# 環境

- python                    :3.7.9                
- django                    :3.1.2                        
- django-allauth            :0.47.0   
- markdown                  :3.2.2                   


## 1. はじめに
今回は2021年クラウドアプリ開発入門講座を受講し，独自のアプリ開発をすることになった．その報告会に向けた成果物として今回のカレンダープロジェクトを行っていく．
しかし，クラウドアプリ開発の期間では完成させることができなかったため，プロジェクト型演習でその続きを行っていく．
* 全員すること
    * [クラウドアプリ開発講座2021の開発環境をダウンロードする](Document/make_env.md)
    * githubアカウントを作る
    * gitのインストールする
* リポジトリ作る人がすること
    * [キャッシュファイル読み込み無効化](https://note.com/masato1230/n/na63ac4e7ccdd)
    * [キャッシュの削除](https://qiita.com/fuwamaki/items/3ed021163e50beab7154)


## 2. 自分のリポジトリにフォークする
右上の **Folk** から **自分のリポジトリにフォーク** してください．それをクローンしてください．


## 3. ローカルにリポジトリを保存する(cloneする)
コマンドプロンプトを開く．以下のコマンドを実行し，リポジトリをクローンしたいディレクトリに移動する．(1の開発環境以外の場所にある場合は各自で変更お願いします)
    
    cd C://Django/vscode/Workspace
 
リポジトリをクローンする．(URLは各自で変更してください)

    git clone https://github.com/自分のGithub_id/calendar.git
    
## 4.VScodeの開き方
1. **C://Django/vscode/VisualStudioCode.bat** ファイルをクリック。すると、VSCodeが開く!(batファイルから開かないと，5.のactivate envができません．)

2. ファイル → Open Folder → vscode/Workspace/calendarを選択。
3. ターミナルを開き、「powershell」になっている人は、「cmd」に変更！
4. 「cmd」になっている事を確認したら、activate envのコマンドを打つ!      

        activate env



6. django-alauthをインストールしていなければ、以下のコマンドを打つ

        pip install django-allauth

7. 以下のコマンドを打ちサーバを立ち上げる!

        python manage.py runserver
        
8. localhostにアクセスする
Cancel changes
    [localhost:8000](http://localhost:8000/)　　　
    ※サーバーを閉じるときは「Ctrlキー + C」

    


## 5. pushするために必要な作業(VScodeのターミナルで実行する)
1.Githubのアカウント　(VSCodeのターミナル)  
例：git config --global user.name "takathosiinaoka"

    git config --global user.name "Githubアカウント名"  　 


2.メールアドレス(VSCodeのターミナル)  
例：git config --global user.email heavenhayao2316@gmail.com  

    git config --global user.email メールアドレス

## 6.編集履歴の表示(TortoiseGit or Gitlog)
エクスプローラーで緑のチェックが入ったフォルダを右クリックし、「TortoiseGit」の「ログを表示」より閲覧できる。  
また、VSCodeのターミナルで確認することもできる。以下のコードより確認できる。Enterキーを押すと過去のログが参照できる。「q」キーで終了する。


    git log
   
## 7.フォークしたリポジトリを最新化する
[フォークしたリポジトリを最新化する方法](https://qiita.com/Nossa/items/ace2ab802adc85f86b20)


1.GitHubのフォーク元のリポジトリをリモートブランチに追加する

    git remote add upstream https://github.com/takatoshiinaoka/calendar.git

2.フォーク元のmainブランチの変更差分を持ってくる

    git fetch upstream

3.mainブランチに移動し，フォーク元の差分をマージする

    git merge upstream/main

4 **DBファイル**「db.sqlite3」と **マイグレーションファイル** 「000X~」の削除
         
5.マイグレーションファイルの作成

    python manage.py makemigrations

6.DBの作成
   
    python manage.py migrate
    
7.ブランチ更新

      git pull origin main

## 8. 編集
担当になった機能を実装します．変更したら，自分のリモートリポジトリにプッシュします．

## 9.プルリクエスト
自分の担当の機能が完成したら，Githubからプルリクエストをします．

**自分のリポジトリのメインブランチ** → **稲岡のリポジトリのメインブランチ**

となるようにしてください．

  

  
   

   
   
