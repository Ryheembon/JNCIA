#!/usr/bin/env python3
import random
import time
import os
import sys

# ANSI color codes for formatting
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print a formatted header for the quiz."""
    clear_screen()
    print(f"{Colors.HEADER}{Colors.BOLD}========================================{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}          JNCIA-105 QUIZ CLI           {Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}========================================{Colors.ENDC}")
    print()

# Comprehensive question bank for JNCIA-105 (50 questions)
questions = [
    # Original questions from the existing quiz
    {
        "question": "What is the default port number for SSH on Junos devices?",
        "options": ["22", "23", "80", "443"],
        "answer": "22",
        "explanation": "SSH (Secure Shell) uses port 22 by default, while Telnet uses port 23."
    },
    {
        "question": "Which layer of the OSI model does a router operate on?",
        "options": ["Layer 1", "Layer 2", "Layer 3", "Layer 4"],
        "answer": "Layer 3",
        "explanation": "Routers operate at Layer 3 (Network Layer) of the OSI model, making forwarding decisions based on IP addresses."
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
        "explanation": "The 'commit' command activates the changes made in the candidate configuration and moves them to the active configuration."
    },
    {
        "question": "Which command displays the routing table in Junos?",
        "options": ["show interfaces", "show route", "show configuration", "show arp"],
        "answer": "show route",
        "explanation": "The 'show route' command displays the routing table entries in Junos."
    },
    {
        "question": "Which protocol is used for communication in OSPF?",
        "options": ["TCP", "UDP", "IP", "ICMP"],
        "answer": "IP",
        "explanation": "OSPF uses IP protocol 89 directly, without TCP or UDP."
    },
    {
        "question": "How do you revert to a previous configuration in Junos?",
        "options": ["rollback 0", "rollback 1", "load replace", "load override"],
        "answer": "rollback 1",
        "explanation": "The 'rollback 1' command reverts to the previous configuration. 'rollback 0' loads the current active configuration."
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
        "explanation": "Routing policies are used to control the import and export of routes, modify route attributes, and filter routes."
    },
    {
        "question": "In Junos, which command allows you to view the software version?",
        "options": ["show version", "show software", "show system", "show configuration"],
        "answer": "show version",
        "explanation": "The 'show version' command displays information about the Junos OS version installed on the device."
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
        "explanation": "Static routes are manually configured by administrators and do not change automatically in response to network conditions."
    },
    {
        "question": "Which protocol does Junos use for secure remote access?",
        "options": ["FTP", "Telnet", "SSH", "HTTP"],
        "answer": "SSH",
        "explanation": "SSH (Secure Shell) provides secure encrypted communications for remote access to Junos devices."
    },
    # Adding more questions to reach at least 50
    {
        "question": "What are the routing table names in Junos?",
        "options": [
            "inet.0, inet.1, inet.2, inet.3",
            "ipv4.0, ipv6.0",
            "route.0, route.1",
            "main.0, backup.0"
        ],
        "answer": "inet.0, inet.1, inet.2, inet.3",
        "explanation": "The main routing tables in Junos are inet.0 (IPv4 unicast), inet.1 (IPv4 multicast), inet.2 (MPLS), inet.3 (MPLS LSP), etc."
    },
    {
        "question": "What is the default administrative distance for OSPF internal routes?",
        "options": ["5", "10", "15", "20"],
        "answer": "10",
        "explanation": "In Junos, OSPF internal routes have a default preference value of 10."
    },
    {
        "question": "What command shows BGP neighbor status?",
        "options": [
            "show bgp neighbor",
            "show protocol bgp",
            "display bgp peer",
            "get bgp neighbors"
        ],
        "answer": "show bgp neighbor",
        "explanation": "The 'show bgp neighbor' command displays the status of BGP neighbor connections."
    },
    {
        "question": "What are the three security zone types in Junos?",
        "options": [
            "Security, Functional, Transport",
            "Public, Private, DMZ",
            "Trust, Untrust, DMZ",
            "Inside, Outside, Perimeter"
        ],
        "answer": "Security, Functional, Transport",
        "explanation": "The three security zone types are Security zones (for security policies), Functional zones (for special purposes like management), and Transport zones (for VPN termination)."
    },
    {
        "question": "What command do you use to check interface errors?",
        "options": [
            "show interfaces extensive",
            "show interface errors",
            "display interface stats",
            "get interface counters"
        ],
        "answer": "show interfaces extensive",
        "explanation": "The 'show interfaces extensive' command provides detailed information about interfaces including error counters."
    },
    {
        "question": "What are the different types of NAT in Junos?",
        "options": [
            "Source NAT, Destination NAT, Static NAT, Persistent NAT",
            "Basic NAT, Advanced NAT",
            "One-to-one NAT, One-to-many NAT",
            "Inbound NAT, Outbound NAT"
        ],
        "answer": "Source NAT, Destination NAT, Static NAT, Persistent NAT",
        "explanation": "Junos supports Source NAT (SNAT), Destination NAT (DNAT), Static NAT, and Persistent NAT types."
    },
    {
        "question": "What are the components of chassis clustering?",
        "options": [
            "Control ports, Fabric ports, Redundancy groups",
            "Main ports, Backup ports, Failover groups",
            "Primary unit, Secondary unit",
            "Active node, Passive node"
        ],
        "answer": "Control ports, Fabric ports, Redundancy groups",
        "explanation": "Chassis clustering involves control ports, fabric ports, redundancy groups, redundant ethernet interfaces, control links, and fabric links."
    },
    {
        "question": "What are the OSPF LSA types?",
        "options": [
            "Type 1-7",
            "Type 1-5",
            "Type A-E",
            "Type Primary, Secondary, Tertiary"
        ],
        "answer": "Type 1-7",
        "explanation": "OSPF uses LSA Types 1-7, including Type 1 (Router LSA), Type 2 (Network LSA), Type 3 (Summary LSA), etc."
    },
    {
        "question": "What are the BGP neighbor states in order?",
        "options": [
            "Idle, Connect, Active, OpenSent, OpenConfirm, Established",
            "Down, Init, 2-Way, ExStart, Exchange, Loading, Full",
            "Starting, Connecting, Connected, Operational",
            "New, Handshake, Authentication, Established"
        ],
        "answer": "Idle, Connect, Active, OpenSent, OpenConfirm, Established",
        "explanation": "BGP neighbor states progress in this order: Idle, Connect, Active, OpenSent, OpenConfirm, and finally Established."
    },
    {
        "question": "What are the OSPF network types?",
        "options": [
            "Broadcast, Point-to-Point, Point-to-Multipoint, Non-Broadcast",
            "Ethernet, Serial, Frame Relay, ATM",
            "LAN, WAN, MAN, WLAN",
            "Wired, Wireless, Cellular, Satellite"
        ],
        "answer": "Broadcast, Point-to-Point, Point-to-Multipoint, Non-Broadcast",
        "explanation": "OSPF network types include Broadcast, Point-to-Point, Point-to-Multipoint, and Non-Broadcast Multi-Access (NBMA)."
    },
    {
        "question": "What command shows interface statistics?",
        "options": [
            "show interfaces statistics",
            "show interface counters",
            "display interface stats",
            "get interface metrics"
        ],
        "answer": "show interfaces statistics",
        "explanation": "The 'show interfaces statistics' command displays packet counts and other statistical information for interfaces."
    },
    {
        "question": "What is the purpose of the 'show log messages' command?",
        "options": [
            "View system log messages",
            "Display configuration changes",
            "Show login history",
            "View error reports"
        ],
        "answer": "View system log messages",
        "explanation": "The 'show log messages' command displays system log messages which are useful for troubleshooting."
    },
    {
        "question": "What are the different VLAN types supported in Junos?",
        "options": [
            "Layer 2 VLANs, IRB, Layer 3 VLANs, Private VLANs",
            "Standard VLANs, Extended VLANs",
            "Single VLANs, Multiple VLANs",
            "Trunk VLANs, Access VLANs"
        ],
        "answer": "Layer 2 VLANs, IRB, Layer 3 VLANs, Private VLANs",
        "explanation": "Junos supports Layer 2 VLANs, Integrated Routing and Bridging (IRB), Layer 3 VLANs, and Private VLANs."
    },
    {
        "question": "What command is used to check the routing engine status?",
        "options": [
            "show chassis routing-engine",
            "show system routing-engine",
            "display routing-engine",
            "get routing-engine status"
        ],
        "answer": "show chassis routing-engine",
        "explanation": "The 'show chassis routing-engine' command shows the status and health of the routing engine."
    },
    {
        "question": "What is the default hello interval for OSPF?",
        "options": ["10 seconds", "30 seconds", "40 seconds", "60 seconds"],
        "answer": "10 seconds",
        "explanation": "The default hello interval for OSPF is 10 seconds on broadcast and point-to-point networks."
    },
    {
        "question": "What command is used to display current users logged into a Junos device?",
        "options": ["show system users", "show users", "display users", "who"],
        "answer": "show system users",
        "explanation": "The 'show system users' command displays information about users currently logged into the device."
    },
    {
        "question": "What is the purpose of 'commit confirmed' in Junos?",
        "options": [
            "Temporarily activates changes and automatically rolls back unless confirmed",
            "Permanently saves configuration changes",
            "Checks configuration for errors",
            "Confirms previous commit operation"
        ],
        "answer": "Temporarily activates changes and automatically rolls back unless confirmed",
        "explanation": "The 'commit confirmed' command activates configuration changes but automatically rolls back after a specified time unless the commit is confirmed."
    },
    {
        "question": "What does the 'monitor traffic' command do?",
        "options": [
            "Captures and displays packets on an interface",
            "Shows bandwidth utilization",
            "Displays interface statistics",
            "Monitors user activity"
        ],
        "answer": "Captures and displays packets on an interface",
        "explanation": "The 'monitor traffic' command is similar to tcpdump and captures/displays packet information passing through an interface."
    },
    {
        "question": "What is the default dead interval for OSPF?",
        "options": ["40 seconds", "10 seconds", "60 seconds", "30 seconds"],
        "answer": "40 seconds",
        "explanation": "The default dead interval for OSPF is 40 seconds, which is 4 times the hello interval."
    },
    {
        "question": "What command is used to view the current configuration?",
        "options": [
            "show configuration",
            "display config",
            "get configuration",
            "view configuration"
        ],
        "answer": "show configuration",
        "explanation": "The 'show configuration' command displays the current active configuration of the device."
    },
    {
        "question": "What is the purpose of 'load merge' in Junos?",
        "options": [
            "Combines configuration data with the current candidate configuration",
            "Replaces the entire configuration",
            "Loads a previous configuration version",
            "Merges running and startup configurations"
        ],
        "answer": "Combines configuration data with the current candidate configuration",
        "explanation": "The 'load merge' command combines (merges) new configuration data with the existing candidate configuration."
    },
    {
        "question": "What is the Junos OS modular architecture based on?",
        "options": ["FreeBSD", "Linux", "Windows", "Proprietary OS"],
        "answer": "FreeBSD",
        "explanation": "Junos OS is based on FreeBSD which provides process separation between the control and forwarding planes."
    },
    {
        "question": "What are the BGP path attributes that influence route selection?",
        "options": [
            "Local Preference, AS Path, Origin, MED",
            "Weight, Priority, Cost, Metric",
            "Distance, Delay, Bandwidth, Load",
            "Route, Path, Hop, Jump"
        ],
        "answer": "Local Preference, AS Path, Origin, MED",
        "explanation": "BGP path attributes that influence route selection include Local Preference, AS Path length, Origin code, MED, and others."
    },
    {
        "question": "What is the purpose of the 'request system reboot' command?",
        "options": [
            "Reboots the entire system",
            "Restarts only routing processes",
            "Reloads the configuration",
            "Restarts interfaces"
        ],
        "answer": "Reboots the entire system",
        "explanation": "The 'request system reboot' command initiates a full system reboot of the Junos device."
    },
    {
        "question": "What is the default route preference for static routes in Junos?",
        "options": ["5", "10", "20", "100"],
        "answer": "5",
        "explanation": "Static routes in Junos have a default route preference (administrative distance) of 5."
    },
    {
        "question": "What is the Junos command to display the current zone configuration?",
        "options": [
            "show security zones",
            "display zones",
            "get security zones",
            "list zones"
        ],
        "answer": "show security zones",
        "explanation": "The 'show security zones' command displays information about configured security zones."
    },
    {
        "question": "What protocol does Junos use for transferring files to/from the device?",
        "options": ["SCP/SFTP", "FTP", "TFTP", "HTTP"],
        "answer": "SCP/SFTP",
        "explanation": "Junos primarily uses SCP (Secure Copy) and SFTP (SSH File Transfer Protocol) for secure file transfers."
    },
    {
        "question": "How do you verify OSPF neighbors in Junos?",
        "options": [
            "show ospf neighbor",
            "display ospf peer",
            "get ospf adjacency",
            "list ospf neighbors"
        ],
        "answer": "show ospf neighbor",
        "explanation": "The 'show ospf neighbor' command displays information about OSPF neighbor relationships."
    },
    {
        "question": "What command displays hardware information about a Junos device?",
        "options": [
            "show chassis hardware",
            "display hardware",
            "get hardware info",
            "show system hardware"
        ],
        "answer": "show chassis hardware",
        "explanation": "The 'show chassis hardware' command displays information about the physical components of the device."
    },
    {
        "question": "What is the purpose of a firewall filter in Junos?",
        "options": [
            "To filter traffic based on match conditions",
            "To block malware and viruses",
            "To encrypt sensitive data",
            "To compress traffic"
        ],
        "answer": "To filter traffic based on match conditions",
        "explanation": "Firewall filters in Junos are used to filter traffic based on specified match conditions and perform actions (accept, discard, etc.)."
    },
    {
        "question": "How do you check the status of interfaces in Junos?",
        "options": [
            "show interfaces terse",
            "display interface status",
            "get interfaces",
            "list interface state"
        ],
        "answer": "show interfaces terse",
        "explanation": "The 'show interfaces terse' command provides a concise view of interface status and IP addressing."
    },
    {
        "question": "What is the command to check BGP summary information?",
        "options": [
            "show bgp summary",
            "display bgp overview",
            "get bgp status",
            "list bgp peers"
        ],
        "answer": "show bgp summary",
        "explanation": "The 'show bgp summary' command displays summary information about BGP peers and routes."
    },
    {
        "question": "What are the OSPF area types?",
        "options": [
            "Backbone, Standard, Stub, Totally Stubby, NSSA",
            "Primary, Secondary, Tertiary",
            "Main, Backup, Transit",
            "Core, Distribution, Access"
        ],
        "answer": "Backbone, Standard, Stub, Totally Stubby, NSSA",
        "explanation": "OSPF area types include Backbone (Area 0), Standard Area, Stub Area, Totally Stubby Area, and Not-So-Stubby Area (NSSA)."
    },
    {
        "question": "What is the purpose of the 'ping' command in Junos?",
        "options": [
            "To test network connectivity to another host",
            "To check interface status",
            "To display routing information",
            "To verify system uptime"
        ],
        "answer": "To test network connectivity to another host",
        "explanation": "The 'ping' command is used to test IP connectivity to another host by sending ICMP echo requests."
    },
    {
        "question": "What is the default MTU size for Ethernet interfaces in Junos?",
        "options": ["1500 bytes", "1000 bytes", "1400 bytes", "9000 bytes"],
        "answer": "1500 bytes",
        "explanation": "The default Maximum Transmission Unit (MTU) size for Ethernet interfaces in Junos is 1500 bytes."
    },
    {
        "question": "What command allows you to monitor interface traffic in real-time?",
        "options": [
            "monitor interface traffic",
            "show interface live",
            "watch interfaces",
            "display interface realtime"
        ],
        "answer": "monitor interface traffic",
        "explanation": "The 'monitor interface traffic' command displays real-time traffic statistics for interfaces."
    },
    {
        "question": "What are the routing instances types supported in Junos?",
        "options": [
            "Virtual-router, VRF, Virtual-switch, Forwarding",
            "Primary, Secondary, Auxiliary",
            "Main, Backup, Standby",
            "Active, Passive, Monitoring"
        ],
        "answer": "Virtual-router, VRF, Virtual-switch, Forwarding",
        "explanation": "Junos routing instance types include virtual-router, VRF (Virtual Routing and Forwarding), virtual-switch, and forwarding."
    },
    {
        "question": "What is the purpose of 'deactivate' in Junos configuration?",
        "options": [
            "To temporarily disable a configuration section without deleting it",
            "To permanently remove a configuration",
            "To restart a process",
            "To reset a configuration to defaults"
        ],
        "answer": "To temporarily disable a configuration section without deleting it",
        "explanation": "The 'deactivate' command temporarily disables a portion of the configuration without deleting it."
    },
    {
        "question": "What is the command to view the current NAT rules?",
        "options": [
            "show security nat",
            "display nat rules",
            "get nat configuration",
            "list nat translations"
        ],
        "answer": "show security nat",
        "explanation": "The 'show security nat' command displays information about configured NAT rules."
    },
    {
        "question": "What is the Junos operational mode prompt?",
        "options": [
            "user@device>",
            "user@device#",
            "user@device$",
            "user@device:"
        ],
        "answer": "user@device>",
        "explanation": "The Junos operational mode prompt ends with '>' (e.g., user@device>), while configuration mode ends with '#'."
    },
    {
        "question": "What is the command to check system alarms?",
        "options": [
            "show chassis alarms",
            "display system alarms",
            "get alarms",
            "list alerts"
        ],
        "answer": "show chassis alarms",
        "explanation": "The 'show chassis alarms' command displays active system and hardware alarms."
    },
    {
        "question": "What is the difference between 'commit' and 'commit confirmed'?",
        "options": [
            "'commit confirmed' automatically rolls back unless confirmed, 'commit' doesn't",
            "'commit' is temporary, 'commit confirmed' is permanent",
            "'commit confirmed' requires approval, 'commit' doesn't",
            "There is no difference"
        ],
        "answer": "'commit confirmed' automatically rolls back unless confirmed, 'commit' doesn't",
        "explanation": "'commit confirmed' activates changes but automatically rolls back after a specified time unless confirmed, while 'commit' makes changes permanent immediately."
    }
]

def random_quiz_questions(questions, num_questions=10):
    """Return a random subset of questions."""
    return random.sample(questions, min(num_questions, len(questions)))

def print_progress_bar(current, total, bar_length=50):
    """Print a progress bar to show quiz progress."""
    percent = float(current) / float(total)
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    
    sys.stdout.write(f"\rProgress: [{arrow}{spaces}] {int(percent * 100)}%")
    sys.stdout.flush()

def run_quiz():
    """Run the main quiz application."""
    print_header()
    
    # Ask how many questions
    while True:
        try:
            print(f"{Colors.YELLOW}How many questions would you like (5-50)?{Colors.ENDC}")
            num_questions = int(input("> "))
            if 5 <= num_questions <= 50:
                break
            else:
                print(f"{Colors.RED}Please enter a number between 5 and 50.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.RED}Please enter a valid number.{Colors.ENDC}")
    
    # Select random questions
    quiz_questions = random_quiz_questions(questions, num_questions)
    total_questions = len(quiz_questions)
    correct_answers = 0
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}Starting quiz with {total_questions} questions...{Colors.ENDC}")
    time.sleep(1)
    
    # Loop through questions
    for i, question in enumerate(quiz_questions):
        clear_screen()
        print_header()
        print_progress_bar(i, total_questions)
        print(f"\n{Colors.BOLD}Question {i+1} of {total_questions}:{Colors.ENDC}")
        print(f"{Colors.BLUE}{question['question']}{Colors.ENDC}\n")
        
        # Display options
        for j, option in enumerate(question['options']):
            print(f"{j+1}. {option}")
        
        # Get user answer
        while True:
            try:
                print(f"\n{Colors.YELLOW}Enter your answer (1-{len(question['options'])}):{Colors.ENDC}")
                user_answer = int(input("> "))
                if 1 <= user_answer <= len(question['options']):
                    break
                else:
                    print(f"{Colors.RED}Please enter a number between 1 and {len(question['options'])}.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.RED}Please enter a valid number.{Colors.ENDC}")
        
        # Check answer
        user_choice = question['options'][user_answer-1]
        is_correct = user_choice == question['answer']
        
        if is_correct:
            correct_answers += 1
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ CORRECT!{Colors.ENDC}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}✗ INCORRECT!{Colors.ENDC}")
            print(f"{Colors.RED}The correct answer is: {question['answer']}{Colors.ENDC}")
        
        # Display explanation
        print(f"\n{Colors.YELLOW}Explanation: {question['explanation']}{Colors.ENDC}")
        
        # Wait for user to continue
        input("\nPress Enter to continue...")
    
    # Display final score
    clear_screen()
    print_header()
    score_percent = (correct_answers / total_questions) * 100
    
    print(f"\n{Colors.BOLD}Quiz Complete!{Colors.ENDC}")
    print(f"\nYou got {correct_answers} out of {total_questions} questions correct.")
    print(f"Your score: {Colors.BOLD}{score_percent:.1f}%{Colors.ENDC}")
    
    if score_percent >= 80:
        print(f"\n{Colors.GREEN}Great job! You're doing well with your JNCIA preparation!{Colors.ENDC}")
    elif score_percent >= 60:
        print(f"\n{Colors.YELLOW}Good effort! Keep studying to improve your score.{Colors.ENDC}")
    else:
        print(f"\n{Colors.RED}More practice needed. Focus on the topics you missed.{Colors.ENDC}")
    
    # Ask if user wants to try again
    print("\nWould you like to take another quiz? (y/n)")
    try_again = input("> ").lower()
    if try_again == 'y':
        run_quiz()
    else:
        print(f"\n{Colors.BLUE}Thank you for using the JNCIA-105 Quiz CLI!{Colors.ENDC}")
        print(f"{Colors.BLUE}Good luck with your exam preparation!{Colors.ENDC}")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Quiz terminated. Goodbye!{Colors.ENDC}") 