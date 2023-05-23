# ともすすタスク管理

友人と使う想定で作ったタスク進捗管理アプリケーションです。<br>
使用者相互のタスクの進捗、作業時間などが確認できます。<br>
ログイン後はシングルページアプリケーションとなっています。<br>
フロントエンドはReactとRedux ToolKitで制作し、Firebase Hostingを用いて公開しています。

# URL

https://tomosusu-task.web.app/ <br>
ゲストアカウント<br>
ユーザーネーム: guest <br>
パスワード: guestpassword <br>

# 作成経緯

私自身、人の作業状況が見えることがモチベーションに繋がる性格であったため、<br>
友人と作業状況を共有して大学の期末考査に向けて勉強を効率的に進められるように<br>
本アプリを作成しました。

# 使用技術

- Python
- Django REST framework
- PostgreSQL
- Nginx
- React
- Redux ToolKit
- AWS EC2
- Firebase

# 機能一覧
- 認証関連
    - ユーザー登録
    - ログイン
    - ログアウト
- タスク関連
    - タスク新規作成
    - タスク編集
        - タスク種別の新規作成
        - タスクの作業時間測定
    - タスク削除
    - タスクの並び替え
    - タスクの検索
- その他
    - プロフィール画像の設定、編集
