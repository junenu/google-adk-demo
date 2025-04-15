from google.adk.agents import Agent
from netmiko import ConnectHandler
import os
import yaml
from typing import Dict, Any


def load_device_config(device_name: str) -> Dict[str, Any]:
    config_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "devices.yaml"
    )

    try:
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        if device_name not in config.get("devices", {}):
            raise KeyError(f"Device '{device_name}' not found in configuration")

        return config["devices"][device_name]
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found at {config_path}")


def get_router_info(device_name: str) -> str:
    """
    ネットワークデバイスの情報を取得する関数
    ネットワークデバイスのOSのバージョン情報を取得します。
    Args:
        device_name (str): デバイスの名前
    Returns:
        str: デバイスの情報
    """
    try:
        device = load_device_config(device_name)
        with ConnectHandler(**device) as connection:
            output = connection.send_command("show version")
            return output
    except Exception as e:
        return f"Error connecting to device: {e}"


root_agent = Agent(
    name="nw_agent",
    model="gemini-2.0-flash",
    description=("あなたはネットワークエンジニアのAIです。 "),
    instruction=(
        "ネットワークデバイスの情報を取得するためのエージェントです。 "
        "ネットワークデバイスに接続し、必要な情報を取得します。"
        "取得した情報は、ユーザーに返します。"
    ),
    tools=[get_router_info],
)
