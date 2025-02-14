# JUNOS 105 - 30 Day Study Plan

## Week 1: Fundamentals Review
### Days 1-2: Routing Basics
- Review IPv4/IPv6 routing concepts
  * Address formats and subnetting
  * Static vs Dynamic routing
  * Route preferences and selection
  * Route tables and forwarding
- Study routing tables and routing instances
  * inet.0, inet.1, inet.2, etc.
  * VRF instances
  * Logical systems
- Practice basic routing configuration
  * Interface configuration
  * Static routes
  * Default routes
  * Route preferences

### Days 3-4: Interface Configuration
- Interface types and properties
  * Gigabit Ethernet
  * Aggregated interfaces
  * Loopback interfaces
  * Tunnel interfaces
- Logical interfaces and units
  * Family inet/inet6
  * VLAN tagging
  * Interface properties
- Interface monitoring and troubleshooting
  * show interfaces extensive
  * monitor interface traffic
  * Interface diagnostics

### Days 5-7: Protocol Review
- OSPF configuration and verification
  * Area types (backbone, stub, NSSA)
  * Network types
  * Authentication
  * Route redistribution
- BGP basics and configuration
  * IBGP vs EBGP
  * Route reflection
  * Communities
  * Path attributes
- Route preferences and selection
  * Administrative distance
  * BGP path selection
  * OSPF path cost

## Week 2: Security Focus
### Days 8-10: Security Zones and Policies
- Security zone configuration
  * Security zones vs functional zones
  * Host inbound traffic
  * Interface assignment
- Security policies
  * Match criteria
  * Actions (permit/deny/reject)
  * Application services
  * Logging options
- NAT configuration
  * Source NAT
  * Destination NAT
  * Static NAT
  * Persistent NAT

### Days 11-14: VPNs and IPsec
- IPsec concepts
- VPN configuration
- Tunnel interfaces
- IKE configuration

## Week 3: Advanced Features
### Days 15-17: Class of Service
- CoS configuration
- Classifiers and forwarding classes
- Schedulers and rewrite rules
- Queue monitoring

### Days 18-21: High Availability
- VRRP configuration
- Chassis clustering
- Redundancy groups
- Failover configuration

## Week 4: Troubleshooting and Practice
### Days 22-24: Troubleshooting Tools
- Logging and tracing
- Show commands mastery
- Performance monitoring
- Common issues and solutions

### Days 25-27: Lab Scenarios
- Practice lab scenarios
- Common deployment configurations
- Performance optimization
- Security implementations

### Days 28-30: Final Preparation
- Review weak areas
- Practice exams
- Command quick reference
- Configuration verification

## Daily Study Routine
1. Morning (1 hour):
   - Review previous day's material
   - Read documentation on new topics

2. Afternoon (2 hours):
   - Hands-on lab practice
   - Configuration exercises

3. Evening (1 hour):
   - Flashcard review
   - Practice questions

## Key Focus Areas
1. Routing Protocols (25%)
2. Security Features (25%)
3. Interface Configuration (20%)
4. Troubleshooting (20%)
5. High Availability (10%)

## Resources
1. Official Juniper Documentation
2. Lab Environment (virtual or physical)
3. Practice Tests
4. Configuration Guides

## Tips
1. Create a lab environment using vSRX
2. Practice configurations daily
3. Document common issues and solutions
4. Use commit confirmed for testing
5. Master show commands 

## Daily Lab Exercises

### Week 1 Labs
1. Basic Router Setup
   ```junos
   set system host-name ROUTER1
   set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
   set routing-options static route 0.0.0.0/0 next-hop 192.168.1.254
   ```

2. OSPF Configuration
   ```junos
   set protocols ospf area 0.0.0.0 interface ge-0/0/0.0
   set protocols ospf area 0.0.0.0 interface lo0.0 passive
   ```

3. BGP Setup
   ```junos
   set routing-options autonomous-system 65000
   set protocols bgp group EXTERNAL type external
   set protocols bgp group EXTERNAL peer-as 65001
   set protocols bgp group EXTERNAL neighbor 192.168.1.2
   ```

### Week 2 Labs
[Continue with detailed lab configurations...]

## Verification Commands Cheatsheet
1. Routing Verification
   - show route
   - show route protocol ospf
   - show route protocol bgp
   - show route table inet.0

2. Interface Verification
   - show interfaces terse
   - show interfaces extensive
   - show interfaces diagnostics optics

[Continue with more sections...] 