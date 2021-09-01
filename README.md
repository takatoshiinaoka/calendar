# calender 環境設定の手順

## 1. はじめに
- [キャッシュファイル読み込み無効化](https://note.com/masato1230/n/na63ac4e7ccdd)
* githubアカウントを作る。
* gitのインストールする。

## 2. リポジトリにコラボレーターとして招待する
* リポジトリ作成者はチームメンバーをコラボレーターすることで、リポジトリに書き込み等の権限が付与され、ソースコードのプッシュなどができるようになります。
1. コラボレーターとして招待する人のユーザ名を確認してください。  
2. Githubで、リポジトリのメインページにアクセスしてください。 
3. リポジトリ名の下で Setting(設定) をクリックしてください。
4. 左のサイドバーで Manage access(アクセスの管理) をクリックしてください。
5. [Invite a collaborator] をクリックします。
6. 検索フィールドで招待する人の名前を入力し、一致するリストの名前をクリックします。
7. [Add NAME to REPOSITORY] をクリックします。
8. メールに届いた招待からリポジトリに参加できます。

## 3. ローカルにリポジトリを保存する
エクスプローラーのリポジトリを入れたいフォルダで検索欄に「cmd」と入力し、コマンドプロンプトを開き、以下のコードを入力する。
    

    git clone githubのアドレス

## 4. pushするために必要な作業(VScodeのターミナルで実行する)
1.Githubのアカウント　(VSCodeのターミナル)  
例：git config --global user.name "takathosiinaoka"

    git config --global user.name "Githubアカウント名"  　 


2.メールアドレス(VSCodeのターミナル)  
例：git config --global user.email heavenhayao2316@gmail.com  

    git config --global user.email メールアドレス

## 5.編集履歴の表示(TortoiseGit or Gitlog)
エクスプローラーで緑のチェックが入ったフォルダを右クリックし、「TortoiseGit」の「ログを表示」より閲覧できる。  
また、VSCodeのターミナルで確認することもできる。以下のコードより確認できる。Enterキーを押すと過去のログが参照できる。「q」キーで終了する。

    git log

  

  
   
   
