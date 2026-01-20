## Discord HypeSquad Badge Remover & Changer

This is a simple Python script that allows you to remove or change your Discord HypeSquad badge after Discord removed the HypeSquad menu (Thanks Discord!).

---

## Setup

Before running the script, you need to have **Python** installed on your system and install the `requests` library.

### 1. Install Requirements

Open your terminal or command prompt and run the following command to install the necessary dependency:

```bash
pip install requests

```
---

## How to Use

1. **Run the Script:**
```bash
python main.py

```


2. **Select an Option:** Type the number corresponding to the house you want and press **Enter**.

| Input Number | House | Badge Color |
| --- | --- | --- |
| **0** | **Remove Badge** | N/A |
| **1** | **Bravery** | Purple |
| **2** | **Brilliance** | Red |
| **3** | **Balance** | Green |

3. **Enter Token:** Paste your Discord account token when prompted and press **Enter**.

---

## Security & Warning

> [!IMPORTANT]
> **Keep your token secret.** Your Discord token is essentially your password. Never share it with anyone or paste it into untrusted websites. This script only sends your token to the official `discord.com/api` endpoint.

### How to get your Discord Token:

1. Open Discord in your **Web Browser** (Chrome, Edge, etc.).
2. Press `F12` (or `Ctrl` + `Shift` + `I`) to open Developer Tools.
3. Go to the **Network** tab.
4. Filter `Fetch/XHR` requests only.
5. Switch to any channel/server/DM or send a message. 
6. Click on one of the requests and look for `authorization` under the **Request Headers** section. That is your token.
