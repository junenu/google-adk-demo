# google-adk-demo

## Description

```bash
pip install google-adk
```

```bash
mkdir YOUR_PROJECT
```

```bash
echo "from . import agent" > YOUR_PROJECT/__init__.py
```

```bash
touch YOUR_PROJECT/agent.py
```

## Example

```bash
$ adk run quickstart
Log setup complete: /var/folders/99/c_hjgj5s63g73v4f_xysq34r0000gn/T/agents_log/agent.20250415_091219.log
To access latest log: tail -F /var/folders/99/c_hjgj5s63g73v4f_xysq34r0000gn/T/agents_log/agent.latest.log
Running agent weather_time_agent, type exit to exit.
user: What is the weather in New York?
[weather_time_agent]: OK. The weather in New York is sunny with a temperature of 25 degrees Celsius (41 degrees Fahrenheit).
```

## ADK Usage

- Web

```bash
adk web
```

- Cli

```bash
adk run YOUR_PROJECT
```

- Api-server

```bash
adk api_server
```

## reference

[Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)
