const flashcards = [
    // ROUTING FUNDAMENTALS (25 questions)
    {
        category: 'routing',
        question: 'What are the main routing table names in Junos?',
        answer: `Main routing tables in Junos:
1. inet.0 - IPv4 unicast routes
2. inet.1 - IPv4 multicast routes
3. inet.2 - MPLS routes
4. inet.3 - MPLS LSP routes
5. inet.4 - Multicast RPF routes
6. inet6.0 - IPv6 unicast routes`
    },
    {
        category: 'routing',
        question: 'Explain route preferences in JunOS',
        answer: `Route preferences (lower is preferred):
1. Direct route: 0
2. Local route: 0
3. Static route: 5
4. OSPF internal: 10
5. BGP internal: 170
6. BGP external: 170`
    },
    {
        category: 'routing',
        question: 'What are the different BGP path attributes?',
        answer: `BGP path attributes:
1. Origin (IGP, EGP, Incomplete)
2. AS_PATH
3. NEXT_HOP
4. MED (Multi-Exit Discriminator)
5. Local Preference
6. Community`
    },
    // SECURITY (25 questions)
    {
        category: 'security',
        question: 'What are the IPsec phases?',
        answer: `IPsec phases:
1. Phase 1 (IKE):
   - Authentication
   - Key exchange
   - SA establishment
2. Phase 2 (IPsec):
   - Data encryption
   - Tunnel establishment`
    },
    {
        category: 'security',
        question: 'What are the available NAT rule match conditions?',
        answer: `NAT match conditions:
1. Source address/prefix
2. Destination address/prefix
3. Protocol
4. Source port
5. Destination port
6. Routing instance`
    },
    // SWITCHING (15 questions)
    {
        category: 'switching',
        question: 'Explain RSTP port states',
        answer: `RSTP port states:
1. Discarding
2. Learning
3. Forwarding

Previous STP states:
1. Blocking
2. Listening
3. Learning
4. Forwarding
5. Disabled`
    },
    // TROUBLESHOOTING (20 questions)
    {
        category: 'troubleshooting',
        question: 'What steps do you take to troubleshoot OSPF neighbor issues?',
        answer: `OSPF troubleshooting steps:
1. Verify physical connectivity
2. Check interface configuration
3. Verify OSPF configuration:
   - Area match
   - Authentication
   - Network type
4. Check timers
5. Commands to use:
   - show ospf neighbor
   - show ospf interface
   - show route protocol ospf`
    },
    // HIGH AVAILABILITY (15 questions)
    {
        category: 'high-availability',
        question: 'What are the redundancy group states in chassis cluster?',
        answer: `Redundancy group states:
1. Primary
2. Secondary
3. Disabled
4. Ineligible
5. Hold`
    },
    // Policy & Firewall (15 questions)
    {
        category: 'policy',
        question: 'What are the components of a security policy?',
        answer: `Security policy components:
1. Match criteria (source/destination zones)
2. Match conditions (addresses, applications)
3. Actions (permit/deny)
4. Application services
5. Policy options (logging, counting)`
    },
    // OSPF Configuration
    {
        category: 'routing',
        question: 'What are the basic steps to configure OSPF?',
        answer: `Basic OSPF configuration:
1. Enable OSPF:
set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
2. Configure router-id:
set routing-options router-id 10.0.0.1
3. Configure interface:
set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24`
    },
    // BGP Configuration
    {
        category: 'routing',
        question: 'How do you configure basic BGP?',
        answer: `Basic BGP configuration:
1. Configure AS number:
set routing-options autonomous-system 65000
2. Configure BGP group:
set protocols bgp group EXTERNAL-PEERS type external
3. Configure peer:
set protocols bgp group EXTERNAL-PEERS peer-as 65001
set protocols bgp group EXTERNAL-PEERS neighbor 192.168.1.2`
    },
    // Security
    {
        category: 'security',
        question: 'How do you configure basic NAT?',
        answer: `Basic source NAT configuration:
1. Create NAT pool:
set security nat source pool SNAT-POOL address 203.0.113.1/24
2. Configure rule set:
set security nat source rule-set RS1 from zone TRUST
set security nat source rule-set RS1 to zone UNTRUST
3. Configure rules:
set security nat source rule-set RS1 rule R1 match source-address 192.168.1.0/24
set security nat source rule-set RS1 rule R1 then source-nat pool SNAT-POOL`
    },
    // Interface Configuration
    {
        category: 'configuration',
        question: 'What are the steps to configure VLAN tagging?',
        answer: `1. Configure interface for VLAN tagging:
set interfaces ge-0/0/0 vlan-tagging

2. Create logical interfaces with VLAN IDs:
set interfaces ge-0/0/0 unit 10 vlan-id 10
set interfaces ge-0/0/0 unit 20 vlan-id 20`
    },
    // Security
    {
        category: 'security',
        question: 'What are security zones and how are they configured?',
        answer: `Security zones are logical segments that define security boundaries. Basic configuration:
1. Create zone:
set security zones security-zone TRUST
2. Add interface:
set security zones security-zone TRUST interfaces ge-0/0/0.0
3. Configure policies:
set security policies from-zone TRUST to-zone UNTRUST policy ALLOW-WEB`
    },
    // Add these to the flashcards array
    {
        category: 'routing',
        question: 'What are the BGP route selection criteria in order?',
        answer: `BGP route selection process:
1. Highest Local Preference
2. Shortest AS path
3. Lowest Origin code (IGP < EGP < Incomplete)
4. Lowest MED
5. EBGP over IBGP
6. Lowest IGP metric to next hop
7. Lowest Router ID
8. Lowest Peer IP address`
    },
    {
        category: 'security',
        question: 'What are the steps to configure IPsec VPN?',
        answer: `IPsec VPN configuration steps:
1. Configure IKE proposal (Phase 1):
   set security ike proposal IKE-PROP authentication-method pre-shared-keys
   set security ike proposal IKE-PROP dh-group group14
2. Configure IPsec proposal (Phase 2):
   set security ipsec proposal IPSEC-PROP protocol esp
3. Configure IKE gateway:
   set security ike gateway GW-1 ike-policy IKE-POL
4. Configure IPsec VPN:
   set security ipsec vpn VPN-1 ike gateway GW-1`
    },
    {
        category: 'switching',
        question: 'What are the components of MSTP?',
        answer: `MSTP components:
1. MST regions
2. IST (Internal Spanning Tree)
3. CST (Common Spanning Tree)
4. MSTI (Multiple Spanning Tree Instance)
5. Region Revision
6. Configuration Name
7. Instance VLAN mapping`
    },
    {
        category: 'troubleshooting',
        question: 'What are the steps to troubleshoot high CPU utilization?',
        answer: `High CPU troubleshooting:
1. Check process utilization:
   show system processes extensive
2. Monitor real-time CPU:
   monitor start /user/sbin/cpu
3. Check routing engine status:
   show chassis routing-engine
4. Review system logs:
   show log messages
5. Check interface statistics:
   show interfaces extensive`
    },
    {
        category: 'policy',
        question: 'What are the different NAT rule types and their use cases?',
        answer: `NAT rule types:
1. Source NAT (SNAT):
   - Hide internal addresses
   - Load balancing
2. Destination NAT (DNAT):
   - Public service hosting
   - Load balancing
3. Static NAT:
   - One-to-one mapping
   - Bidirectional access
4. Persistent NAT:
   - Application persistence
   - Gaming/streaming`
    },
    {
        category: 'high-availability',
        question: 'What are the requirements for chassis clustering?',
        answer: `Chassis cluster requirements:
1. Compatible hardware platforms
2. Same JunOS version
3. Control link connection
4. Fabric link connection
5. Matching interface configurations
6. Valid cluster ID (1-15)
7. Node ID configuration (0 or 1)`
    },
    {
        category: 'routing',
        question: 'What are the different types of OSPF areas and their characteristics?',
        answer: `OSPF area types:
1. Backbone Area (0):
   - All other areas connect to it
   - Carries all inter-area traffic
2. Standard Area:
   - Accepts all LSA types
   - Full routing information
3. Stub Area:
   - No external routes
   - Default route only
4. Totally Stubby:
   - Only default route
   - No external or inter-area routes
5. NSSA:
   - External routes converted to Type 7
   - Can have ASBR`
    },
    {
        category: 'security',
        question: 'What are the different authentication methods supported in JunOS?',
        answer: `Authentication methods:
1. Local password
2. RADIUS
3. TACACS+
4. SecurID
5. LDAP
6. Certificate-based

Configuration example:
set system authentication-order [radius tacplus password]`
    },
    {
        category: 'routing',
        question: 'What are the different types of routing instances in JunOS?',
        answer: `Routing instance types:
1. forwarding - Transparent bridge/layer 2 switch
2. l2backhaul-vpn - Layer 2 backhaul service
3. l2vpn - Layer 2 VPN
4. layer2-control - Layer 2 control protocols
5. virtual-router - Separate routing table
6. virtual-switch - VPLS instance
7. vpls - Virtual private LAN service
8. vrf - Layer 3 VPN routing/forwarding`
    },
    {
        category: 'switching',
        question: 'What are the different types of Layer 2 security features?',
        answer: `Layer 2 security features:
1. DHCP snooping
2. Dynamic ARP inspection
3. MAC limiting
4. Storm control
5. Port security
6. Root protection
7. BPDU protection
8. Loop prevention`
    },
    {
        category: 'troubleshooting',
        question: 'What are the key commands for troubleshooting IPsec VPN?',
        answer: `IPsec VPN troubleshooting commands:
1. show security ike security-associations
2. show security ipsec security-associations
3. show security ipsec statistics
4. show security flow session
5. show security ike statistics
6. show security ipsec tunnel-events
7. show security log`
    },
    {
        category: 'policy',
        question: 'What are the different types of ALGs (Application Layer Gateways)?',
        answer: `Common ALGs in JunOS:
1. FTP
2. TFTP
3. RSH
4. TALK
5. DNS
6. H.323
7. SIP
8. PPTP
9. SQL*Net
10. MSRPC`
    },
    {
        category: 'high-availability',
        question: 'What are the different types of VRRP authentication?',
        answer: `VRRP authentication:
1. Simple text password
2. MD5 authentication
3. No authentication

Key configuration:
set interfaces ge-0/0/0 unit 0 family inet vrrp-group 1 authentication-type md5
set interfaces ge-0/0/0 unit 0 family inet vrrp-group 1 authentication-key "$9$key"`
    },
    {
        category: 'routing',
        question: 'What are the different types of BGP communities?',
        answer: `BGP community types:
1. Standard communities (format: AS:value)
2. Extended communities
3. Large communities
4. Well-known communities:
   - no-export (65535:65281)
   - no-advertise (65535:65282)
   - no-export-subconfed (65535:65283)
   - no-peer (65535:65284)`
    },
    {
        category: 'security',
        question: 'What are the different types of screens in JunOS?',
        answer: `Screen types:
1. ICMP flood
2. UDP flood
3. SYN flood
4. Land attack
5. Teardrop attack
6. ICMP fragment
7. IP spoofing
8. Ping of death
9. TCP SYN-ACK-ACK proxy flood
10. IP sweep`
    },
    {
        category: 'troubleshooting',
        question: 'What are the steps to troubleshoot BGP route advertisement issues?',
        answer: `BGP route advertisement troubleshooting:
1. Verify BGP session state:
   show bgp summary
2. Check received routes:
   show route receive-protocol bgp neighbor-address
3. Check advertised routes:
   show route advertising-protocol bgp neighbor-address
4. Verify policy application:
   show policy policy-name
5. Check route presence in routing table:
   show route protocol bgp
6. Verify BGP export policies:
   show configuration protocols bgp group group-name export`
    },
    {
        category: 'switching',
        question: 'What are the different types of interface monitoring options?',
        answer: `Interface monitoring options:
1. Link aggregation monitoring
2. VRRP interface monitoring
3. BFD monitoring
4. RPM (Real-time Performance Monitoring)
5. Interface diagnostics
6. SNMP interface monitoring
7. Syslog monitoring
8. Interface statistics monitoring`
    },
    {
        category: 'routing',
        question: 'What are the OSPF network types and their characteristics?',
        answer: `OSPF network types:
1. Broadcast:
   - Multiple access networks
   - Uses DR/BDR
   - Example: Ethernet
2. Point-to-Point:
   - Two routers only
   - No DR/BDR election
   - Example: Serial links
3. Point-to-Multipoint:
   - Hub and spoke
   - No DR/BDR
4. Non-Broadcast:
   - Requires static neighbor config
   - Uses DR/BDR`
    },
    {
        category: 'security',
        question: 'What are the different types of user authentication methods in IPsec?',
        answer: `IPsec authentication methods:
1. Pre-shared keys (PSK)
2. RSA signatures
3. DSS signatures
4. X.509 certificates
5. Extended authentication (XAuth)
6. Internet Key Exchange (IKE)`
    },
    {
        category: 'switching',
        question: 'What are the different types of link aggregation in JunOS?',
        answer: `Link aggregation types:
1. Static LAG
2. LACP (Link Aggregation Control Protocol)
   - Active mode
   - Passive mode
3. Configuration example:
   set chassis aggregated-devices ethernet device-count 4
   set interfaces ae0 aggregated-ether-options lacp active`
    },
    {
        category: 'policy',
        question: 'What are the different types of security policy actions?',
        answer: `Security policy actions:
1. permit - Allow traffic
2. deny - Block traffic
3. reject - Block and send notification
4. count - Count matching traffic
5. log - Log matching traffic
6. services - Apply specific services`
    },
    {
        category: 'high-availability',
        question: 'What are the different types of BFD authentication?',
        answer: `BFD authentication types:
1. Simple password
2. Keyed MD5
3. Meticulous Keyed MD5
4. Keyed SHA-1
5. Meticulous Keyed SHA-1

Configuration:
set protocols bfd authentication algorithm keyed-sha-1
set protocols bfd authentication key-chain bfd-key`
    },
    {
        category: 'troubleshooting',
        question: 'What are the steps to troubleshoot VRRP issues?',
        answer: `VRRP troubleshooting steps:
1. Check VRRP state:
   show vrrp detail
2. Verify interface status:
   show interfaces terse
3. Check VRRP configuration:
   show configuration interfaces
4. Monitor VRRP messages:
   monitor traffic interface ge-0/0/0
5. Verify tracking configuration:
   show vrrp track`
    },
    {
        category: 'security',
        question: 'What are the different types of UTM features?',
        answer: `UTM (Unified Threat Management) features:
1. Antivirus
2. Web filtering
3. Content filtering
4. Antispam
5. SSL proxy
6. Application firewall
7. IPS (Intrusion Prevention)
8. Custom objects`
    },
    {
        category: 'routing',
        question: 'What are the different types of routing policies?',
        answer: `Routing policy types:
1. Import policies
2. Export policies
3. AS-path policies
4. Community policies
5. Prefix-list filters
6. Route-filter policies
7. Source address policies
8. Load-balancing policies`
    },
    {
        category: 'switching',
        question: 'What are the different types of storm control?',
        answer: `Storm control types:
1. Broadcast storm control
2. Multicast storm control
3. Unknown unicast storm control
4. Control packet storm control

Configuration:
set interfaces ge-0/0/0 unit 0 family ethernet-switching storm-control default`
    },
    {
        category: 'troubleshooting',
        question: 'What logs should you check for security issues?',
        answer: `Security logs to check:
1. show log messages
2. show log firewall
3. show log ips
4. show log utm
5. show log auth
6. show log security-events
7. show log system
8. show log chassisd`
    }
    // Continuing with more questions...
];

let currentCardIndex = 0;
let currentCards = [...flashcards];

const flashcardElement = document.getElementById('flashcard');
const questionElement = document.getElementById('question');
const answerElement = document.getElementById('answer');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const flipBtn = document.getElementById('flipBtn');
const cardNumberElement = document.getElementById('cardNumber');
const categorySelect = document.getElementById('categorySelect');

function updateCard() {
    const card = currentCards[currentCardIndex];
    questionElement.textContent = card.question;
    answerElement.textContent = card.answer;
    cardNumberElement.textContent = `Card ${currentCardIndex + 1} of ${currentCards.length}`;
    flashcardElement.classList.remove('flipped');
}

function filterCards() {
    const selectedCategory = categorySelect.value;
    currentCards = selectedCategory === 'all' 
        ? [...flashcards]
        : flashcards.filter(card => card.category === selectedCategory);
    currentCardIndex = 0;
    updateCard();
}

prevBtn.addEventListener('click', () => {
    currentCardIndex = (currentCardIndex - 1 + currentCards.length) % currentCards.length;
    updateCard();
});

nextBtn.addEventListener('click', () => {
    currentCardIndex = (currentCardIndex + 1) % currentCards.length;
    updateCard();
});

flipBtn.addEventListener('click', () => {
    flashcardElement.classList.toggle('flipped');
});

flashcardElement.addEventListener('click', () => {
    flashcardElement.classList.toggle('flipped');
});

categorySelect.addEventListener('change', filterCards);

// Initialize the first card
updateCard(); 

function createQuizFromFlashcards() {
    // Randomly select 5 cards from the flashcards array
    const shuffledCards = [...flashcards].sort(() => Math.random() - 0.5);
    const selectedCards = shuffledCards.slice(0, 5);
    
    return selectedCards.map(card => {
        // Create incorrect options by randomly selecting other answers
        let options = [card.answer.split('\n')[0]]; // Take first line of answer as correct option
        
        // Get 3 random wrong answers from other cards
        const otherAnswers = flashcards
            .filter(c => c !== card)
            .map(c => c.answer.split('\n')[0])
            .sort(() => Math.random() - 0.5)
            .slice(0, 3);
        
        options = [...options, ...otherAnswers];
        
        // Shuffle options
        options = options.sort(() => Math.random() - 0.5);
        
        return {
            question: card.question,
            options: options,
            correct: card.answer.split('\n')[0]
        };
    });
}

let currentQuizQuestions = [];
let currentQuizIndex = 0;
let quizScore = 0;

const quizContainer = document.getElementById('quizContainer');
const flashcardContainer = document.getElementById('flashcard');
const toggleQuizBtn = document.getElementById('toggleQuiz');
const quizQuestion = document.getElementById('quizQuestion');
const quizOptions = document.getElementById('quizOptions');
const submitQuizBtn = document.getElementById('submitQuiz');
const quizResult = document.getElementById('quizResult');
const quizScoreElement = document.getElementById('quizScore');

function toggleQuizMode() {
    if (quizContainer.style.display === 'none') {
        quizContainer.style.display = 'block';
        flashcardContainer.style.display = 'none';
        toggleQuizBtn.textContent = 'Switch to Flashcards';
        loadQuiz(); // Load new quiz
    } else {
        quizContainer.style.display = 'none';
        flashcardContainer.style.display = 'block';
        toggleQuizBtn.textContent = 'Switch to Quiz Mode';
    }
}

function loadQuiz() {
    currentQuizQuestions = createQuizFromFlashcards();
    currentQuizIndex = 0;
    quizScore = 0;
    displayCurrentQuestion();
}

function displayCurrentQuestion() {
    const quiz = currentQuizQuestions[currentQuizIndex];
    quizQuestion.textContent = quiz.question;
    quizOptions.innerHTML = '';
    
    quiz.options.forEach(option => {
        const button = document.createElement('div');
        button.className = 'quiz-option';
        button.textContent = option;
        button.onclick = () => selectOption(button);
        quizOptions.appendChild(button);
    });

    quizScoreElement.textContent = `Question ${currentQuizIndex + 1} of 5 | Score: ${quizScore}/5`;
}

function selectOption(selectedButton) {
    document.querySelectorAll('.quiz-option').forEach(button => {
        button.classList.remove('selected');
    });
    selectedButton.classList.add('selected');
}

function submitQuiz() {
    const selected = document.querySelector('.quiz-option.selected');
    if (!selected) {
        quizResult.textContent = 'Please select an answer!';
        return;
    }

    const quiz = currentQuizQuestions[currentQuizIndex];
    
    if (selected.textContent === quiz.correct) {
        quizScore++;
        quizResult.textContent = 'Correct!';
        quizResult.style.color = 'green';
    } else {
        quizResult.textContent = `Incorrect. The correct answer is: ${quiz.correct}`;
        quizResult.style.color = 'red';
    }

    quizScoreElement.textContent = `Question ${currentQuizIndex + 1} of 5 | Score: ${quizScore}/5`;
    
    // Move to next question after delay
    setTimeout(() => {
        currentQuizIndex++;
        if (currentQuizIndex < 5) {
            displayCurrentQuestion();
            quizResult.textContent = '';
        } else {
            quizQuestion.textContent = `Quiz completed! Final Score: ${quizScore}/5`;
            quizOptions.innerHTML = '';
            submitQuizBtn.style.display = 'none';
            
            // Add retry button
            const retryButton = document.createElement('button');
            retryButton.textContent = 'Try Another Quiz';
            retryButton.onclick = () => {
                submitQuizBtn.style.display = 'block';
                loadQuiz();
            };
            quizOptions.appendChild(retryButton);
        }
    }, 2000);
}

toggleQuizBtn.addEventListener('click', toggleQuizMode);
submitQuizBtn.addEventListener('click', submitQuiz);