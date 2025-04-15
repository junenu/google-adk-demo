# ネットワークデバイス管理エージェント

## 概要

このプロジェクトは、Google ADK（Agent Development Kit）を活用して構築された、ネットワークデバイス管理のためのAIアシスタントです。
Netmikoライブラリを活用して、ネットワークデバイス（ルーター、スイッチなど）に接続し、情報の取得および管理が可能です。

## 機能

- YAMLファイルからのデバイス設定情報の読み込み
- Netmikoを使用したネットワークデバイスへの接続
- ネットワークデバイスからのバージョン情報（show version）の取得
- Google ADKを活用したAIエージェントインターフェース
- エラーハンドリング機能（デバイス設定ファイルの欠如や、指定されたデバイスが設定ファイルに存在しない場合に対応）

## 何ができるか？

このエージェントでは、以下のことが可能です：

1. **デバイス情報の取得**: ネットワークデバイスに接続し、OSバージョンや設定情報を取得できます
2. **複数デバイスの管理**: `devices.yaml`に定義された複数のデバイス設定を切り替えて使用可能
3. **自然言語インターフェース**: Geminiモデルを活用し、自然言語でデバイス情報を要求できます
4. **モジュール式設計**: 機能拡張が容易な構造になっており、新たなネットワーク管理機能の追加が可能

## 使い方

### 1. 環境設定

```bash
# 必要なライブラリのインストール
pip install google-adk netmiko pyyaml
```

### 2. デバイス設定ファイルの作成

`devices.yaml` をプロジェクトディレクトリに作成し、以下の形式でデバイス情報を記述します：

```yaml
devices:
  router1:
    device_type: cisco_ios
    host: 192.168.x.x
    username: admin
    password: password
  
  switch1:
    device_type: cisco_ios
    host: 192.168.x.x
    username: admin
    password: password
```

### 3. エージェントの起動

```bash
# Google ADK CLIでエージェントを起動
adk run .
```

### 4. エージェントの使用例

```bash
adk run .
Log setup complete: /var/folders/99/c_hjgj5s63g73v4f_xysq34r0000gn/T/agents_log/agent.20250415_094423.log
To access latest log: tail -F /var/folders/99/c_hjgj5s63g73v4f_xysq34r0000gn/T/agents_log/agent.latest.log
Running agent nw_agent, type exit to exit.
user: rt1のOSバージョンを教えてください
[nw_agent]: rt1のOSバージョンは、Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.15.1です。
```

ちなみに

```bash
RT1#show version 
Cisco IOS Software [IOSXE], Linux Software (X86_64BI_LINUX-ADVENTERPRISEK9-M), Version 17.15.1, RELEASE SOFTWARE (fc4)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2024 by Cisco Systems, Inc.

--- snip ---
          
RT1#
```

## 注意事項

- 本番環境では、パスワードなどの機密情報の取り扱いに十分注意してください。
- ネットワークデバイスへの接続は適切な権限を持つユーザーが行うこと
- 大規模な環境では、接続のタイムアウト設定やエラーハンドリングを強化することをお勧めします
