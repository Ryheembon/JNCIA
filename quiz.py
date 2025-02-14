import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions
questions = [
    {
        "question": "What is the default port number for SSH on Junos devices?",
        "options": ["22", "23", "80", "443"],
        "answer": "22",
    },
    {
        "question": "Which layer of the OSI model does a router operate on?",
        "options": ["Layer 1", "Layer 2", "Layer 3", "Layer 4"],
        "answer": "Layer 3",
    },
    {
        "question": "What is the primary purpose of the 'commit' command in Junos?",
        "options": [
            "Save the configuration to a file",
            "Activate changes to the configuration",
            "Display configuration history",
            "Reset the configuration to factory defaults",
        ],
        "answer": "Activate changes to the configuration",
    },
    {
        "question": "Which command displays the routing table in Junos?",
        "options": ["show interfaces", "show route", "show configuration", "show arp"],
        "answer": "show route",
    },
    {
        "question": "Which protocol is used for communication in OSPF?",
        "options": ["TCP", "UDP", "IP", "ICMP"],
        "answer": "IP",
    },
    {
        "question": "How do you revert to a previous configuration in Junos?",
        "options": ["rollback 0", "rollback 1", "load replace", "load override"],
        "answer": "rollback 1",
    },
    {
        "question": "What is the function of a routing policy?",
        "options": [
            "To physically reroute traffic",
            "To alter route attributes or filter routes",
            "To upgrade Junos OS",
            "To manage firewall rules",
        ],
        "answer": "To alter route attributes or filter routes",
    },
    {
        "question": "In Junos, which command allows you to view the software version?",
        "options": ["show version", "show software", "show system", "show configuration"],
        "answer": "show version",
    },
    {
        "question": "What is the primary purpose of static routing?",
        "options": [
            "To enable dynamic path selection",
            "To predetermine and manually configure routes",
            "To allow automatic route changes",
            "To advertise routes to other routers",
        ],
        "answer": "To predetermine and manually configure routes",
    },
    {
        "question": "Which protocol does Junos use for secure remote access?",
        "options": ["FTP", "Telnet", "SSH", "HTTP"],
        "answer": "SSH",
    },
    {
        "question": "What is the purpose of the 'show interfaces' command in Junos?",
        "options": [
            "To display interface statistics and status",
            "To view routing tables",
            "To load a saved configuration",
            "To upgrade Junos OS",
        ],
        "answer": "To display interface statistics and status",
    },
    {
        "question": "What does CSMA/CD stand for in Ethernet networking?",
        "options": [
            "Carrier Sense Multiple Access with Collision Detection",
            "Continuous Signal Multiple Access with Collision Detection",
            "Carrier Sense Multipath Access with Connection Division",
            "Carrier Signal Multiple Allocation with Collision Division",
        ],
        "answer": "Carrier Sense Multiple Access with Collision Detection",
    },
    {
        "question": "Which Junos command saves the current configuration?",
        "options": ["commit", "rollback", "save config", "store configuration"],
        "answer": "commit",
    },
    {
        "question": "Which tool is used in Junos to troubleshoot connectivity?",
        "options": ["ping", "show route", "commit", "rollback"],
        "answer": "ping",
    },
    {
        "question": "What does the term 'default gateway' refer to?",
        "options": [
            "The main IP address of a router",
            "The destination for packets with no specific route",
            "The address of the DNS server",
            "The IP address of a local device",
        ],
        "answer": "The destination for packets with no specific route",
    },
    {
        "question": "What is the function of NAT in networking?",
        "options": [
            "To translate private IPs to public IPs",
            "To switch traffic between VLANs",
            "To reroute dynamic paths",
            "To assign MAC addresses to devices",
        ],
        "answer": "To translate private IPs to public IPs",
    },
    {
        "question": "Which address class is used for multicast traffic?",
        "options": ["Class A", "Class B", "Class C", "Class D"],
        "answer": "Class D",
    },
    {
        "question": "What is the function of the 'commit check' command?",
        "options": [
            "To test the syntax of a configuration",
            "To save the configuration",
            "To view commit history",
            "To rollback to a previous configuration",
        ],
        "answer": "To test the syntax of a configuration",
    },
    {
        "question": "Which of these is a routing protocol?",
        "options": ["TCP", "UDP", "OSPF", "IP"],
        "answer": "OSPF",
    },
    {
        "question": "What is the subnet mask for a /24 network?",
        "options": ["255.255.255.0", "255.255.0.0", "255.0.0.0", "255.255.255.128"],
        "answer": "255.255.255.0",
    },

    # New Questions
    {
        "question": "Which Junos configuration mode allows you to edit settings?",
        "options": ["Operational Mode", "Configuration Mode", "Monitor Mode", "Boot Mode"],
        "answer": "Configuration Mode",
    },
    {
        "question": "What command shows the current configuration?",
        "options": ["show config", "show system", "show configuration", "view config"],
        "answer": "show configuration",
    },
    {
        "question": "What is the MTU size for Ethernet by default?",
        "options": ["1500 bytes", "1400 bytes", "1600 bytes", "9000 bytes"],
        "answer": "1500 bytes",
    },
    {
        "question": "What is the purpose of the 'set' command in Junos?",
        "options": [
            "To display routing tables",
            "To modify the current configuration",
            "To commit changes",
            "To rollback changes",
        ],
        "answer": "To modify the current configuration",
    },
    {
        "question": "What is the loopback address for IPv4?",
        "options": ["127.0.0.1", "192.168.0.1", "10.0.0.1", "255.255.255.255"],
        "answer": "127.0.0.1",
    },
    {
        "question": "Which layer of the OSI model does the TCP protocol operate?",
        "options": ["Layer 2", "Layer 3", "Layer 4", "Layer 5"],
        "answer": "Layer 4",
    },
    {
        "question": "What does DHCP stand for?",
        "options": [
            "Dynamic Host Configuration Protocol",
            "Data Host Communication Protocol",
            "Dynamic Hardware Configuration Protocol",
            "Default Host Communication Protocol",
        ],
        "answer": "Dynamic Host Configuration Protocol",
    },
    {
        "question": "Which command checks the hardware status of a Junos device?",
        "options": ["show chassis hardware", "show system status", "show hardware info", "show inventory"],
        "answer": "show chassis hardware",
    },
    {
        "question": "What is the administrative distance of OSPF?",
        "options": ["90", "100", "110", "120"],
        "answer": "110",
    },
    {
        "question": "Which protocol is used for IP address resolution?",
        "options": ["ARP", "DNS", "NAT", "ICMP"],
        "answer": "ARP",
    },
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JNCIA-105 Quiz")
        self.root.geometry("600x400")

        # Shuffle questions
        random.shuffle(questions)
        self.questions = questions
        self.current_question = 0
        self.score = 0

        # Question Label
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        # Options Buttons
        self.options_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), width=40, command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=5)
            self.options_buttons.append(button)

        # Next Button
        self.next_button = tk.Button(root, text="Next Question", font=("Arial", 12), command=self.next_question)
        self.next_button.pack(pady=20)
        self.next_button.config(state="disabled")

        # Start Quiz
        self.display_question()

    def display_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=f"Q{self.current_question + 1}: {question['question']}")

        # Update options
        for idx, option in enumerate(question["options"]):
            self.options_buttons[idx].config(text=option, state="normal")

        # Disable Next button
        self.next_button.config(state="disabled")

    def check_answer(self, idx):
        question = self.questions[self.current_question]

        if question["options"][idx] == question["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer is: {question['answer']}")

        # Disable options after answering
        for btn in self.options_buttons:
            btn.config(state="disabled")

        # Enable Next button
        self.next_button.config(state="normal")

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.display_question()
        else:
            # End of Quiz
            messagebox.showinfo("Quiz Finished", f"You scored {self.score}/{len(self.questions)}!")
            self.root.destroy()

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
