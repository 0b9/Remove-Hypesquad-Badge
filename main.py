import requests

class DiscordHypeSquadManager:
    def __init__(self):
        self.api_url = "https://discord.com/api/v9/hypesquad/online"
        self.house_names = {
            1: "Bravery (Purple)",
            2: "Brilliance (Red)",
            3: "Balance (Green)"
        }

    def run(self):
        print("--- Discord HypeSquad Badge Changer & Remover ---")
        
        while True:
            print("\nOptions: [1] Bravery, [2] Brilliance, [3] Balance, [0] Remove Badge")
            
            try:
                user_input = input("Select an option (0-3): ").strip()
                if not user_input.isdigit() or int(user_input) not in [0, 1, 2, 3]:
                    print("Invalid choice. Please enter 0, 1, 2, or 3.")
                    continue
                
                choice = int(user_input)
                print()
                
                token = input("Enter your Discord Token: ").strip().strip("'").strip('"')
                print()

                if not token:
                    print("Token cannot be empty.")
                    continue

                if choice == 0:
                    success = self.remove_badge(token)
                else:
                    success = self.set_badge(token, choice)
                
                if success:
                    break

            except ValueError:
                print("Invalid input. Please enter a number.")

    def set_badge(self, token, house_id):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        payload = {"house_id": house_id}

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            house_label = self.house_names.get(house_id, f"House {house_id}")
            return self.handle_response(response, f"Changed to {house_label} badge successfully!")
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def remove_badge(self, token):
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        try:
            response = requests.delete(self.api_url, headers=headers)
            if response.status_code in [200, 204]:
                print("HypeSquad badge removed successfully")
                return True
            else:
                return self.handle_response(response, "HypeSquad badge removed successfully")
        except Exception as e:
            print(f"Connection error: {e}")
            return False

    def handle_response(self, response, success_msg):
        if response.status_code in [200, 204]:
            print(success_msg)
            return True
        elif response.status_code == 401:
            print("Invalid token. Please try again.")
            return False
        elif response.status_code == 429:
            print("Ratelimited. Please wait for a few minutes before trying again.")
            return False
        else:
            try:
                error_data = response.json()
                print(f"Error ({response.status_code}): {error_data.get('message', 'Unknown error')}")
            except:
                print(f"Error: Received status code {response.status_code}")
            return False

if __name__ == "__main__":
    manager = DiscordHypeSquadManager()
    manager.run()
