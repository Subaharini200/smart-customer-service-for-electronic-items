class ElectronicsSupportAgent:
    def __init__(self):
        self.knowledge_base = {
            "router": {
                "no internet": {
                    "questions": [
                        "Is the WAN light blinking?",
                        "Have you restarted the router?"
                    ],
                    "solutions": [
                        "Restart the modem and router",
                        "Check if ISP service is down",
                        "Replace ethernet cable"
                    ]
                },
                "wifi keeps disconnecting": {
                    "questions": [
                        "Does the issue happen on all devices?",
                        "Does the router overheat?"
                    ],
                    "solutions": [
                        "Update router firmware",
                        "Move router to open space",
                        "Change Wi-Fi channel"
                    ]
                }
            },

            "tv": {
                "no display": {
                    "questions": [
                        "Is the power light on?",
                        "Is the HDMI cable connected properly?"
                    ],
                    "solutions": [
                        "Reconnect HDMI cable",
                        "Try using a different HDMI port",
                        "Factory reset the TV"
                    ]
                },
                "no sound": {
                    "questions": [
                        "Is the TV muted?",
                        "Are speakers set to the right output?"
                    ],
                    "solutions": [
                        "Unmute TV",
                        "Select correct audio source",
                        "Check HDMI/AV cable audio pins"
                    ]
                },
                "apps not working": {
                    "questions": [
                        "Is the TV connected to the internet?",
                        "Have you updated the app?"
                    ],
                    "solutions": [
                        "Reconnect Wi-Fi",
                        "Update or reinstall the app",
                        "Restart the TV"
                    ]
                }
            },

            "laptop": {
                "overheating": {
                    "questions": [
                        "Is the fan making noise?",
                        "Does the laptop shut down automatically?"
                    ],
                    "solutions": [
                        "Clean the fan vents",
                        "Use a cooling pad",
                        "Replace thermal paste"
                    ]
                },
                "battery draining fast": {
                    "questions": [
                        "Is the screen brightness too high?",
                        "Do you have many apps running?"
                    ],
                    "solutions": [
                        "Reduce brightness",
                        "Disable background apps",
                        "Replace old battery"
                    ]
                },
                "slow performance": {
                    "questions": [
                        "Are there many startup programs?",
                        "Is disk usage at 100%?"
                    ],
                    "solutions": [
                        "Uninstall unused apps",
                        "Disable startup programs",
                        "Upgrade to SSD or add RAM"
                    ]
                }
            }
        }

    def diagnose(self, product, issue):
        product = product.lower()
        issue = issue.lower()

        if product in self.knowledge_base:
            for known_issue in self.knowledge_base[product]:
                if known_issue in issue:
                    return self.knowledge_base[product][known_issue]

        return {
            "questions": ["Can you describe the issue in more detail?"],
            "solutions": ["Escalate to technical support"]
        }


def main():
    agent = ElectronicsSupportAgent()

    product = input("Enter product type (router / tv / laptop): ")
    issue = input("Describe the issue: ")

    result = agent.diagnose(product, issue)

    print("\n🔍 Diagnostic Questions:")
    for q in result["questions"]:
        print("- " + q)

    print("\n💡 Suggested Solutions:")
    for s in result["solutions"]:
        print("- " + s)

if __name__ == "__main__":
    main()


