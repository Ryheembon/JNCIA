# JUNOS 105 Daily Study Guide

## Week 1: Routing Fundamentals

### Day 1: Basic Routing Concepts
**Daily Goals:**
1. Understand routing tables
2. Learn route preferences
3. Configure basic interfaces

**Tasks:**
- [ ] Study inet.0 through inet.6 routing tables
- [ ] Practice 'show route' commands
- [ ] Configure 2 interfaces with IPv4/IPv6

**Lab Exercise:**
```junos
# Basic interface and routing configuration
set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
set interfaces ge-0/0/1 unit 0 family inet address 10.0.0.1/24
show route
show interfaces terse
```

### Day 2: Static Routing
**Daily Goals:**
1. Configure static routes
2. Understand next-hop options
3. Implement default routes

**Tasks:**
- [ ] Configure 3 static routes
- [ ] Test route reachability
- [ ] Document route preferences

### Day 3: OSPF Basics
**Daily Goals:**
1. Configure basic OSPF
2. Understand area types
3. Verify OSPF neighbors

**Tasks:**
- [ ] Set up OSPF area 0
- [ ] Configure OSPF interfaces
- [ ] Verify neighbor relationships

### Day 4: BGP Fundamentals
**Daily Goals:**
1. Understand BGP path attributes
2. Configure EBGP session
3. Verify BGP routes

**Tasks:**
- [ ] Configure BGP peer
- [ ] Set up route advertising
- [ ] Check BGP path selection

## Week 2: Security

### Day 8: Security Zones
**Daily Goals:**
1. Configure security zones
2. Set up interfaces in zones
3. Implement basic policies

**Tasks:**
- [ ] Create TRUST and UNTRUST zones
- [ ] Assign interfaces to zones
- [ ] Configure initial security policies

**Lab Exercise:**
```junos
# Basic security configuration
set security zones security-zone TRUST interfaces ge-0/0/0.0
set security zones security-zone UNTRUST interfaces ge-0/0/1.0
set security policies from-zone TRUST to-zone UNTRUST policy ALLOW-WEB
```

[Continue with daily goals for each day...]

## Daily Review Checklist
□ Review previous day's concepts
□ Complete all lab exercises
□ Test configurations
□ Document new commands learned
□ Update study notes
□ Review related flashcards
□ Practice troubleshooting

## Progress Tracking
- Keep a daily log of completed tasks
- Note areas needing more focus
- Track lab exercise completion
- Document configuration mistakes
- Record successful troubleshooting

## Daily Time Allocation
1. **Morning Study (1 hour)**
   - Theory review
   - Documentation reading
   - Command syntax review

2. **Lab Practice (2 hours)**
   - Configuration exercises
   - Troubleshooting practice
   - Verification commands

3. **Evening Review (1 hour)**
   - Flashcard review
   - Documentation updates
   - Next day preparation
